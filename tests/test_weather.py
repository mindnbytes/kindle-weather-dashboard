from datetime import datetime, timedelta, timezone
from http.server import ThreadingHTTPServer
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import unittest
from urllib.error import HTTPError
from urllib.request import urlopen

from server.serve import handler_for
from server.weather import normalize, update, validate_config


NOW = datetime(2026, 10, 15, 23, 30, tzinfo=timezone.utc)
CONFIG = {"location": "Test town", "latitude": 0, "longitude": 0}


def response():
    fixture = Path(__file__).resolve().parents[1] / "server/fixtures/open-meteo.json"
    return json.loads(fixture.read_text())


class WeatherTests(unittest.TestCase):
    def test_offline_fixture_cli_is_repeatable_and_marked_sample(self):
        root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as directory:
            outputs = []
            for name in ("first", "second"):
                destination = Path(directory) / name
                subprocess.run([sys.executable, "-m", "server.weather", "--fixture",
                                "server/fixtures/open-meteo.json", "--state-dir", str(destination)],
                               cwd=root, check=True, capture_output=True)
                outputs.append((destination / "weather.png").read_bytes())
                self.assertEqual(json.loads((destination / "forecast.json").read_text())["source"],
                                 "SAMPLE DATA")
            self.assertEqual(*outputs)

    def test_midnight_selection_and_distinct_snow_storm(self):
        data = normalize(response(), CONFIG, NOW)
        self.assertEqual([h["time"] for h in data["hourly"]],
                         ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00"])
        self.assertEqual(data["current"]["precipitation_probability_pct"], 20)
        self.assertEqual(data["current"]["condition"], "Snow")
        self.assertEqual([h["condition"] for h in data["hourly"]],
                         ["cloudy", "rain", "rain", "snow", "storm", "partly_cloudy"])
        self.assertEqual(data["daily"][0]["day"], "Fri 16")

    def test_offset_applies_to_display_times_and_daily_boundaries(self):
        raw = response()
        raw["utc_offset_seconds"] = 7200
        raw["current"]["time"] -= 7200
        raw["hourly"]["time"] = [stamp - 7200 for stamp in raw["hourly"]["time"]]
        raw["daily"]["time"] = [stamp - 7200 for stamp in raw["daily"]["time"]]
        data = normalize(raw, CONFIG, NOW - timedelta(hours=2))
        self.assertTrue(data["generated_at"].endswith("+02:00"))
        self.assertEqual(data["hourly"][0]["time"], "00:00")
        self.assertEqual(data["daily"][0]["day"], "Fri 16")

    def test_missing_values_and_short_horizon_rejected(self):
        for mutate in (
            lambda raw: raw["current"].update(temperature_2m=None),
            lambda raw: raw["hourly"].update(time=[]),
            lambda raw: raw["daily"].update(time=[]),
            lambda raw: raw["current"].update(weather_code=1000),
        ):
            raw = response()
            mutate(raw)
            with self.assertRaises(ValueError):
                normalize(raw, CONFIG, NOW)
        with self.assertRaises(ValueError):
            normalize(response(), CONFIG, NOW + timedelta(hours=3))

    def test_failed_fetch_or_validation_preserves_last_publication(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            update(CONFIG, root, fetcher=lambda config: response(), now=NOW)
            original = {p.name: p.read_bytes() for p in root.iterdir()}

            def offline(config):
                raise OSError("offline")

            for fetcher in (offline, lambda config: {"broken": True}):
                with self.assertRaises((OSError, KeyError)):
                    update(CONFIG, root, fetcher=fetcher, now=NOW)
                self.assertEqual(original, {p.name: p.read_bytes() for p in root.iterdir()})
            data = json.loads((root / "forecast.json").read_text())
            self.assertEqual(data["source"], "Open-Meteo.com")

    def test_config_requires_explicit_finite_coordinates(self):
        for value in (None, float("nan"), 91):
            with self.assertRaises(ValueError):
                validate_config(dict(CONFIG, latitude=value))

    def test_http_exact_bytes_missing_image_and_private_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            server = ThreadingHTTPServer(("127.0.0.1", 0), handler_for(root / "weather.png"))
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            base = f"http://127.0.0.1:{server.server_port}"
            try:
                with self.assertRaises(HTTPError) as error:
                    urlopen(base + "/weather.png")
                self.assertEqual(error.exception.code, 503)
                error.exception.close()
                update(CONFIG, root, fetcher=lambda config: response(), now=NOW)
                with urlopen(base + "/weather.png") as result:
                    self.assertEqual(result.headers["Content-Type"], "image/png")
                    self.assertEqual(result.headers["Cache-Control"], "no-store")
                    self.assertEqual(result.read(), (root / "weather.png").read_bytes())
                for path in ("/", "/forecast.json", "/../forecast.json"):
                    with self.assertRaises(HTTPError) as error:
                        urlopen(base + path)
                    self.assertEqual(error.exception.code, 404)
                    error.exception.close()
            finally:
                server.shutdown()
                server.server_close()
                thread.join()


if __name__ == "__main__":
    unittest.main()
