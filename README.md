# Kindle weather dashboard

An offline fixture renderer for a Kindle Paperwhite 1 display. Current scope is
the **Mac-side half of M2**: produce and inspect a PNG. Device access, weather
APIs, serving, and scheduling are later milestones. Read the
[project brief](kindle-weather-dashboard.md) for safety and review gates.

## Development with Nix

Requires Nix with `nix-command` and `flakes` enabled. From this directory:

```sh
nix develop
python server/render.py
python -m unittest discover -s tests -v
file weather.png
```

The first `nix develop` may download dependencies. Subsequent rendering and tests
use local fixture data and require no network. `flake.lock` pins the development
environment; Python and Pillow are the only runtime dependencies. The flake is a
development shell, with no NixOS service or deployment configuration.

Without entering an interactive shell:

```sh
nix develop -c python server/render.py
nix develop -c python -m unittest discover -s tests -v
```

## CLI and inspection

```sh
python server/render.py --fixture server/fixtures/weather.json --output weather.png
python server/render.py --help
python -c 'from PIL import Image; im = Image.open("weather.png"); print(im.format, im.size, im.mode)'
```

Expected: `PNG (758, 1024) L`, an 8-bit grayscale portrait image. On macOS, open
`weather.png` in Preview and inspect at actual size for legible text, margins,
and an unclipped hourly strip and three-day forecast. Each hourly column shows
temperature, a monochrome condition icon, rain probability, and time. Fixture
condition values are `sunny`, `cloudy`, `partly_cloudy`, or `rain`.

The fixture describes **invented sample weather**, with no personal coordinates.
It deliberately provides both forecast and generation timestamps with UTC
offsets. The renderer never reads the system clock: identical input produces
identical PNG bytes in the pinned environment. The footer shows forecast age
**at generation**, which does not advance while the image is displayed.

The renderer uses Pillow's bundled Aileron font (distributed by Pillow under the
SIL Open Font License), avoiding macOS font dependencies. Its layout uses the
same font on Linux; no project font download or installation is needed.

The smoke test runs the CLI twice from another working directory, verifies PNG
format/dimensions/grayscale, checks that content bands contain ink, and compares
the output bytes. Visual inspection complements these checks. E-ink contrast,
orientation, ghosting, and UI overwrite behavior still require later device
testing.

**Review point:** inspect the generated image before proceeding to Kindle-side
work. This repository does not establish console access or modify the device.
