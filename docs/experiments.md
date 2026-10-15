# Experiments

## 2026-10-15 — Owner pauses before Wi-Fi connection

Owner requested saving work and pausing. Wi-Fi SSH configuration is applied and
verified, but radio/server were not started. Keep airplane mode on and automatic
SSH startup disabled. USB mass storage remains the last verified device mode.
No Wi-Fi SSH success or traffic-isolation result is claimed.

Resume by reconfirming Speedport rule Kindle-no-internet is enabled, TCP/UDP
0–65535, and assigned only to the privately MAC-matched Kindle entry. Then review
the deliberate Wi-Fi connection/manual SSH startup and isolation verification
steps before enabling the radio. Preserve existing working keys and private
known-hosts evidence. Windows and Mac Wi-Fi SSH checks remain outstanding.

## 2026-10-15 — Wi-Fi SSH config applied; radio/server still off

Owner requested resuming Wi-Fi SSH setup. Confirmed all five USB-stage file
hashes still matched the successful baseline and auto-start was absent. Prepared
Wi-Fi config differed only in USE_WIFI and USE_WIFI_SSHD_ONLY. After command
approval, privately backed up/hash-verified the working USB-only config, copied
the Wi-Fi config once, flushed and verified size/SHA-256
`3635b0c931450239dd57bacc2dd8fa36ddef298c8d6ead727f265d89caa26c67`.
All four key/auth files remained unchanged. Current flags USE_WIFI=true,
USE_WIFI_SSHD_ONLY=true, USE_OPENSSH=true; auto-start absent. Finished 12:29:44 UTC
(14:29:44 Europe/Berlin). No radio enable, server start or mode toggle triggered.

Windows Wi-Fi LAN address observed as 192.168.2.70/24. Saved Speedport Kindle-only
blocker must be reconfirmed before deliberate networking; traffic isolation,
Wi-Fi host-key/auth checks and Mac access remain pending. Airplane mode stays on.

## 2026-10-15 — USB SSH teardown verified

Owner restored the adapter settings, toggled USBNetwork off and reported USB
Drive Mode. Read-only verification confirmed F: as Kindle/FAT32, no present
VID_0525/PID_A4A2 networking gadget, recorded USB interface DHCP enabled and
static DNS empty. Device config remains USE_WIFI=false, USE_WIFI_SSHD_ONLY=false,
USE_OPENSSH=true; usbnet/auto is absent. The successful SSH session had already
exited normally. USB test and teardown are complete.

Unique host key, public authorized key and USB-only OpenSSH config remain as the
reviewed baseline. No Wi-Fi configuration applied or access tested. Next milestone:
review the two remaining Wi-Fi config flags and controlled network-isolation
verification, then verify Wi-Fi SSH from Windows and Mac. Physical PNG display
remains pending. Logs, keys and backups remain outside Git.

## 2026-10-15 — USB public-key SSH smoke check passed

Owner configured only Ethernet 2 IPv4 manually after the non-admin command was
denied. Verified 192.168.15.201/24 in Preferred state, no default USB gateway,
and no IPv4 DNS servers. Kindle TCP port 22 at 192.168.15.244 was reachable.
Scanned its Ed25519 host key and compared the complete public-key bytes with
the independently generated host public key: exact match. Only after this match,
saved a dedicated private known_hosts file on Windows.

Windows OpenSSH connected with explicit id_ed25519 identity, strict host-key
checking, dedicated known_hosts, BatchMode and password/keyboard-interactive
authentication disabled. Client log explicitly confirmed publickey authentication.
Remote command chain `uname -a && id && mount && df -h` exited zero, uid=0(root)
confirmed, kernel Linux 2.6.31-rt11-lab126. Complete shell output and client log
are saved privately outside Git, without copying any client private key.
Finished at 12:18:49 UTC (14:18:49 Europe/Berlin); SSH session exited normally.

USB SSH smoke test passed. Teardown remains pending: restore original Windows
USB adapter DHCP/DNS configuration, unplug, toggle USBNetwork off on Kindle,
reconnect and confirm USB mass storage returns. Wi-Fi access, network isolation,
Mac SSH and physical PNG display remain unverified. Airplane mode stays on.

## 2026-10-15 — RNDIS adapter working; IPv4 change needs Windows administrator

Owner reported successful driver installation. Verified correlated gadget is
USB Ethernet/RNDIS Gadget, Net class, Status OK, problem code zero, Acer provider,
oem10.inf and USB_RNDIS service. Matching network adapter is Ethernet 2, index 49,
Status Up. Privately saved original adapter/IP/DNS/routes and device association.
Original IPv4 was DHCP enabled with APIPA 169.254/16 and no default route;
original DNS configuration is retained in the private baseline.

Rechecked no conflicting non-default route on another interface. Attempt to set
DHCP disabled on only index 49 failed immediately with Windows "Access is denied"
despite host sandbox approval. No subsequent New-NetIPAddress or DNS command ran;
no successful adapter configuration or port/SSH test is claimed. Owner needs
administrator-authorized IPv4 configuration on this adapter. Normal Wi-Fi/LAN
settings remain unchanged, and Kindle airplane mode remains required.

