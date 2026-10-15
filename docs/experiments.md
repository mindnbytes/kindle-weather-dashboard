# Experiments

## 2026-10-15 — USBNetwork installation verified; SSH files prepared on PC

Owner reported MRPI success, UI restart and no errors. Read-only USB inspection
confirmed MRPI processed the selected touch_pw installer and logged `Success! :)`;
USBNetwork's own installer log ended `Done!`. USBNetwork KUAL menu is present,
mrpackages is empty, and usbnet/auto is absent. Installed default settings are
USE_WIFI=false, USE_WIFI_SSHD_ONLY=false, USE_OPENSSH=false. No server startup
or Wi-Fi connection has been performed. Log timestamps show March 2015; device
clock is inaccurate and those timestamps are not treated as execution dates.

Privately copied and hash-verified both logs plus original config and sshd_config
to the PC setup directory outside Git. Inspected only Windows public-key files
and fingerprints; the default id_ed25519 public key is available with a private
counterpart. No client private-key contents read or copied.

Prepared LF-only config/sshd_config/authorized_keys privately on Windows and
generated a unique Ed25519 Kindle host key in a new private ssh-prep directory.
Only the existing Windows client public key is selected; Mac authorization will
be added later from its public key. Host fingerprint is retained privately for
the first connection. No prepared files staged to the Kindle yet. Next step is
separate review of the USB-only SSH configuration action sheet.

## 2026-10-15 — Approved PW1 USBNetwork installer staged

Owner approved the USBNetwork installation action sheet. Preflight confirmed
Kindle/FAT32 on F:, installed MRPI, empty mrpackages, no root update BINs, and
no existing usbnet or extensions/usbnet. Copied only the selected
`Update_usbnet_0.22.N_install_touch_pw.bin` once into mrpackages, flushed it and
verified 15337628 bytes and SHA-256
`a0c32074c79feabfbcef74a4d361e9e293400452124cd009cd5bae26e6e18538`.
It was the only directory entry in mrpackages. Finished at 11:36:15 UTC
(13:36:15 Europe/Berlin). No installation, server start or networking toggle
triggered by the agent. MRPI outcome and installation logs remain pending.

## 2026-10-15 — KUAL and MRPI menu confirmed

After safe-eject/unplug and opening KUAL, owner confirmed Helper → Install MR
Packages is present. Launcher/MRPI menu checkpoint passed. No package installation
or SSH startup is implied by the menu check. Reverified the selected PW1
USBNetwork payload size/hash and reviewed MRPI log path and USBNetwork installer
startup effects for the next separate action sheet.

## 2026-10-15 — Approved KUAL and MRPI copied and verified

Owner approved the launcher/MRPI action sheet. Preflight confirmed F: as
Kindle/FAT32, no root update BINs and no selected destination collisions.
Reverified the pinned MRPI archive and KUAL file. Validated archive paths and
member types (regular files/directories only), then extracted MRPI on Windows.
Copied KUAL-KDK-2.0.azw2 to documents and the selected MRInstaller tree to
extensions/MRInstaller, and created empty mrpackages. Existing unrelated files
were preserved. KUAL plus all nine MRPI files were flushed and verified by byte
count and SHA-256; mrpackages remained empty. Private per-file source inventory
is retained beside the PC extraction. Finished 11:32:08 UTC (13:32:08 Europe/Berlin).

No launcher or installer executed by the agent. Owner's next step is eject,
unplug and open KUAL once, then confirm Helper → Install MR Packages is present
without selecting it. KUAL launch/menu result remains pending. No USBNetwork
installer staged and no Wi-Fi connection performed.

## 2026-10-15 — Post-update hotfix success reported

After the library-visibility diagnosis and instructions to check All Items and
search Hotfix, owner reported success, restart, no errors, and normal home screen.
This passes the owner-reported post-update hotfix/UI checkpoint on 5.6.1.1.
No hotfix recopy or reinstall was performed by the agent during diagnosis, and
owner did not report reinstalling it. No claim of SSH access or display rendering.

Rechecked the pinned KUAL and MRPI archive hashes and selected KUAL-KDK-2.0.azw2
size/hash on Windows. Prepared their separate action sheet; no launcher or MRPI
files copied yet. Airplane mode remains required.

## 2026-10-15 — Post-update hotfix entry missing: read-only diagnosis

Owner approved the post-update runner action but then reported no Run Hotfix
entry visible in the library; no successful post-update run is claimed.
Stopped before any recopy/reinstall. Read-only USB inspection confirmed F: is
the Kindle and `documents/Run Hotfix.run_hotfix` still exists. Root has no update
BINs; `mkk` exists and `kmc` does not exist in USB storage. Those user-storage
directory observations do not establish the state of `/var/local` system support.

The KindleModding FAQ recommends reinstalling the hotfix after a firmware update:
https://kindlemodding.org/jailbreaking/jailbreak-faq.html
This supports reviewing a pinned hotfix reinstall if UI filtering/indexing
checks do not resolve visibility; it does not authorize retries, reset or
re-jailbreaking. Next read-only owner check: library filters and Hotfix search
after safe eject/unplug. No device files changed during diagnosis.

