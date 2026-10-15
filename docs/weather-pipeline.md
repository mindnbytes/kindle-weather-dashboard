# M3 Mac pipeline

Current workflow uses invented data. No Kindle connection is needed. Run from
the repository root; no packages beyond the existing Nix Python/Pillow shell.

```sh
nix develop -c python -m server.weather --fixture server/fixtures/open-meteo.json
nix develop -c python -m server.serve
```

In another terminal:

```sh
curl --fail http://127.0.0.1:8000/weather.png -o /tmp/kindle-served.png
shasum -a 256 runtime/weather.png /tmp/kindle-served.png
```

Stop the server with Ctrl-C. It serves only `/weather.png`, has no directory
listing, and binds to loopback by default. `/forecast.json` and all other paths
return 404. Missing image returns 503. Responses use `image/png` and `no-store`.
For a later reviewed LAN test, explicitly supply the Mac's current LAN address
with `--bind`; do not expose it through router forwarding. Kindle retrieval,
deployment, timers and power management have not been implemented or tested.

## Fixture contract

`server/fixtures/open-meteo.json` is an **invented API-shaped response**, based on
the [Open-Meteo forecast documentation](https://open-meteo.com/en/docs). It uses
the exact fields requested by the live fetcher: current temperature, apparent
temperature and WMO code; parallel hourly time/temperature/precipitation/code
arrays; daily min/max/code arrays. Metadata and units reflect the API shape.
Coordinates 0/0 are non-personal placeholders, not the future forecast location.

It is deliberately shortened to the minimum useful horizon (seven hourly rows
and four daily rows), with current conditions between hours at 23:30. It tests
selection across midnight, three future days, fog/drizzle/rain/snow/storm codes
and zero/negative temperatures. Tests additionally exercise a +02:00 offset,
missing/null values, unknown codes and insufficient horizons. The original
normalized `weather.json` remains the independent M2 renderer fixture.

Both fixture and live responses pass through the **same normalize/render/cache/
publish functions**. Fixture mode replaces only acquisition and the generation
clock (fixed at current.time + 15 minutes), and marks the image `SAMPLE DATA`.
It never invokes the HTTP fetcher. Output is repeatable in the pinned environment.
This is contract-based coverage, not a captured Hannover forecast or proof of
every possible provider response.

## Live mode later

Copy `config.example.json` to ignored `config.local.json`, set the location label
and explicit latitude/longitude, then run:

```sh
nix develop -c python -m server.weather --config config.local.json
```

This command makes one HTTPS Open-Meteo request with a 20-second socket timeout,
four forecast days, Celsius, `timezone=auto`, and `timeformat=unixtime`.
The free API requires no key for this workflow. No automatic polling is installed.
Location config and runtime files are ignored by Git. Exact future coordinates
are not stored in tracked files. Runtime and config are private local files,
not secrets served by the HTTP handler. Live images credit Open-Meteo.com.

The API's resolved fixed `utc_offset_seconds` controls displayed local time and
daily boundaries. This follows its response convention; DST transitions inside
the forecast range are not modeled. `Valid` means current conditions' valid
time, **not** the upstream model's update time. `Generated` means image creation.
The hourly strip starts at the first hour at/after current conditions; the current
precipitation probability comes from the containing hour. Daily rows start tomorrow.
Simple icons distinguish snow and storms; fog shares the cloud icon and drizzle
shares rain. Icons currently do not distinguish day from night.

## Cache and failure behavior

`runtime/forecast.json` caches the last validated normalized snapshot, and
`runtime/weather.png` is the last published image. Each file is replaced using
a same-directory temporary file plus atomic rename. They are not a two-file
transaction; only the PNG is served. Fetch, schema/value validation or rendering
failure returns nonzero and leaves both previous files intact. A file publication
error also returns nonzero; if cache replacement succeeded first, the cache may
be newer than the previous PNG. No partial PNG is published.

On an outage the server continues serving the last successful image with its
original timestamps; it does not relabel old data as fresh or redraw from cache.
If there has been no successful publication, the endpoint returns 503. Age printed
on the image is age **at generation** and cannot advance on a retained e-ink image.
There is no scheduler, retry loop, stale-data overlay or cache recovery command yet.

## Validation

```sh
nix develop -c python -m unittest discover -s tests -v
```

Tests cover deterministic original renderer and API-fixture CLI output, midnight
and offset handling, malformed/stale data, last-image retention on acquisition
failure, and real loopback HTTP byte equality/private-path rejection. A separate
live smoke request at non-personal 0/0 coordinates succeeded on 2026-10-15; its
temporary image was visually inspected. Normal development remains offline.
