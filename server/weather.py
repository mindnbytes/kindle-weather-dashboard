"""One-shot Open-Meteo acquisition and publication; run with python -m server.weather."""

import argparse
from datetime import datetime, timedelta, timezone
import io
import json
import math
import os
from pathlib import Path
import sys
import tempfile
from urllib.parse import urlencode
from urllib.request import urlopen

from server.render import render


def atomic_write(path, content):
    """Readers see either the previous complete file or the new complete file."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as stream:
        temporary = Path(stream.name)
        try:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        except BaseException:
            temporary.unlink(missing_ok=True)
            raise
    try:
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError("Missing or non-finite weather value")
    return value


def condition(code):
    """Short labels fit the existing layout; icon vocabulary stays explicit."""
    code = number(code)
    if code in (0, 1):
        return "Clear", "sunny"
    if code == 2:
        return "Partly cloudy", "partly_cloudy"
    if code == 3:
        return "Overcast", "cloudy"
    if code in (45, 48):
        return "Fog", "cloudy"
    if code in (51, 53, 55, 56, 57):
        return "Drizzle", "rain"
    if code in (61, 63, 65, 66, 67, 80, 81, 82):
        return "Rain", "rain"
    if code in (71, 73, 75, 77, 85, 86):
        return "Snow", "snow"
    if code in (95, 96, 97, 99):
        return "Thunderstorm", "storm"
    raise ValueError(f"Unsupported weather code: {code}")


def validate_config(config):
    for key, limit in (("latitude", 90), ("longitude", 180)):
        if abs(number(config[key])) > limit:
            raise ValueError(f"Invalid {key}")
    label = config["location"]
    if not isinstance(label, str) or not label.strip() or len(label) > 24:
        raise ValueError("Location label must contain 1–24 characters")
    return config


def fetch(config):
    query = urlencode({
        "latitude": config["latitude"], "longitude": config["longitude"],
        "timezone": "auto", "timeformat": "unixtime", "forecast_days": 4,
        "temperature_unit": "celsius",
        "current": "temperature_2m,apparent_temperature,weather_code",
        "hourly": "temperature_2m,precipitation_probability,weather_code",
        "daily": "temperature_2m_min,temperature_2m_max,weather_code",
    })
    with urlopen("https://api.open-meteo.com/v1/forecast?" + query, timeout=20) as response:
        return json.load(response)


def normalize(raw, config, now):
    if now.utcoffset() is None:
        raise ValueError("Generation time needs a UTC offset")
    # API daily boundaries use the fixed offset resolved at request time.
    zone = timezone(timedelta(seconds=number(raw["utc_offset_seconds"])))
    local = lambda stamp: datetime.fromtimestamp(number(stamp), zone)
    current = raw["current"]
    valid = local(current["time"])
    if valid > now or now - valid > timedelta(hours=2):
        raise ValueError("Current conditions timestamp is future or over two hours old")
    hours = raw["hourly"]
    indices = [i for i, stamp in enumerate(hours["time"]) if stamp >= current["time"]][:6]
    if len(indices) != 6:
        raise ValueError("Need six upcoming hourly entries")
    # Current rain chance is the probability for the hour containing current.time.
    containing = [i for i, stamp in enumerate(hours["time"]) if stamp <= current["time"]]
    if not containing or current["time"] - hours["time"][containing[-1]] >= 3600:
        raise ValueError("No hourly precipitation probability for current conditions")

    def probability(index):
        value = number(hours["precipitation_probability"][index])
        if not 0 <= value <= 100:
            raise ValueError("Invalid precipitation probability")
        return value

    daily = raw["daily"]
    days = [i for i, stamp in enumerate(daily["time"]) if local(stamp).date() > valid.date()][:3]
    if len(days) != 3:
        raise ValueError("Need three future forecast days")
    return {
        "location": config["location"], "source": "Open-Meteo.com",
        "forecast_updated_at": valid.isoformat(), "generated_at": now.astimezone(zone).isoformat(),
        "forecast_time_label": "Valid",
        "current": {"temperature_c": number(current["temperature_2m"]),
                    "feels_like_c": number(current["apparent_temperature"]),
                    "condition": condition(current["weather_code"])[0],
                    "precipitation_label": "Precipitation chance",
                    "precipitation_probability_pct": probability(containing[-1])},
        "hourly": [{"time": local(hours["time"][i]).strftime("%H:%M"),
                    "temperature_c": number(hours["temperature_2m"][i]),
                    "condition": condition(hours["weather_code"][i])[1],
                    "precipitation_probability_pct": probability(i)} for i in indices],
        "daily": [{"day": local(daily["time"][i]).strftime("%a %d"),
                   "condition": condition(daily["weather_code"][i])[0],
                   "low_c": number(daily["temperature_2m_min"][i]),
                   "high_c": number(daily["temperature_2m_max"][i])} for i in days],
    }


def update(config, state_dir, *, fetcher=fetch, now=None, source="Open-Meteo.com"):
    """On fetch/validation/render failure, leave the previous PNG and cache intact."""
    validate_config(config)
    raw = fetcher(config)
    data = normalize(raw, config, now or datetime.now(timezone.utc))
    data["source"] = source
    image = render(data)
    output = io.BytesIO()
    image.save(output, format="PNG")
    # Cache the validated normalized snapshot privately, outside the HTTP route.
    atomic_write(Path(state_dir) / "forecast.json", json.dumps(data).encode())
    atomic_write(Path(state_dir) / "weather.png", output.getvalue())
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    inputs = parser.add_mutually_exclusive_group(required=True)
    inputs.add_argument("--config", type=Path, help="Private coordinates; performs a live API request")
    inputs.add_argument("--fixture", type=Path, help="Invented Open-Meteo response; no network")
    parser.add_argument("--state-dir", type=Path, default=Path("runtime"))
    args = parser.parse_args()
    try:
        if args.fixture:
            raw = json.loads(args.fixture.read_text())
            # Fixed fixture generation time keeps the offline pipeline repeatable.
            generated = datetime.fromtimestamp(raw["current"]["time"], timezone.utc) + timedelta(minutes=15)
            update({"location": "Sample town", "latitude": 0, "longitude": 0},
                   args.state_dir, fetcher=lambda config: raw, now=generated, source="SAMPLE DATA")
        else:
            update(json.loads(args.config.read_text()), args.state_dir)
    except (OSError, ValueError, KeyError, IndexError, TypeError) as error:
        # Do not echo request URLs (coordinates) or provider response bodies.
        print(f"Update failed ({type(error).__name__}); previous files retained where present.", file=sys.stderr)
        return 1
    print(f"Published {args.state_dir / 'weather.png'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
