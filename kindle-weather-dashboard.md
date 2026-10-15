# Kindle Paperwhite Weather Dashboard — Project Instructions

## Goal

Repurpose an old Amazon Kindle Paperwhite as an **offline-first, wall/fridge-mounted e-ink weather display**. Develop and test the weather image generator on a **Mac first**; later deploy it to a **NixOS mini home server**. The generator produces a weather report image; the Kindle retrieves it over local Wi-Fi, draws it on its screen, and ideally sleeps until the next refresh. Keep the implementation minimal, auditable, and easy to iterate with coding agents.

**First vertical slice (definition of done):** generate one PNG on the Mac → transfer it to Kindle → show it full-screen on e-ink. **Deployment later:** move the same tested renderer to the NixOS mini home server. Do **not** combine this milestone with power-management modifications.

## Known hardware (from device labels/settings, 2026-10-14)

| Item | Value |
| --- | --- |
| Device | **Kindle Paperwhite 1 (2012), Wi-Fi** |
| Evidence | Serial prefix **B024**; back model **EY21** |
| Firmware | **5.6.1.1 (2689890035)** |
| Display | 758 × 1024 pixels, grayscale, front-lit e-ink |
| Free user storage | ~1,109 MB at inspection |
| Connectivity | Micro-USB, Wi-Fi |
| Jailbreak status | **Completed with hotfix; returned to 5.6.1.1** |
| SSH access | **Windows USB/Wi-Fi verified; Mac Wi-Fi checks confirmed by owner** |

Do not store the complete serial number or MAC address in project files or logs. Reconfirm model and firmware before any modification.

## Constraints and non-goals

- **No firmware updates, factory reset, flashing, downgrade, or root-filesystem changes without explicit human review.** Jailbreak/downgrade can brick the device; success reports are not guarantees.
- Preserve stock firmware and recovery options. Make a backup of accessible user files before starting.
- Keep the Kindle's software as small as possible; develop weather API access, layout, fonts, and PNG rendering on the Mac, then deploy them to the NixOS mini home server.
- **Local network only** for the first version: no public endpoints, cloud dependencies on Kindle, telemetry, or third-party services on the device. The NixOS home server may retrieve forecast data from a selected public weather API.
- Use SSH public keys; do not expose SSH to the internet. After jailbreak/hotfix and return to 5.6.1.1, prefer Wi-Fi SSH on a trusted LAN with Kindle internet access blocked before connection. Keep USB mass-storage access for preparation/recovery and USB SSH as an optional fallback. Device setup uses Windows; renderer development remains on Mac/Nix. See [the access plan](docs/jailbreak.md).
- Avoid permanently charging an old lithium battery unattended; inspect battery health, swelling, and runtime. Use a safe mount/holder rather than attaching magnets directly to the device.
- Out of scope: Amazon Kindle library, DRM, KOReader, full Linux distribution replacement, interactive GUI, custom PCB.

## Design

```text
Open-Meteo (or another weather source)
                |
                v
 Mac during development / NixOS mini after deployment:
          fetch -> normalize -> render 758x1024 PNG
                |
        local HTTP (eventually)
                |
                v
 Kindle: wake -> Wi-Fi -> GET image -> FBInk -> suspend
                |
          e-ink retains image
```

**Initial transfer:** prefer manual SCP over verified Wi-Fi SSH, directly from the Mac or from Windows. USB-network SSH/SCP is a fallback. Do not require HTTP, automated fetching, or a wake scheduler for milestone 1. Later, prefer **Kindle-pull over HTTP** rather than server-initiated SCP, because the Kindle may be asleep between updates.

