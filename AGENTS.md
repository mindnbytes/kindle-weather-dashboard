Read `kindle-weather-dashboard.md` before working here. It defines device safety,
milestones, and review gates. Read `README.md` and `docs/experiments.md` for current
implementation and evidence. Use `nix develop` for development.

Current checkpoint: M0 preparation, M1 console access and M2 first PNG display
complete. Owner subsequently observed stock UI overwrite and touches navigating
the underlying UI; persistent dashboard mode is not established. M4 must address
screen ownership, touch handling and lock/suspend retention with separately
approved device commands. Do not assume locking immediately preserves the PNG.
Downgrade, jailbreak,
hotfix, return to 5.6.1.1, KUAL/MRPI and PW1 USBNetwork installation have passed
their recorded checkpoints. USB public-key SSH smoke check and teardown passed;
Wi-Fi public-key SSH from Windows now passes with USB unplugged, including
host-key verification and repeat connections. Owner reconfirmed Speedport's
Kindle-only internet blocker; a bounded IPv4 HTTP probe was refused while its
Windows control succeeded. Broader isolation coverage is unproven. Owner also
confirmed Mac Wi-Fi public-key SSH and all four shell checks. Owner confirmed
server stop/airplane-mode teardown for the earlier SSH session. A later approved
Mac SCP transfer, SHA-256 read-back and single FBInk 1.25.0 draw succeeded;
owner confirmed the physical image looked good and requested commit/pause.
This latest session's teardown is requested but not yet confirmed. On resume,
reconfirm device/network state. Next is M3 weather acquisition/cache/local HTTP
on Mac/Nix; no automation or power-management changes yet. M3 Mac pipeline now
implements API-shaped invented-fixture acquisition, normalization/cache, atomic
PNG publication and loopback-only-by-default HTTP. Owner chose invented data
for now; real location comes later through ignored local config. Read
docs/weather-pipeline.md. Real-location and Kindle LAN retrieval acceptance are
pending; do not infer full M3/deployment completion from local tests.
Offline WLAN uses the approved
WIFI_NO_NET_PROBE flag; temporary usbnet/verbose remains pending cleanup.
Keep the blocker enabled and use airplane mode when parked. Automatic SSH
startup is disabled. Device modification requires explicit approval of exact
commands; consult the action sheets and latest experiment entries. Renderer
development remains on Mac/Nix; do not regenerate it on Windows.
