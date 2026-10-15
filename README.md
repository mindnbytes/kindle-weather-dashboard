# Kindle weather dashboard

An offline fixture renderer for a Kindle Paperwhite 1 display. The **Mac-side
half of M2** has passed its renderer checks. Owner-directed **Windows M1 setup**
is now in progress: PW1 jailbreak/hotfix, return to 5.6.1.1, KUAL/MRPI and
USBNetwork installation have passed recorded checkpoints. A USB-only SSH smoke
check passed with verified host key, public-key root login and read-only shell
commands. USB storage mode and original Windows adapter DHCP/DNS settings were
restored and verified afterward. Wi-Fi configuration/access and Mac SSH remain
pending.
Weather APIs, serving, and scheduling remain later milestones. Read the
[project brief](kindle-weather-dashboard.md) for safety and review gates.

Device evidence and approved actions are in [the experiment log](docs/experiments.md)
and [access plan](docs/jailbreak.md). Keep the Kindle in airplane mode until
reviewed network isolation and access setup. Renderer commands below remain
for Mac/Nix development; no regeneration is needed on Windows.

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

**Renderer review point:** the generated image was inspected on the Mac before
owner-approved Kindle setup began. Physical display testing remains pending;
the renderer itself does not establish console access or modify the device.