**Rendering:** [FBInk](https://github.com/NiLuJe/FBInk) writes PNG images directly to the Kindle framebuffer. Use a **device-compatible** build and verify its flags with `fbink --help`. The upstream documented form is `fbink -i /path/to/image.png`; rendering, rotation, screen clearing, and refresh behavior must be tested on this PW1.

**Image:** start with a static 758x1024 grayscale PNG (high contrast, large typography). Verify orientation and actual image dimensions after testing. A full refresh may be needed to prevent ghosting.

**Development (Mac first):** choose the smallest useful portable implementation (e.g., Python + Pillow + standard HTTP server). Keep weather acquisition separate from the renderer so a fixture JSON can be rendered without internet access. Include generation timestamp and age of forecast in the layout. Use a local Python virtual environment or an existing Nix development workflow if convenient; do not require NixOS to run or test the project. Confirm that any fonts used can also be installed on NixOS, or bundle appropriately licensed project fonts.

**Deployment (NixOS mini, later):** reuse the same generator and tests; only the packaging, service configuration, and runtime paths should change. Integrate with the existing NixOS configuration rather than introducing a flake by default. For unattended operation, prefer a declarative NixOS `systemd` service/timer and a LAN-only HTTP endpoint. Keep service accounts, dependencies, ports, and firewall configuration explicit and minimal.

## Milestones and review gates

### M0 — Confirm device and prepare safely

- [x] Reconfirm PW1 / B024 / EY21 and firmware 5.6.1.1.
- [x] Enable airplane mode until a deliberate networking decision; review OTA precautions. Retain protected-LAN policy and airplane mode when parked.
- [x] Back up user-visible storage over USB (797 files, SHA-256 verified; owner spot-check passed).
- [x] Check battery condition and charge reliability (owner reported fully charged and no visible concerns; long-term runtime unmeasured).
- [x] Read the exact PW1 firmware-specific jailbreak instructions **in full** and verify download provenance/checksums where available.
- [x] Produce a risk/rollback report, and **stop for human approval** before firmware changes (recorded action sheets and stepwise approvals).

### M1 — Obtain console access (human-approved device modification)

- [x] Select and validate a **PW1 5.6.1.1-specific** jailbreak path; do not substitute PW2 instructions.
- [x] Only after approval, execute the documented steps one at a time; record actual outcomes.
- [x] Install suitable KUAL/MRPI/USBNetwork components if required by the chosen method.
- [x] After jailbreak/hotfix and return to 5.6.1.1, configure public-key Wi-Fi SSH; demonstrate Windows and Mac access with USB unplugged. Router blocker confirmed before joining; subsequent bounded IPv4 HTTP probe refused while Windows control succeeded. Broader isolation remains unproven. USB SSH and mass-storage restoration also passed.
- [x] Demonstrate `uname -a`, `id`, `mount`, `df -h` from shell. Avoid writing to root filesystem during checks.
- [x] Back up device-specific configuration before changing it (private verified backups recorded).

**Important:** There is a community-reported route for **PW1 B024 on 5.6.1.1** involving a temporary downgrade to 5.3.3, legacy jailbreak, a compatible hotfix, then return to 5.6.1.1. A report from October 2026 documents differences from older instructions. Treat this as a **research lead, not a preauthorized procedure**. Verify current package compatibility and each step with the owner before execution:

- [MobileRead forum, PW1 downgrade thread, page 3](https://www.mobileread.com/forums/showthread.php?t=264432&page=3) — see posts #39 and #41.
- [MobileRead USBNetwork wiki](https://wiki.mobileread.com/wiki/USBNetwork)
- [KindleModding Hotfix releases](https://github.com/KindleModding/Hotfix/releases)

### M2 — First end-to-end PNG (core MVP)

- [x] Produce `weather.png` on the Mac from **static fixture data**, with no API requirement.
- [x] Verify `file weather.png` and dimensions 758x1024.
- [x] Install/test a compatible FBInk binary without altering system partitions unnecessarily (existing hotfix-supplied FBInk 1.25.0 used).
- [x] Copy PNG to the Kindle's user storage (`/mnt/us/weather-m2.png`), verify SHA-256 read-back.
- [x] Render on the Kindle; owner reports perfect appearance. Stock UI later overwrites it and touch still operates the underlying UI; elapsed time unmeasured. Persistent display is a later acceptance gate.
- [x] Document the successful manual redraw command in `docs/first-image-action-sheet.md`; repeated execution not yet tested.

**Illustrative commands only; do not run before SSH/FBInk verification:**

```sh
# On Mac, after Wi-Fi SSH verification; replace KINDLE_LAN_IP with the observed address
scp weather.png root@KINDLE_LAN_IP:/mnt/us/weather.png

# On Kindle (once a compatible FBInk binary is installed)
fbink -i /mnt/us/weather.png
```

### M3 — Weather data and server

- [ ] Fetch forecast on the Mac during development; later on the NixOS home server (candidate: [Open-Meteo](https://open-meteo.com/)). Set location explicitly in config; do not hardcode API credentials.
- [ ] Cache last known forecast. Define failure behavior for API/network outages.
- [ ] Render: current temperature, feels-like or precipitation, hourly trend, next 1–3 days, last-updated timestamp.
- [ ] Export a grayscale PNG, atomically replacing the served file (`tmp` + rename).
- [ ] Serve locally from the Mac during development and test retrieval independently. Later move the endpoint to the NixOS mini and verify Kindle connectivity before changing the Kindle URL.
- [ ] Only for deployment, integrate with existing NixOS configuration; use a dedicated `systemd` service/timer rather than cron if scheduling on the server. Bind only to the appropriate LAN address, and open only the required firewall port (if any).

### M4 — Unattended periodic refresh

- [ ] Resolve screen ownership and touch handling: owner observed stock UI returning and touches operating through the PNG. Review a reversible PW1-compatible approach, including a clear exit/recovery path; device commands require separate approval.
- [ ] Test whether normal lock/suspend preserves the dashboard or replaces it. Do not assume immediate locking solves UI overwrite. Dashboard must remain visible and accidental touches must not navigate the stock UI during unattended use.
- [ ] Verify whether the PW1 firmware and hardware can perform **RTC wake from suspend** reliably; do not assume another Kindle model's approach applies.
- [ ] Investigate stock power manager/screensaver and what overwrites the framebuffer on lock/suspend.
- [ ] Test manual sleep → wake → fetch → render first; then automate.
- [ ] Turn Wi-Fi on only during retrieval if practical.
- [ ] Start with 60-minute updates, adjust based on observed battery consumption.
- [ ] Ensure updates are idempotent, time-bounded, and recover from Wi-Fi/API/server failure; preserve the last successful image on error.
- [ ] Record measured battery life and behavior across several days before mounting it permanently.

### M5 — Mounting and polish (optional)

- [ ] Design a removable magnetic holder / frame, not magnets glued to device electronics.
- [ ] Confirm readable contrast, viewing angle, and charging access.
- [ ] Optional: richer weather icons, alerts, calendar, indoor sensor data, configurable themes.

## Suggested repository structure

```text
kindle-weather/
├── AGENTS.md                # instructions for coding agents (can point here)
├── README.md                # setup and progress
├── docs/
│   ├── device.md            # verified device details (no full identifiers)
│   ├── jailbreak.md         # researched, reviewed steps; no auto-execution
│   └── experiments.md       # dated observations and commands/results
├── nix/                     # later: NixOS module/service definitions
├── server/
│   ├── render.py            # fixture/forecast -> grayscale PNG
│   ├── weather.py           # weather source adapter
│   └── fixtures/            # deterministic mock JSON
├── kindle/
│   ├── display.sh           # draw locally available image
│   └── refresh.sh           # later: fetch/display cycle
└── tests/
```

## Agent working agreement

1. **Inspect before editing.** Read this file, the current README, and prior experiment notes. State assumptions and the precise next milestone.
2. **Small, reviewable iterations.** One milestone or experiment per change. Favor simple shell/Python over new frameworks.
3. **No unilateral device modification.** Do not trigger firmware updates, downgrades, jailbreaks, partition remounts, factory reset, persistent daemon installation, or power-management changes without explicit user approval of exact commands.
4. **Verify compatibility.** All Kindle commands, package binaries, and jailbreak instructions must be checked for **PW1/B024/5.6.1.1**, not generic Kindle or PW2.
5. **Offline-test first.** Server rendering uses fixed fixture data and unit/smoke tests; don't require a connected Kindle for ordinary development.
6. **Report evidence, not assumptions.** Record successful/failed commands, versions, screen behavior, connectivity, power draw when measured, and recovery options. Never assert that a step worked without output or confirmation.
7. **Stop on unexpected behavior.** Preserve diagnostic output and ask before attempting retries that may alter firmware.
8. **Security and privacy.** No credentials, complete serial/MAC, or personal geolocation in git. Keep the Kindle on trusted LAN; avoid unnecessary egress.
9. **Finish with next steps.** After each iteration, summarize changes, tests, open risks, and the single next recommended action.

## First task to give an agent

> Read this project brief. Do **not** modify the Kindle. Set up the repository and implement milestone M2's **Mac-side half only**: generate a deterministic 758x1024 grayscale `weather.png` using fixture weather data, provide a minimal CLI and a smoke test, and document how to inspect the file. Run and test it on macOS with a documented minimal setup. No weather API, HTTP server, SSH, jailbreak, NixOS deployment, or automation yet. Keep dependencies minimal. Stop for review when the PNG is ready.

## Reference links

- [PW1 downgrade / jailbreak discussion](https://www.mobileread.com/forums/showthread.php?t=264432&page=3)
- [USBNetwork](https://wiki.mobileread.com/wiki/USBNetwork)
- [FBInk repository](https://github.com/NiLuJe/FBInk)
- [FBInk CLI reference](https://github.com/NiLuJe/FBInk/blob/master/CLI.md)
- [Open-Meteo](https://open-meteo.com/)

*Status, 2026-10-15: owner-approved Windows setup has completed downgrade to
5.3.3, legacy jailbreak, universal hotfix 2.5.0, return to 5.6.1.1, post-update
hotfix, KUAL/MRPI and PW1 USBNetwork installation. USB public-key SSH and read-only
shell checks passed; USB mass storage and Windows adapter settings were restored.
Windows Wi-Fi public-key SSH also passed with USB unplugged; a bounded IPv4
egress probe was refused while the Windows control succeeded. Owner confirmed
Mac Wi-Fi public-key SSH and shell checks. Broader isolation remains unverified.
Owner confirmed server stop/airplane-mode teardown
and requested a pause. Subsequently, owner approved Mac PNG transfer and a
single FBInk draw; SHA-256 read-back matched and owner accepted the physical
image. M2's first end-to-end display is complete. Latest session teardown is
requested but not yet confirmed; next is M3 on Mac/Nix. Consult
docs/experiments.md for evidence; pending steps still
require their review gates. Mac-side fixture renderer checks passed previously.*