## 2026-10-15 — Return to 5.6.1.1 confirmed

Owner reported normal return with no errors and Device Info firmware
**5.6.1.1 (2689890035)**. Return-update checkpoint passed. No forced reboot or
recovery action reported. The post-update Run Hotfix action remains pending;
do not infer jailbreak persistence solely from a successful stock firmware boot.
Airplane mode remains required. No KUAL/USBNetwork installation or Wi-Fi test yet.

## 2026-10-15 — Approved return firmware staged

Owner explicitly approved the separate return-to-5.6.1.1 action sheet.
Preflight confirmed F: as Kindle/FAT32, no existing root update BINs, sufficient
storage and the existing Run Hotfix library entry file. Copied the pinned Amazon
return firmware once to USB root, flushed it, and verified 217523739 bytes and
SHA-256 `6be62d30df26894b08083dbc55d23774756710c3a44c9a1d0075dd02d12090c9`.
Verification finished at 11:12:26 UTC (13:12:26 Europe/Berlin).

No firmware installation triggered by the agent. Owner's next steps are safe
eject/unplug and the normal Update Your Kindle menu action, then report version
and usable UI. Return update and post-update hotfix remain unconfirmed. Airplane
mode remains required; no forced reboot or recovery attempt is authorized.

## 2026-10-15 — Hotfix completion and normal UI confirmed

Owner confirmed both seeing "Hotfix Complete! Restarting GUI" before the
restart and a usable home screen after the transient application-error dialog.
The observed sequence matches the inspected runner's documented GUI restart
behavior. The universal-hotfix installation and library-action checkpoints pass
on 5.3.3; persistence through the return update remains untested.

Rechecked the pinned Amazon 5.6.1.1 firmware locally: 217523739 bytes, SHA-256
`6be62d30df26894b08083dbc55d23774756710c3a44c9a1d0075dd02d12090c9`.
Prepared a separate return-update action sheet. No return firmware copied to
the Kindle yet; airplane mode remains required.

## 2026-10-15 — Hotfix installation and runner observations

Owner confirmed the universal hotfix package update succeeded and returned to
the normal screen with no errors (clarified a typing ambiguity). Then, after
instructions to tap Run Hotfix once, owner reported that it went well but after
the restart displayed: "Application Error The selected application could not be
started. Please try again."

The previously inspected 2.5.0 `hotfix.sh` restarts lab126_gui and explicitly
displays guidance that an error dialog is expected during that transition,
instructing the user to close it and keep waiting. This is a possible match,
not independent proof that every hotfix job succeeded. Owner advised to close
the dialog once and wait, without retrying the application. Explicit completion
text, recovered UI usability and absence of recurring errors remain to be
confirmed. No return firmware staged; airplane mode remains required.

## 2026-10-15 — Approved universal hotfix staged

Owner explicitly approved the hotfix action sheet and requested continuation.
Preflight found F: as Kindle/FAT32, no remaining legacy jailbreak payloads or
update BINs, and no existing Run Hotfix action file. Copied the pinned universal
hotfix 2.5.0 once to USB root, flushed it, and verified destination size 3743762
bytes and SHA-256
`94d5c05254b70c4905392515411f620168ac238db62c7dcbc48a1e31d5de6c59`.
Verification completed at 10:59:53 UTC (12:59:53 Europe/Berlin).

No installation or library action triggered by the agent. Owner must eject,
unplug, install through Update Your Kindle, and report the result before the
Run Hotfix action. Package-install outcome and UI usability remain unconfirmed;
approval alone was not counted as observation of UI usability. Airplane mode
remains required.

## 2026-10-15 — Legacy jailbreak banner confirmed

After the approved eject/unplug and menu-update step, owner explicitly confirmed
`**** JAILBREAK ****` appeared. This satisfies the legacy jailbreak banner
checkpoint on confirmed PW1 5.3.3. Normal UI usability still needs confirmation
before the next installation. No hotfix or later package installed yet.
Airplane mode remains required. Prepared [hotfix action sheet](hotfix-action-sheet.md)
for separate owner review; pinned local hotfix size/hash rechecked successfully.

## 2026-10-15 — Approved legacy jailbreak files staged

Owner explicitly approved the separate legacy jailbreak action sheet. Host-level
preflight confirmed F: as Kindle/FAT32, with no existing root update BINs or
target-name collisions. The earlier sandbox temporary extraction was unavailable
to the host; before any device write, re-extracted the pinned inner ZIP to a new
private Documents/KindleSetup subfolder and checked all seven manifest hashes.

Copied each approved file once with literal paths to the Kindle USB root, flushed
each destination, and verified byte count and SHA-256 against the reviewed
manifest. All seven passed at 10:55:16 UTC (12:55:16 Europe/Berlin).
No installer, shell script or restart was triggered by the agent. Owner's next
action is Windows safe eject, unplug, Settings → menu → Update Your Kindle;
the JAILBREAK banner and usable UI remain unconfirmed. Wi-Fi stays off.

