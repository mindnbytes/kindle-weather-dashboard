# Kindle weather dashboard

An offline fixture renderer for a Kindle Paperwhite 1 display. **M1 console
access and M2's first end-to-end PNG display are complete; M0 preparation is also
complete.** PW1 jailbreak/hotfix,
return to 5.6.1.1, KUAL/MRPI and
USBNetwork installation have passed recorded checkpoints. A USB-only SSH smoke
check passed with verified host key, public-key root login and read-only shell
commands. USB storage mode and original Windows adapter DHCP/DNS settings were
restored and verified afterward. Windows Wi-Fi SSH now passes with USB unplugged,
verified host key, public-key root login and repeat connections. The approved
WIFI_NO_NET_PROBE flag resolved offline WLAN validation failures. A bounded
IPv4 HTTP probe was refused on Kindle while Windows reached the same endpoint;
broader isolation coverage remains unproven. The Kindle-only Speedport blocker
stays enabled. Owner also confirmed Mac public-key SSH and all four shell checks.
The existing hotfix-supplied FBInk 1.25.0 displayed the Mac fixture PNG after
SCP transfer and matching SHA-256 read-back. Owner confirmed it rendered and
looked perfect, but later observed the original UI returning and touches
operating the UI through the image. The PNG draw does not establish persistent
dashboard mode. Screen ownership, touch handling and lock/suspend retention are
explicit M4 gates. The approved procedure is in the [first-image action sheet](docs/first-image-action-sheet.md).
Owner requested a pause; this session's server stop/airplane-mode teardown has
been requested but not yet confirmed. SSH startup remains manual. Next is M3:
weather acquisition, caching and local HTTP delivery on Mac/Nix; NixOS deployment
and unattended refresh come later. The Mac M3 pipeline now supports an invented
Open-Meteo-shaped fixture, validated normalization/cache, atomic PNG publication
and loopback HTTP delivery. Live acquisition has had one non-personal smoke
check; real-location and Kindle LAN retrieval acceptance remain pending.
Read the
[project brief](kindle-weather-dashboard.md) for safety and review gates.

Device evidence and approved actions are in [the experiment log](docs/experiments.md)
and [access plan](docs/jailbreak.md). Use only the reviewed protected LAN for
SSH and return to airplane mode when parked. Renderer commands below remain
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

## M3 offline data-to-HTTP workflow

```sh
nix develop -c python -m server.weather --fixture server/fixtures/open-meteo.json
nix develop -c python -m server.serve
```

Fetch `http://127.0.0.1:8000/weather.png` locally and stop the server with Ctrl-C.
This leaves the original M2 `weather.png` untouched. See [the pipeline guide](docs/weather-pipeline.md)
for fixture/API correspondence, caching and outage behavior, private live config,
validation, and the later explicit LAN binding. Invented data remains the current
workflow; no Kindle changes or background services are included.

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
the output bytes. Visual inspection complements these checks. Owner accepted the
first physical display; stock UI overwrite and active underlying touch handling
are observed limitations. Overwrite timing, long-term ghosting and sleep/wake
behavior remain unmeasured.

**Renderer review point:** the generated image was inspected on the Mac before
owner-approved Kindle setup began, then transferred and displayed successfully
on the PW1. This establishes the manual fixture-to-screen slice, not automated
weather delivery or persistence through sleep.
