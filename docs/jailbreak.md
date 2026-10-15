# PW1 jailbreak and first display — review draft

**Current checkpoint, 2026-10-15:** owner-approved device work has passed the
downgrade, jailbreak banner, hotfix, return to 5.6.1.1, post-update hotfix,
KUAL/MRPI and USBNetwork installer/log checks. SSH is not yet verified. Owner
requested a USB SSH check before the pending Wi-Fi configuration. Airplane mode
remains on. The original research status and unchecked planning list below are
historical; use the latest experiment entries and stage action sheets for actual
outcomes. Do not treat this checkpoint as approval of pending modifications.

Researched: **2026-10-15**. Status: **planning only; not ready for execution**.
No device was accessed, no installation packages were downloaded, and no device
steps below were performed. This document is not approval to execute them.

**Preparation update, 2026-10-15:** owner reconfirmed identifiers/firmware,
airplane mode and battery condition. Windows USB storage backup completed and
all 797 files passed SHA-256 comparison; owner checked representative files.
See `docs/experiments.md`. Initial candidate packages have now been downloaded
to a private PC-only setup folder (not the Kindle); pinned details follow.
The original status above describes the research draft. Device modification
remains unapproved; compatibility and final action-sheet review are pending.

Target from the project brief: Paperwhite 1 (2012), Wi-Fi, serial prefix B024,
back model EY21, firmware 5.6.1.1 (2689890035). These are prior observations;
reconfirm them at M0. Never record complete serial numbers or MAC addresses here.

**Setup machine: Windows.** Perform package preparation, USB backup, firmware
transfer, and initial Wi-Fi SSH verification from that machine. Record its Windows
version/build before setup. The renderer stays on the Mac/Nix development workflow;
verify Wi-Fi SSH from the Mac too, allowing direct PNG transfers for M2. USB
mass-storage access remains available for preparation and configuration recovery.

**Procedure takes precedence:** follow the selected, reviewed jailbreak and
hotfix instructions exactly, including their airplane-mode requirements. Wi-Fi
SSH setup begins only after all required jailbreak, hotfix, firmware-return and
post-update steps are complete and those instructions permit networking. If they
require airplane mode longer, keep it enabled longer; the preferred SSH path is
not a reason to change the jailbreak sequence.

## Proposed route and evidence

Candidate sequence:

```text
M0: identify, isolate, back up, check battery, verify artifacts, review risk
  -> approval of the exact device steps
M1: 5.6.1.1 -> 5.3.3 -> legacy K5 jailbreak -> compatible hotfix
  -> 5.6.1.1 -> re-run hotfix -> launcher/MRPI -> USBNetwork
  -> configure keys + LAN isolation -> Wi-Fi SSH from Windows and Mac
M2: compatible FBInk -> transfer existing PNG -> manual display -> review
```