## 2026-10-15 — Matching signed RNDIS package prepared

Inbox rndiscmp.inf selection was rejected by Windows; user's subsequent model
picker remained limited to serial drivers. Researched a specific alternative
from Microsoft Update Catalog matching USB\VID_0525&PID_A4A2, including AMD64.
Downloaded/extracted only the reviewed Acer INF/catalog package from Microsoft's
download host. Catalog signature is Valid; SignTool confirmed the exact INF's
catalog membership under kernel signing policy, zero warnings/errors. Required
inbox binaries exist. Full provenance and hashes are in
[Windows driver review](windows-rndis-driver-review.md).

No driver installation has been performed by the agent. Proposed next action
is user-operated Update driver → Browse folder on the correlated COM3 gadget,
allowing Windows to evaluate the exact hardware match rather than forcing an
unrelated inbox serial/network model. Runtime result remains pending.

## 2026-10-15 — Kindle gadget serial binding confirmed

On reconnect, exactly one correlated VID_0525/PID_A4A2 gadget appeared as USB
Serial Device (COM3), Ports class, Status OK. Hardware revision 0325; compatible
IDs advertise USB Class_02/SubClass_02/Prot_FF. Driver binding is Microsoft's
usbser.inf, service usbser, version 10.0.26100.9278, problem code zero.
No Ethernet adapter is created, so USB SSH cannot be attempted yet.

Read installed Microsoft netrndis.inf and rndiscmp.inf. The latter supplies the
Remote NDIS Compatible Device model (Net class, version 10.0.26100.1). Consulted
Microsoft's RNDIS documentation and MobileRead's Windows USBNetwork guidance.
The generic RNDIS INF does not automatically match the reported compatible IDs;
this is not proof of successful runtime compatibility. A specific built-in
driver selection must be reviewed, with no downloads, signature bypass or
changes to unrelated devices. No driver or adapter settings changed yet.

## 2026-10-15 — USB serial device correlated with Kindle cable

After owner unplugged only the Kindle USB cable, present-device inspection
found zero VID_0525/PID_A4A2 devices and zero COM3 devices. This disappearance
correlates the observed COM3 gadget with the Kindle connection. No USB network
device was present. No mode toggle, driver change, network setting or SSH
attempt performed. Next: reconnect without toggling and inspect compatible IDs
and current driver binding before proposing a specific driver correction.

## 2026-10-15 — USB networking attempt: Windows driver diagnosis

Owner performed the reviewed USBNetwork toggle and reconnected USB, reporting
no Kindle errors. Read-only Windows inspection found F: no longer available,
but no new network adapter or USB network-class PnP device. Present-device
inspection found `USB Serial Device (COM3)`, hardware VID_0525/PID_A4A2,
Ports class, Status OK, problem code zero. This suggests a USB gadget associated
with a serial driver, but Kindle association still requires unplug/replug
correlation; do not identify it conclusively from VID/PID alone.

No Windows adapter IP, driver, firewall or network-sharing setting changed.
No SSH connection attempted. Stop at device/driver diagnosis per action sheet;
no arbitrary driver or device removal is authorized. Airplane mode remains on.

## 2026-10-15 — Approved USB-only SSH configuration applied

Owner explicitly approved the USB SSH action sheet. Reconfirmed Kindle/FAT32
on F:, unchanged original config hashes against the private backup, absent
authorized_keys/unique-host-key destinations and absent auto-start file.
Rechecked all five prepared source files against the private inventory, then
copied/flushed and SHA-256/size verified every destination in usbnet/etc.
No client private key was copied. Config now has KINDLE_IP=192.168.15.244,
USE_WIFI=false, USE_WIFI_SSHD_ONLY=false, USE_OPENSSH=true; usbnet/auto is absent.
Finished at 11:55:11 UTC (13:55:11 Europe/Berlin).

No SSH server start or USB-mode switch triggered by the agent. Next owner action:
safe eject/unplug, KUAL USBNetwork toggle once, reconnect USB. Adapter recognition,
Windows USB IPv4 configuration and SSH authentication remain untested.

## 2026-10-15 — Owner requests USB SSH before Wi-Fi setup

Saved completed milestones in commit 322ae96 and pending Wi-Fi SSH configuration
in 0fcc75b, leaving a clean checkpoint before USB-test preparation. Owner requests
a USB-only SSH smoke check first; pending Wi-Fi files were not staged.

Read-only preflight found no Windows non-default IPv4 route matching the candidate
192.168.15.244 address and no Kindle USB Ethernet adapter while still in mass
storage. Installed USBNetwork flags remain false; no authorized_keys, unique
selected server-key destination or auto-start file present. Prepared a separate
PC-only config keeping both Wi-Fi flags false and selecting OpenSSH, plus a
private five-file source inventory using the existing prepared key-only setup.
No device config writes, USB-mode switch or server startup yet. See
[USB SSH action sheet](usb-ssh-action-sheet.md) for exact proposed test/teardown.

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
