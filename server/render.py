"""Render offline fixture data; no network, clock, or device access."""

import argparse
from datetime import datetime
import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


SIZE = (758, 1024)
DEFAULT_FIXTURE = Path(__file__).parent / "fixtures" / "weather.json"


def weather_icon(draw, x, y, condition):
    """Draw small monochrome symbols without external assets or emoji fonts."""
    if condition not in {"sunny", "cloudy", "partly_cloudy", "rain", "snow", "storm"}:
        raise ValueError(f"Unsupported hourly condition: {condition}")
    if condition in {"sunny", "partly_cloudy"}:
        sx, sy = (x, y) if condition == "sunny" else (x - 11, y - 9)
        for index in range(8):
            angle = index * math.pi / 4
            draw.line((sx + 20 * math.cos(angle), sy + 20 * math.sin(angle),
                       sx + 26 * math.cos(angle), sy + 26 * math.sin(angle)),
                      fill=0, width=3)
        draw.ellipse((sx - 14, sy - 14, sx + 14, sy + 14), fill=255, outline=0, width=3)
    if condition != "sunny":
        # Union the shapes before outlining so there are no internal seams.
        cloud = Image.new("L", (80, 80), 0)
        shape = ImageDraw.Draw(cloud)
        shape.ellipse((10, 27, 36, 53), fill=255)
        shape.ellipse((28, 13, 60, 48), fill=255)
        shape.rounded_rectangle((14, 35, 66, 53), radius=9, fill=255)
        draw.bitmap((x - 38, y - 30), cloud.filter(ImageFilter.MaxFilter(7)), fill=0)
        draw.bitmap((x - 38, y - 30), cloud, fill=255)
    if condition == "rain":
        for dx in (-14, 1, 16):
            draw.line((x + dx, y + 29, x + dx - 5, y + 37), fill=0, width=3)
    if condition == "snow":
        for dx in (-16, 4, 24):
            draw.line((x + dx - 4, y + 30, x + dx + 4, y + 38), fill=0, width=2)
            draw.line((x + dx - 4, y + 38, x + dx + 4, y + 30), fill=0, width=2)
    if condition == "storm":
        draw.line((x + 6, y + 24, x - 5, y + 34, x + 3, y + 34, x - 8, y + 44), fill=0, width=3)


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

    text(40, 30, f'WEATHER / {data.get("source", "SAMPLE DATA")}', 23)
    text(40, 69, data["location"], 38)
    text(40, 122, generated.strftime("%a %d %b %Y"), 24)
    rule(164)

    current = data["current"]
    text(40, 184, f'{current["temperature_c"]:g} C', 108)
    text(44, 312, current["condition"], 37)
    text(44, 370, f'Feels like {current["feels_like_c"]:g} C', 27)
    text(44, 411, f'{current.get("precipitation_label", "Chance of rain")} {current["precipitation_probability_pct"]:g}%', 27)
    rule(465)

    text(40, 486, "HOURLY FORECAST / C", 23)
    hours = data["hourly"]
    for index, hour in enumerate(hours):
        x = 91 + index * 115
        text(x, 530, f'{hour["temperature_c"]:g}°', 30, "mt")
        weather_icon(draw, x, 591, hour["condition"])
        text(x, 636, f'{hour["precipitation_probability_pct"]:g}%', 25, "mt")
        text(x, 666, hour["time"], 21, "mt")
    rule(712)

    for index, day in enumerate(data["daily"]):
        y = 739 + index * 58
        text(40, y, day["day"], 25)
        text(194, y, day["condition"], 25)
        text(718, y, f'{day["low_c"]:g} / {day["high_c"]:g} C', 25, "rt")
    rule(923)
    text(40, 939, f'Generated {generated.strftime("%d %b %H:%M %z")}', 20)
    label = data.get("forecast_time_label", "Forecast")
    text(40, 974, f'{label} {updated.strftime("%H:%M %z")} / age at generation: {age_minutes} min', 20)
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