This is a community-supported candidate, not a tested procedure for our unit.
The original author describes a PW1 boot-time downgrade using Amazon's 5.3.3
package: keep USB connected, copy to the storage root, wait at least two minutes,
then restart using the power button while connected. This differs from a normal
menu update. The thread title's PW2 speculation is not applicable evidence.
[Original downgrade procedure](https://www.mobileread.com/forums/showthread.php?t=264432).

The March 2024 report (#39) uses an older hotfix and includes a factory reset.
The October 4, 2026 report (#41) specifically identifies B024/5.6.1.1, reports
success with the universal hotfix on 5.3.3, returns to 5.6.1.1, re-runs the hotfix,
then starts Kindlet KUAL. It reports the legacy hotfix failing. A subsequent
reply recommends booklet KUAL instead. These reports leave a launcher choice;
they do not justify mixing packages or retrying failed updates blindly.
[Reports #39–42](https://www.mobileread.com/forums/showthread.php?t=264432&page=3).

The legacy jailbreak maintainer documents support through 5.4.4.2, not direct
installation on 5.6.1.1. On a supported firmware, extract the contents of the
inner `kindle-5.4-jailbreak.zip` to the USB storage root, eject/unplug, and use
Settings → menu → Update Your Kindle. The expected indication is a JAILBREAK
banner, rather than a normal firmware update. Jailbreak maintenance must precede
a subsequent official update; custom packages on 5.6.x generally require MRPI.
[Maintainer instructions](https://www.mobileread.com/forums/showthread.php?t=186645).

The Hotfix repository's current default branch describes a broader toolkit and
explicitly notes incomplete compatibility testing. Do not assume that branch,
the newest release, and the package used in report #41 are equivalent. Release
2.5.0 is listed, but the report does not pin its asset hash. Exact release and
5.3.3/PW1 compatibility still need review.
[Repository](https://github.com/KindleModding/Hotfix),
[release 2.5.0](https://github.com/KindleModding/Hotfix/releases/tag/2.5.0).

## M0 — preparation and approval packet

All boxes remain pending. The renderer being finished does not complete M0.

- [ ] Owner reconfirms the target identifiers and exact firmware in Settings.
- [ ] Owner enables airplane mode through jailbreak, hotfix, and return to
  5.6.1.1. Use manual USB firmware transfer; do not reconnect to Amazon for an
  update. Enable Wi-Fi only at the deliberate LAN setup stage below.
- [ ] Inspect for swelling, unusual heating, unreliable charging, or USB faults.
  Stop if present. Arrange a charged battery and reliable cable before flashing;
  check package-specific charge requirements rather than inventing a threshold.
- [ ] Copy all accessible USB user storage, including hidden files, to a private
  Windows backup outside Git. Record date, file count/size, and backup location in a
  private note; compare the copy and open representative backed-up files.
- [ ] Inspect visible storage for existing jailbreak/launcher files and stray
  update packages. Record findings before deciding whether a fresh jailbreak is
  needed. Do not delete existing files or reset the device as preparation.
- [ ] Prepare the artifact manifest below. Read each selected archive's README
  and installation/uninstall instructions in full on Windows. Record exact inner
  filenames, target models/firmwares, and every destination.
  Use an archive tool that supports `.tar.xz` and the inner ZIP (for example,
  7-Zip); preserve file contents and line endings. In File Explorer, show hidden
  files and filename extensions. Identify the Kindle's actual drive letter;
  “USB root” means that drive's top level, not its `documents` folder.
- [ ] Resolve the universal-hotfix version and launcher choice. Document whether
  the hotfix includes other components or changes update behavior.
- [ ] Read the selected USBNetwork README for Wi-Fi SSH enablement, key paths,
  server startup and how to keep USB mass-storage access available. Verify whether
  configuration and public keys can be staged through mass storage/KUAL before
  the first connection. Exact configuration values are still pending inspection.
- [ ] Prepare a trusted LAN that allows Windows/Mac to reach the Kindle while
  blocking the Kindle's internet access before its first Wi-Fi connection.
  Record and verify the router/firewall rule; do not assume the hotfix blocks OTA.
  Confirm the Wi-Fi network supports local peer access and the Kindle can join it.
- [ ] Check availability of a Windows SSH client and transfer tool. Prefer the
  Windows OpenSSH Client if available; only the client is needed on the PC.
  PuTTY/WinSCP are alternatives if selected and reviewed. Do not enable a Windows
  SSH server for this procedure.
- [ ] Complete a final action sheet: one action per row, exact source hash,
  destination/menu action, expected screen result, wait guidance, and stop rule.
- [ ] Owner reviews that action sheet and the recovery limits below, then
  explicitly approves the selected device modifications. No blanket approval
  for retries, substitutions, resets, or recovery flashing.

### Artifact manifest to complete before approval

These are candidates identified in source listings, not downloaded or validated
payloads. The snapshots listing is rolling; pin exact bytes before proceeding.
[Maintainer snapshots](https://www.mobileread.com/forums/showthread.php?t=225030).

| Purpose | Candidate | Outstanding verification |
| --- | --- | --- |
| Downgrade | PW1 Amazon `update_kindle_5.3.3.bin`, linked by original procedure | Final Amazon URL, availability, model metadata, size/hash |
| Return firmware | PW1 Amazon `update_kindle_5.6.1.1.bin` | Official provenance, availability, model metadata, size/hash |
| Legacy jailbreak | `kindle-jailbreak-1.16.N-r19426.tar.xz` in current snapshot listing | Differs from r19326 in older report; inspect README and inner ZIP |
| Hotfix | `Update_hotfix_universal.bin` from a pinned KindleModding release | Select release; validate PW1/5.3.3 and post-upgrade instructions |
| Launcher | KUAL; reported archive `KUAL-v2.7.37-gfcb45b5-20250419.tar.xz` | Choose Kindlet/booklet; validate firmware, certificate and installation needs |
| Installer | `kual-mrinstaller-1.7.N-r19303.tar.xz` | Inspect layout and installation instructions |
| SSH over Wi-Fi (USB fallback) | K5 `kindle-usbnet-0.22.N-r19297.tar.xz` | Select exact PW1 inner installer; read Wi-Fi config, keys, startup, USB modes and uninstall route |
| Display, M2 | FBInk Kindle build | Pin compatible PW1 ABI/build, image support and CLI flags |

For each downloaded archive and selected inner payload, record filename, exact
source URL, release/revision, byte count, retrieval date, local SHA-256, and any
publisher checksum/signature plus verification result. Several snapshot entries
list checksum `N/A`; a self-computed hash pins bytes but does not establish
authenticity. Missing provenance or compatibility remains a stop condition.
Do not use firmware mirrors merely to fill an unavailable official download.

### PC-only downloads verified 2026-10-15

Downloaded directly over HTTPS from the following sources; nothing copied to
the Kindle. Local SHA-256 pins bytes but is not independent publisher verification
unless explicitly stated below. Firmware model metadata still needs inspection.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `update_kindle_5.3.3.bin` | 171618740 | `bc1a869f0cd9cf33caa75b4b7434c1b08a875bdf1f6fb2692e6323fc0a7453d0` |
| `update_kindle_5.6.1.1.bin` | 217523739 | `6be62d30df26894b08083dbc55d23774756710c3a44c9a1d0075dd02d12090c9` |
| `kindle-jailbreak-1.16.N-r19426.tar.xz` | 1056936 | `7bad4e414fbe1b9a2bc3fd23b4dcb88fa625ddd506942c472efcb114f1428f68` |
| `Update_hotfix_universal.bin` (2.5.0) | 3743762 | `94d5c05254b70c4905392515411f620168ac238db62c7dcbc48a1e31d5de6c59` |

Exact sources:

- https://s3.amazonaws.com/G7G_FirmwareUpdates_WebDownloads/update_kindle_5.3.3.bin
- https://s3.amazonaws.com/G7G_FirmwareUpdates_WebDownloads/update_kindle_5.6.1.1.bin
- https://storage.gra.cloud.ovh.net/v1/AUTH_2ac4bfee353948ec8ea7fd1710574097/mr-public/Touch/kindle-jailbreak-1.16.N-r19426.tar.xz
- https://github.com/KindleModding/Hotfix/releases/download/2.5.0/Update_hotfix_universal.bin

Hotfix digest matched the GitHub release asset API's published SHA-256. The
2.5.0 README explicitly includes sh_integration and KPM and acknowledges incomplete
compatibility testing. Download does not resolve PW1/5.3.3 compatibility or approve
those additional changes. Source/install behavior and launcher selection remain
under review.

Read the legacy archive's `README.txt`, `README`, and `OLD_README` in full.
The current instructions identify PW1 and firmware 5.0.x–5.4.4.2, and select
the contents of `kindle-5.4-jailbreak.zip`. Archive listing confirms that inner
ZIP exists; extraction, inner-payload hashes and destination review remain pending.
No historical README recovery/retry action is authorized by this inspection.

Windows build reported by the registry: 26300.9550, DisplayVersion 26H2.
Registry ProductName says Windows 10 Education; marketing version not independently
confirmed. Windows OpenSSH `ssh.exe` and `scp.exe`, and Windows `tar.exe`, are available.

For the later verification step, PowerShell can compute a hash without executing
the payload (replace the illustrative path with the selected local file):

```powershell
Get-FileHash -LiteralPath 'C:\KindleSetup\packages\update_kindle_5.3.3.bin' -Algorithm SHA256
```

Use Windows safe removal where the selected package instructions call for
ejecting/unplugging. The boot-time downgrade's instruction to remain connected
is a distinct stage; do not apply the jailbreak's eject/unplug sequence to it.

## M1 — staged device actions, after separate approval

The following defines order and checkpoints. It is not yet the final action
sheet: package selection and inspection above must supply the missing specifics.

| Stage | Proposed action | Evidence required before advancing |
| --- | --- | --- |
| 1 | Apply the original PW1 5.3.3 boot-time downgrade with the approved payload and USB sequence | Device boots normally; Settings explicitly reports 5.3.3 |
| 2 | Apply the legacy jailbreak on 5.3.3 using the maintainer procedure above | Observe and record the success banner; normal UI remains usable |
| 3 | Install the reviewed universal hotfix and run its library action as prescribed by that release | Record installation result and library action output; missing action is a stop |
| 4 | Manually update to the approved PW1 5.6.1.1 package | Normal boot; Settings reports expected firmware; retain airplane mode |
| 5 | Re-run the selected hotfix as its instructions require | Explicit successful result, not just presence of files |
| 6 | Install selected launcher and MRPI | Launcher opens and installer is available; stop on certificate errors |
| 7 | Install only the PW1 USBNetwork payload through MRPI | Installer log indicates success; review configuration before enabling SSH |
| 8 | Back up SSH configuration; stage public keys and enable Wi-Fi SSH using reviewed package instructions | Exact config/key paths verified; manual startup selected; USB mass-storage recovery understood |
| 9 | Verify LAN isolation, then enable Kindle Wi-Fi and start SSH manually | Kindle internet blocked; actual LAN address found in router/device information |
| 10 | Connect over Wi-Fi from Windows, then the Mac | Host key verified; intended public-key authentication succeeds from each client |
| 11 | Collect shell evidence below, then back up relevant configuration privately | Commands succeed over Wi-Fi; repeat connection works with USB unplugged |

No factory reset is proposed. No forced-reboot recovery sequence is proposed:
report #41's account of a hung boot is an incident, not a recovery instruction.
Agree on source-supported wait guidance before the update; a slow or unexpected
screen is a reason to pause for diagnosis, not to improvise power interruption.

MRPI normally places `extensions/MRInstaller` and `mrpackages` at the USB root;
its KUAL Helper action installs packages from `mrpackages`. Keep only the single
reviewed custom installer there for each stage; official firmware follows its
separate procedure. Capture the installer log after every package.
[MRPI maintainer instructions](https://www.mobileread.com/forums/showthread.php?t=251143).

### Wi-Fi SSH plan and acceptance

Despite its name, USBNetwork provides Wi-Fi SSH as well as USB SSH. The wiki
describes enabling Wi-Fi access through the package configuration (normally
`/mnt/us/usbnet/etc/config`) or KUAL. This supports the proposed route, but exact
flags and key locations must come from the selected archive's README.
[USBNetwork wiki](https://wiki.mobileread.com/wiki/USBNetwork).

1. While airplane mode is still on, back up the installed configuration through
   USB mass storage. Stage only client public keys in the documented location;
   private keys remain on Windows/Mac. Enable Wi-Fi access and retain manual
   startup using the documented settings. If this requires a shell first, stop
   and review a minimal USB SSH bootstrap rather than guessing configuration.
2. Confirm the prepared LAN blocks Kindle internet access and allows connections
   from both clients. Then turn off airplane mode, join that network, discover
   the Kindle's actual LAN IP, and start SSH through the documented local action.
   No port forwarding or internet exposure is proposed.
3. Verify the host key using a trusted local/package-supported method and connect
   from Windows using public-key authentication. Verify a connection from the
   Mac against the same host key. Review algorithm errors per host; do not weaken
   global SSH settings or rely on guessed/default passwords.
4. Run the read-only acceptance commands below. Unplug USB and repeat a connection
   and small file transfer to confirm independence from USB networking. A DHCP
   reservation may be considered later; record the observed address for now.
5. Keep automatic SSH startup disabled for this first test. Document how to stop
   the server and return to airplane mode. Keep USB mass-storage recovery
   available; USB networking is an optional fallback, not an M1 prerequisite.

### Optional Windows USB SSH fallback

Use this only if the Wi-Fi setup needs a reviewed bootstrap or LAN diagnosis
cannot resolve the problem. Windows USB network drivers are not required to pass
the preferred Wi-Fi access milestone.

The wiki's Windows procedure identifies an RNDIS/Ethernet Gadget adapter and uses
Kindle `192.168.15.244`, host `192.168.15.201`, and mask `255.255.255.0`. Treat
these as candidates; verify the selected package configuration first. The wiki
is older guidance, not evidence that this Windows machine will recognize it.
[USBNetwork wiki](https://wiki.mobileread.com/wiki/USBNetwork).

If the USB fallback is selected, the planned Windows sequence is:

1. Toggle USB networking as prescribed by that package. Confirm the device in
   Device Manager and identify its adapter in Control Panel → Network and Sharing
   Center → Change adapter settings. Do not change the PC's normal LAN adapter.
2. If the Kindle appears as an unknown USB device or no adapter appears, stop
   and record its status. Resolve driver compatibility/provenance separately;
   do not install an arbitrary RNDIS driver or disable driver-signature checks.
3. Record the USB adapter's original IPv4 settings. If confirmed appropriate,
   set only that adapter to `192.168.15.201`, mask `255.255.255.0`, with no default
   gateway or DNS. Check for an existing subnet conflict first. Leave Internet
   Connection Sharing and network bridging off.
4. Connect to the configured Kindle address with the selected SSH client, after
   reviewing host-key verification and authentication setup below. Diagnose
   connection failures without disabling the Windows firewall globally.
5. At the end, use the package's documented method to restore mass-storage mode
   and restore the recorded adapter settings if changed.

Windows OpenSSH availability depends on the Windows version and installed
optional features; check the PC rather than assuming it is installed.
[Microsoft OpenSSH overview](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh-overview).

### Shell evidence

After a successful Wi-Fi SSH connection, proposed read-only shell evidence is:

```sh
uname -a
id
mount
df -h
```

Store redacted outcomes in `docs/experiments.md`. Keep complete logs/backups
outside Git if they contain identifiers or private data. Shell access does not
prove display compatibility. No root remount or framebuffer write is part of
this acceptance check.

## Risks, recovery limits, and stop rules

| Risk or failure | Planned response |
| --- | --- |
| Wrong image/model or interrupted flashing | Prevent through identification, artifact review, stable power; no guaranteed software recovery is established |
| Backup mistaken for recovery image | USB backup restores accessible documents only; it excludes system partitions, bootloader and device-specific recovery data |
| Grey update menu, disappearing BIN, error code, missing success banner | Record stage, screen/error and selected hash; stop before another copy/install/reboot attempt |
| Boot does not reach normal UI | Preserve observed timing and screen state; seek PW1-specific recovery advice before reset, serial work or flashing |
| Hotfix/jailbreak does not survive update | Stop at that checkpoint; do not install more packages to test guesses |
| Wi-Fi SSH fails | Check LAN peer access, actual IP, server state and authentication separately; retain USB mass-storage recovery and review any USB SSH fallback before using it |
| Windows USB fallback fails | Stop at device/adapter diagnosis; review driver requirements separately; USB driver setup is not a prerequisite for working Wi-Fi SSH |
| Want to return to stock | Plan separately using exact package uninstall instructions and current firmware state; no reset/firmware-reinstall guarantee is established |

A normal return to 5.6.1.1 is part of the candidate route; it is **not** a proven
unbrick or complete jailbreak removal procedure. Rescue packages, serial-console
work, opening the device, and system partition changes require a separate plan
and approval. There is no tested recovery path for this individual device yet.

## M2 — handoff once M1 passes

The Mac renderer and PNG checks are already complete. After M1, transfer
`weather.png` directly from the Mac to the Kindle over the verified Wi-Fi SSH
connection. Windows OpenSSH `scp` or reviewed WinSCP settings are alternatives;
if staging the PNG on Windows, compare its SHA-256 with the Mac original first.
Select and verify
a PW1-compatible FBInk build, keep it in user storage where supported, and inspect
its help before preparing the exact transfer/redraw commands. Current OpenSSH
SCP may require compatibility handling with an old server; resolve based on its
actual error, not global client changes. Test image orientation, margins, contrast,
ghosting and stock UI overwrite manually, recording outcomes.
[FBInk CLI reference](https://github.com/NiLuJe/FBInk/blob/master/CLI.md).

Stop after one reliable manual display. M3 data/HTTP service, M4 sleep/wake and
scheduling, and M5 mounting remain separate milestones.

**Next recommended step:** see [the package inspection](package-review.md).
Owner observations and private USB backup have passed. Complete Speedport Smart 4
internet-blocking preparation, unique SSH host-key planning, and the exact action
sheet before requesting device execution approval. M0 and M1 are not yet complete.
