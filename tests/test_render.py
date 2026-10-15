import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from PIL import Image

from server.render import DEFAULT_FIXTURE, render


ROOT = Path(__file__).resolve().parents[1]


class RendererSmokeTest(unittest.TestCase):
    def test_cli_generates_repeatable_grayscale_png(self):
        with tempfile.TemporaryDirectory() as directory:
            paths = [Path(directory) / name for name in ("first.png", "second.png")]
            for path in paths:
                # Run outside the repo to check fixture path resolution as well.
                subprocess.run(
                    [sys.executable, str(ROOT / "server/render.py"), "--output", str(path)],
                    cwd=directory, check=True, capture_output=True, text=True,
                )
                with Image.open(path) as image:
                    self.assertEqual(image.format, "PNG")
                    self.assertEqual(image.size, (758, 1024))
                    self.assertEqual(image.mode, "L")
                    self.assertEqual(image.getextrema(), (0, 255))
                    # Every major content band must contain visible ink.
                    for top, bottom in [(20, 164), (180, 450), (480, 700), (730, 910), (935, 1010)]:
                        band = image.crop((35, top, 723, bottom))
                        self.assertLess(band.getextrema()[0], 255)
            self.assertEqual(paths[0].read_bytes(), paths[1].read_bytes())

    def test_future_forecast_timestamp_is_rejected(self):
        data = json.loads(DEFAULT_FIXTURE.read_text())
        data["generated_at"] = "2026-10-15T07:30:00+02:00"
        with self.assertRaisesRegex(ValueError, "cannot precede"):
            render(data)


if __name__ == "__main__":
    unittest.main()