## 2026-10-15 — Downgrade confirmed by owner

Owner observed the software-update screen, no errors, an automatic restart,
and return to USB Drive Mode. After instructions to safely eject/unplug and
inspect Device Info, owner reported **5.3.3 (1812030015)**. This matches the
pinned downgrade target. First downgrade checkpoint passed; no jailbreak or
hotfix success is implied. Airplane mode remains the required state.

Prepared the seven files from the pinned inner jailbreak ZIP in a fresh private
Windows temporary folder. ZIP and all extracted file hashes match the recorded
manifest. No jailbreak files copied to the Kindle at this preparation step.
See [the next action sheet](jailbreak-action-sheet.md).

## 2026-10-15 — First downgrade payload staged and verified

Following owner review and instruction to move on, owner reconfirmed USB Drive
Mode and a full/nearly full battery. Read-only preflight confirmed F: is the
Kindle FAT32 volume with no existing root-level update BIN; source firmware size
and SHA-256 matched the action sheet. Sandbox initially reported F: unavailable;
an approved host-level read confirmed it was mounted. No device retry was involved.

Copied the pinned `update_kindle_5.3.3.bin` once to the USB root, flushed the
destination file, and read it back for SHA-256 verification. Destination size
171618740 bytes and hash
`bc1a869f0cd9cf33caa75b4b7434c1b08a875bdf1f6fb2692e6323fc0a7453d0`
matched. Verification finished at 10:38:25 UTC (12:38:25 Europe/Berlin).
The connected wait was timed; at 10:40:36 UTC, more than two minutes had elapsed
since verification, and the owner was instructed to perform the reviewed restart.
No restart initiated by the agent. Firmware remains unconfirmed until owner
performs the reviewed restart and reports Device Info. Wi-Fi remains off;
network isolation behavior has not yet been tested.

## 2026-10-15 — Speedport Kindle internet rule configured

Owner located the Kindle's already-registered router entry by privately matching
its MAC address. No full MAC recorded. Speedport Smart 4 time rules offered daily
or weekday schedules but no Never option. Used Port blocking instead. Its help
explicitly accepts ports 0–65535 and hyphenated ranges.

Owner confirmed saving enabled rule `Kindle-no-internet`, TCP `0-65535`, UDP
`0-65535`, assigned only to the matched Kindle entry, with no errors. Kindle
remains in airplane mode. This is configuration evidence only: WAN blocking,
IPv4/IPv6 coverage, persistence and LAN peer access have not been tested. No
device firmware or files changed. Verify network behavior before accepting M1
Wi-Fi access; do not equate a saved rule with measured isolation.

Owner reviewed the proposed downgrade action sheet and recovery limits and
responded "everything looks good to me", requesting a commit. No downgrade
commands or device actions were executed. Remaining preparation checks are
unchanged; this review does not establish network isolation or complete M0/M1.

## 2026-10-15 — PC-only package compatibility inspection

Downloaded and inspected the selected firmware, legacy jailbreak, universal
hotfix 2.5.0, KUAL candidates, MRPI and USBNetwork archives on Windows.
[Package review](package-review.md) records source URLs, hashes, inner payloads,
metadata, system changes, proposed selections and remaining limitations.
KindleTool's archive MD5 matched the maintainer listing; its read-only header
inspection identified Yoshime firmware and explicit PW1 targeting in the return
firmware, hotfix and selected touch_pw USBNetwork installer. Package scripts were
read as text, never executed. No files were copied to the Kindle.

Owner identified the router as Speedport Smart 4. Internet blocking is not yet
configured or verified. The USBNetwork archive includes host private keys, so
unique host-key provisioning must be reviewed before enabling Wi-Fi SSH.
No device-modification approval requested or granted in this preparation step.

## 2026-10-15 — M0 identification and Windows USB backup

Owner reconfirmed B024 / EY21 and firmware 5.6.1.1 (2689890035), enabled
airplane mode, and reported a fully charged battery with no visible concerns.
The first USB cable did not expose storage; another cable worked. Windows
identified drive F: as Kindle, FAT32, with a Healthy volume status.

Copied accessible storage, including hidden/system files, to a new private
Documents/KindleBackups folder outside Git using Robocopy with `/E /COPY:DAT
/DCOPY:DAT /XJ /R:0 /W:0`. Exit code 1 indicated successful copying: 248
directories and 797 files, with zero failures. Subsequent recursive SHA-256
comparison verified all 797 files (289,726,327 bytes); source and backup file
counts matched. Copy log and verification summary are stored beside the private
backup. No source files were modified. Owner subsequently opened representative
backed-up files and confirmed they looked good.

Top-level inspection found no obvious jailbreak/launcher files or update BINs;
this does not establish whether the device has previously been jailbroken.
No firmware changes or package installations performed. Package selection,
compatibility review, and exact-action approval remain pending.

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
