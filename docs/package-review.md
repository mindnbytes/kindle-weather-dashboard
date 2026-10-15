# Windows package inspection — 2026-10-15

PC-only inspection; no package scripts executed on the Kindle and no device
files changed. This supplements the manifest in [jailbreak.md](jailbreak.md).
Device actions remain subject to an exact-action approval sheet.

## Firmware and inspection tool

KindleTool `kindletool-v1.6.5.251-mingw.zip` came from the Windows link in
[NiLuJe's snapshots](https://www.mobileread.com/forums/showthread.php?t=225030):
https://storage.gra.cloud.ovh.net/v1/AUTH_2ac4bfee353948ec8ea7fd1710574097/mr-public/KindleTool/kindletool-v1.6.5.251-mingw.zip

Its MD5 matched the maintainer listing, `8ad36a42edf6529e636171872f38aef2`.
Local SHA-256: `135ea2d3f12977021443b45226cf1fda7ab0ddf5154455e0964f203bb6640ff3`.
Ran `help`, then `convert -i` on the local packages (information only).
Header inspection is not independent cryptographic signature verification.

- 5.3.3: SP01, certificate number 2 / pubprodkey02.pem, FB03 Recovery V2,
  Yoshime/Yoshime3 platform, target OTA 1812030015. Device count is zero;
  the header does not explicitly enumerate PW1 variants. The original PW1
  downgrade procedure links these exact Amazon-hosted bytes by URL.
- 5.6.1.1: same platform and envelope type, target OTA 2689890035,
  six explicitly listed PW1 variants including PaperWhite WiFi.
- Hotfix 2.5.0: developer certificate, FC04 OTA V2, minimum OTA zero,
  maximum target revision, includes PaperWhite WiFi in its device list.
  These are targeting declarations, not runtime proof.

## Legacy jailbreak

Extracted only `JailBreak/kindle-5.4-jailbreak.zip` on the PC.
ZIP SHA-256: `f9d4414555b95f1714b874f95d4e9451e567c293749b71cc0f83761689ef93e0`.
All seven files go to the USB storage root only after the 5.3.3 checkpoint and
separate approval. Preserve the literal unusual BIN filename; never interpolate
it as shell code or rename it.

| Inner file | Bytes | SHA-256 |
| --- | ---: | --- |
| `Update_jb_$(cd mnt && cd us && sh jb.sh).bin` | 797 | `5a3e505e44d98fc747ae95a336b5a9b1216446664ddb0d3c62c43103026077ba` |
| `bridge.conf` | 8150 | `e48566698c5fc7c19466ed9c3861861a53aadfce813bcb811ba73a45ba6096f1` |
| `bridge.sh` | 27790 | `5142e32bfe8cf15c68689aa69034fdafa3b9519fbc32e2ee5eb4be01eec0c7b6` |
| `developer.keystore` | 40581 | `2ef661c8b263ed801789c60dd2e3462d7ad5e89861b068acf6c6b0ebd1c8119b` |
| `gandalf` | 59036 | `5ea53e29b772fe91224f02d565c040acf3c1096b5f428872edb93d7d8acd2417` |
| `jb.sh` | 15139 | `3b1518de76a81f9bc3f4c5c7e86f227e0664a05e14e31db4ba80bae1b03c3f6e` |
| `json_simple-1.1.jar` | 29036 | `6922499417065b2ae117570ff11424960bc764248d03f70eb4e2567cde51dfc4` |

## Hotfix effects requiring review

Extracted the actual pinned BIN with KindleTool and read its installer, hotfix
runner, helpers, startup configuration and job scripts. Also consulted
[tagged source](https://github.com/KindleModding/Hotfix/tree/2.5.0).

It replaces persistent `/var/local/kmc` and `/var/local/mkk`, installs a startup
job under `/etc/upstart/kmc.conf`, replaces the dispatch script
`/usr/bin/logThis.sh`, registers library handlers in appreg.db, and supplies
`documents/Run Hotfix.run_hotfix` and `/mnt/us/libkh/bin/fbink`.
It installs setuid Gandalf binaries and shell-file library integration.
Running the library action remounts root read-write, runs the bundled jobs,
remounts root read-only and restarts the GUI. Jobs restore update/Kindlet keys
and files, patch available debug-command configurations, and add flag files.
No independent power-management change was selected.

The README also advertises KPM, but the inspected KMC tar listing does not
establish a separate KPM installation; do not infer exact behavior from that
README alone. No uninstall procedure or full rollback has been established
for this bundle. A USB document backup cannot undo these system changes.

The installer targets PW1 and the helpers recognize model code 24. The October
B024 success report does not pin a hotfix hash; exact 2.5.0 runtime success on
this unit is unproven. Accepting the community-supported candidate requires
explicit review of these remaining compatibility and recovery limits.

## Launcher, MRPI, USBNetwork

Additional archives downloaded from the maintainer snapshot links on 2026-10-15.
Publisher checksum is N/A for these entries; local hashes pin downloaded bytes.
URL base: `https://storage.gra.cloud.ovh.net/v1/AUTH_2ac4bfee353948ec8ea7fd1710574097/mr-public/`.

| Relative source | Bytes | SHA-256 |
| --- | ---: | --- |
| `KUAL/kual-mrinstaller-1.7.N-r19303.tar.xz` | 1778608 | `36b3c28a44ad1a91609cc82d2bb9836ad6d7125ba1f63596307bf93f17a9255e` |
| `Touch/kindle-usbnet-0.22.N-r19297.tar.xz` | 46154104 | `cf971557d42cc0a6d7699f1c743108c681fa41e3d67ee5802a91932d130d4032` |
| `KUAL/KUAL-c6ac782-20250419.tar.xz` | 76676 | `8dace9db8ff7b7de80662a48e830296990e978efc71c281efde43b370bc7afe3` |
| `KUAL/KUAL-v2.7.37-gfcb45b5-20250419.tar.xz` | 224876 | `40c4b68712213adc7b667b9502cdd0c8099761fce1e1bf2b161b84102af54135` |

Proposed launcher selection: `KUAL-KDK-2.0.azw2` from the regular KUAL archive,
matching its README's PW1 instructions and report #41, after return to 5.6.1.1
and the hotfix action. Booklet/coplate is retained as an inspected candidate,
not an automatic fallback. Stop on a certificate error.

Selected inner KUAL file: 131070 bytes, SHA-256
`1d7cf02741be9e8f9c541af4eb5e1a97c00ab158819236749dba9250ad1fd4a9`.
Destination would be `documents/KUAL-KDK-2.0.azw2`.

MRPI has no README in this archive; read the maintainer thread installation,
usage and FAQ, archive listing, and relevant changelog entries. Its destination
is `extensions/MRInstaller` plus `mrpackages` at USB root. Its changelog includes
later root-remount handling fixes; early November 2014 warnings concern older
releases and are not proof that this pinned version fails on 5.6.1.1.

Selected SSH installer: `USBNetwork/Update_usbnet_0.22.N_install_touch_pw.bin`,
15337628 bytes, SHA-256
`a0c32074c79feabfbcef74a4d361e9e293400452124cd009cd5bae26e6e18538`.
Its metadata explicitly lists PaperWhite WiFi; do not use the pw2_and_up BIN.
Destination would be `mrpackages/`, installed alone through MRPI.

Read `README_FIRST.txt` and `README` in full, default config, KUAL menu and
SSH config, and relevant toggle/install script sections. The documented public
key location is `usbnet/etc/authorized_keys`. Proposed settings are
`USE_WIFI="true"`, `USE_WIFI_SSHD_ONLY="true"`, keeping `usbnet/auto` absent.
This permits manual SSH startup while retaining USB mass-storage mode.
Preserve LF line endings; back up installed configuration before editing.

The archive includes host private keys. Do not treat a matching bundled host
key as unique device identity. Before Wi-Fi access, finish reviewing host-key
provisioning and prepare unique keys plus a fingerprint verification procedure.
No host keys or client keys were generated or staged in this inspection.

## Remaining preparation

- Router is Speedport Smart 4 (owner confirmation). Owner saved enabled
  `Kindle-no-internet` port blocker, TCP and UDP `0-65535`, assigned only to
  the privately MAC-matched Kindle entry. No errors. Rule behavior and LAN
  peer access remain untested; Kindle stays in airplane mode.
- Finish host-key provisioning and exact configuration actions for SSH.
- Final action sheet must specify source hashes, exact copy/menu actions,
  expected results, wait guidance and stop rules. No firmware transfer,
  reboot, jailbreak or installation is approved by this review.

Router reference: [Telekom Speedport Smart 4 manual](https://www.telekom.de/hilfe/downloads/bedienungsanleitung-speedport-smart-4-typ-a.pdf),
page 92 onward, describes device-specific internet schedules. It does not by
itself establish an always-blocked rule or successful LAN access on this router.
Inspect the actual Internet filtering controls before choosing a rule; do not
enable Kindle Wi-Fi merely to populate the device list. Router firmware/version
and actual available controls are still unobserved.

Update: actual UI help confirmed port ranges including `0-65535`; owner confirmed
that the enabled device-specific rule saved successfully. See experiment log.
