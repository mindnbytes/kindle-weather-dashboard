# Experiments

## 2026-10-15 — M2 Mac-side fixture image

Scope: renderer only. No Kindle connection, device modification, API request,
HTTP server, scheduling, or deployment performed.

Environment observed: macOS 26.7.1 (25G241), Nix 2.34.7. The pinned development
shell provides Python 3.14.7 and Pillow 12.3.0. See `flake.lock` for the exact
nixpkgs revision. An initial uv attempt failed on cache permissions; no virtual
environment was installed. Development switched to Nix at the owner's request.
Nix commands required access to the host Nix daemon outside the execution sandbox.

Commands completed successfully from the project root:

```sh
nix develop -c python server/render.py
nix develop -c python -m unittest discover -s tests -v
file weather.png
shasum -a 256 weather.png
```

Results:

- Both tests passed: CLI output is repeatable, and a generation timestamp before
  the forecast timestamp is rejected.
- `file`: `PNG image data, 758 x 1024, 8-bit grayscale, non-interlaced`.
- SHA-256: `c3eeb29e59bf9657b9e147e7c33a84aa78b9789ba166dae83a2c1782d36ee352`.
- Image inspected visually: portrait orientation, clear margins, no visible text
  clipping or overlaps in the fixture layout. Current temperature, hourly trend,
  three forecast rows, and timestamp footer are visible.

Limits: repeatability was tested in this pinned macOS environment, not across
platforms. Layout is designed for the supplied fixture; arbitrary long location
or condition strings have no automatic wrapping. No evidence yet of Kindle
rendering, physical readability, ghosting, or screen retention.

Next action: owner reviews `weather.png`. Stop here before Kindle-side work.

## 2026-10-15 — Hourly forecast strip

Replaced the hourly line chart with six aligned columns following the owner's
`example.png`: temperature, monochrome condition icon, rain probability, and
time. Updated the invented fixture to consecutive hours (09:00–14:00) with
cloudy, partly cloudy, sunny, and rain examples. Icons are drawn with Pillow;
no assets, fonts, or dependencies were added.

Regenerated using `nix develop -c python server/render.py`; both existing tests
passed again, and `git diff --check` passed. Output remains 758x1024 grayscale.
Visually inspected the final PNG: columns align and labels/icons do not overlap.
Final SHA-256:
`61b53b2ce823552e888b5a52da5c30628758db4de5956dae36f67604163eb561`.

Next action: owner reviews the revised image. Changes are not committed yet.
