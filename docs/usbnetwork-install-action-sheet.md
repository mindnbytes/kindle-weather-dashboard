# Install PW1 USBNetwork through MRPI

Prepared 2026-10-15. **Completed:** owner reported success/no errors, MRPI log
confirmed the selected touch_pw installer and Success, and the USBNetwork log
ended Done. Automatic startup is absent; default Wi-Fi SSH settings remain off.
Historical instructions below do not authorize a repeat installation.
Owner confirmed KUAL and Helper → Install MR Packages on jailbroken PW1 firmware
5.6.1.1. Keep airplane mode enabled. This stage installs the package only; do
not toggle networking, enable automatic startup, change config or join Wi-Fi.

## Exact selected file and effects

Archive: `kindle-usbnet-0.22.N-r19297.tar.xz`, pinned source/hash in
[package-review.md](package-review.md#launcher-mrpi-usbnetwork).
Use only `USBNetwork/Update_usbnet_0.22.N_install_touch_pw.bin`.
Local source:
`C:\Users\Alexey\Documents\KindleSetup\2026-10-15\selected-payload-inspection\USBNetwork\Update_usbnet_0.22.N_install_touch_pw.bin`.

Size 15337628 bytes; SHA-256:
`a0c32074c79feabfbcef74a4d361e9e293400452124cd009cd5bae26e6e18538`.
Header explicitly lists PaperWhite WiFi. **Do not use pw2_and_up.**
Destination: `F:\mrpackages\Update_usbnet_0.22.N_install_touch_pw.bin`, if F:
is still the Kindle volume. Never put this installer in USB root.

The package installs tools/config under `usbnet`, a KUAL USBNetwork extension,
system symlinks and upstart jobs. MRPI remounts root during installation and
temporarily stops/restarts the Kindle UI. No separate power-management changes
are selected. Automatic SSH startup must remain disabled (`usbnet/auto` absent).
The default config does not allow Wi-Fi SSH; authentication and unique host-key
setup will be reviewed separately before any server start.

## Exact actions after approval

1. Connect USB and re-identify Kindle storage. Stop for an existing root BIN,
   nonempty mrpackages, existing usbnet or extensions/usbnet; do not overwrite
   or uninstall to make checks pass. Confirm copied MRPI exists.
2. Reverify selected source size/hash. Copy it once with `Copy-Item -LiteralPath`
   to the exact mrpackages destination above. Flush and compare destination
   byte count and SHA-256. Verify it is the only item in mrpackages.
3. Safely eject in Windows, then unplug USB. Keep airplane mode on.
4. Open KUAL → Helper → **Install MR Packages** once. Do not select any
   USBNetwork toggle. Let MRPI finish and return to normal UI undisturbed.
5. Report the displayed result and any errors. If it returns normally, reconnect
   USB so the agent can read and privately preserve installation logs:
   `extensions/MRInstaller/log/mrinstaller.log` and
   `usbnet/usbnetwork_install.log`.
6. Verify logs identify the selected touch_pw package and report success, with
   no script failure or root-remount failure. Check usbnet/etc/config and
   absent usbnet/auto. Merely seeing a new menu is not installation proof.
7. Stop at that checkpoint. Do not enable Wi-Fi, toggle USB networking/SSH,
   turn on automatic startup, change keys/config or reboot as troubleshooting.

Stop on failure/skip messages, unexpected restart, missing log, abnormal USB
behavior or unresponsive UI. No automatic reinstallation or uninstaller is
authorized. A matching uninstaller is in the original archive but would require
its own reviewed action; it removes package symlinks/jobs and the KUAL extension,
retaining userstore content unless the package's uninstall flag is selected.
No uninstall/recovery has been tested on this unit.

References: selected archive `README_FIRST.txt`, default config and installer;
[maintainer USBNetwork thread](https://www.mobileread.com/forums/showthread.php?t=186645),
[MRPI instructions](https://www.mobileread.com/forums/showthread.php?t=251143).
