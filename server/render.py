"""Render offline fixture data; no network, clock, or device access."""

import argparse
from datetime import datetime
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


SIZE = (758, 1024)
DEFAULT_FIXTURE = Path(__file__).parent / "fixtures" / "weather.json"


def render(data):
    updated = datetime.fromisoformat(data["forecast_updated_at"])
    generated = datetime.fromisoformat(data["generated_at"])
    if updated.utcoffset() is None or generated.utcoffset() is None:
        raise ValueError("Timestamps must include a UTC offset")
    age_minutes = int((generated - updated).total_seconds() // 60)
    if age_minutes < 0:
        raise ValueError("Generation time cannot precede forecast update time")
    if len(data["hourly"]) != 6 or len(data["daily"]) != 3:
        raise ValueError("Fixture must contain six hourly entries and three daily entries")

    image = Image.new("L", SIZE, 255)
    draw = ImageDraw.Draw(image)

    def text(x, y, value, size=28, anchor=None):
        # Pillow's bundled Aileron font avoids host-specific font paths.
        draw.text((x, y), str(value), fill=0,
                  font=ImageFont.load_default(size=size), anchor=anchor)

    def rule(y):
        draw.line((40, y, 718, y), fill=0, width=3)

    text(40, 30, "WEATHER / SAMPLE DATA", 23)
    text(40, 69, data["location"], 38)
    text(40, 122, generated.strftime("%a %d %b %Y"), 24)
    rule(164)

    current = data["current"]
    text(40, 184, f'{current["temperature_c"]:g} C', 108)
    text(44, 312, current["condition"], 37)
    text(44, 370, f'Feels like {current["feels_like_c"]:g} C', 27)
    text(44, 411, f'Chance of rain {current["precipitation_probability_pct"]:g}%', 27)
    rule(465)

    text(40, 486, "TODAY / TEMPERATURE", 23)
    hours = data["hourly"]
    values = [hour["temperature_c"] for hour in hours]
    low, high = min(values) - 2, max(values) + 2
    points = [(70 + i * 123, 646 - (value - low) / (high - low) * 92)
              for i, value in enumerate(values)]
    draw.line(points, fill=0, width=4)
    for hour, (x, y) in zip(hours, points):
        draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill=0)
        text(x, y - 39, f'{hour["temperature_c"]:g}', 25, "mt")
        text(x, 666, hour["time"], 21, "mt")
    rule(712)

    for index, day in enumerate(data["daily"]):
        y = 739 + index * 58
        text(40, y, day["day"], 25)
        text(194, y, day["condition"], 25)
        text(718, y, f'{day["low_c"]:g} / {day["high_c"]:g} C', 25, "rt")
    rule(923)
    text(40, 939, f'Generated {generated.strftime("%d %b %H:%M %z")}', 20)
    text(40, 974, f'Forecast {updated.strftime("%H:%M %z")} / age at generation: {age_minutes} min', 20)
    return image


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--output", type=Path, default=Path("weather.png"))
    args = parser.parse_args()
    with args.fixture.open(encoding="utf-8") as fixture:
        image = render(json.load(fixture))
    image.save(args.output, format="PNG")
    print(f"Wrote {args.output}: {image.width}x{image.height}, grayscale ({image.mode})")


if __name__ == "__main__":
    main()
