# PW1 offline Wi-Fi validation and SSH startup diagnosis

Prepared 2026-10-15. **Owner approved; both zero-byte flags created and verified.
Normal restart, stable Wi-Fi and manual SSH startup confirmed by owner;
Windows public-key Wi-Fi SSH independently passed with USB unplugged.**
Owner observed that dismissing the Wi-Fi error disconnects the Kindle, and KUAL
reports SSHD down in Wi-Fi-only mode. Saved router internet block must remain
enabled; do not reconnect the Kindle to unrestricted internet to bypass this.

## Exact compatibility evidence

Inspected the same pinned Amazon PW1 5.6.1.1 firmware used for the successful
return update, SHA-256
`6be62d30df26894b08083dbc55d23774756710c3a44c9a1d0075dd02d12090c9`.
KindleTool extracted the firmware privately on Windows. No payload scripts ran.
Scanning its decompressed rootfs found the wifid startup script:

```sh
# If the WIFI_NO_NET_PROBE flag file is present in the userstore,
# pass the '-n' option to wifid to disable network validation
# when connecting to an AP.
[ -e /mnt/us/WIFI_NO_NET_PROBE ] && PARAMS="$PARAMS -n" || true
```

Thus this feature is present in our exact PW1 build, not assumed from a PW2
guide. It is read at daemon startup, so a normal menu restart is part of the
proposed action. It suppresses Kindle's network validation; it does not block
internet, stop OTA itself, replace router policy, or prove isolation.

The selected USBNetwork README and KUAL implementation document `usbnet/verbose`
as a trigger for additional startup/log messages. This does not enable automatic
SSH startup. The status button only checks a PID file and is not process proof.

## Exact changes and manual sequence after approval

1. Owner turns airplane mode on and connects USB in mass-storage mode. SSH is
   reported down. Re-identify F: as Kindle and verify reviewed Wi-Fi config,
   key/auth hashes and absent usbnet/auto. Stop on unexpected state.
2. Inspect for existing `F:\WIFI_NO_NET_PROBE` and `F:\usbnet\verbose`; do not
   overwrite nonempty files or alter an existing directory.
3. Create only these two absent zero-byte files (no extensions), using
   `[IO.File]::Open(path, CreateNew, Write, None)`, flush and close. Verify both
   are ordinary zero-byte files. No root partition, key or config edit included.
4. Safely eject in Windows, then unplug USB. While airplane mode remains on,
   select **Settings → menu → Restart** once. This is a normal reviewed restart,
   not a power-button forced reboot or firmware update. Leave it undisturbed.
   Auto-start remains absent; SSH should not start at boot.
5. When the normal UI returns, confirm airplane mode. With the saved router
   block still enabled, turn airplane mode off and join the same protected WLAN.
   Check whether it now stays connected without the previous validation error.
   Report the actual LAN address. Do not toggle SSH if joining still fails.
6. If WLAN remains connected, open KUAL → USBNetwork → Toggle USBNetwork once,
   observe verbose messages and then USBNetwork Status. Report errors verbatim
   or confirm SSHD-up status. Do not toggle repeatedly.
7. Agent performs bounded port/host-key/public-key checks at the observed IP
   with USB unplugged, then read-only shell/network diagnosis. Stop on any new
   failure for review. No reinstall, password change or router unblock.

If normal Restart hangs or errors, stop and record the screen/elapsed time;
no forced recovery is included. If a file copy/write fails, stop without retry.
The two flags are reversible userstore changes: removal is a separately reviewed
teardown, and removing WIFI_NO_NET_PROBE requires daemon restart to re-enable
validation. Keep the flag for intended offline operation if the test succeeds;
remove verbose after diagnosis. Do not mark either outcome before observation.

Primary background sources:
[MobileRead offline Wi-Fi report](https://www.mobileread.com/forums/showthread.php?t=262385),
[Kindle Touch/Paperwhite wiki](https://wiki.mobileread.com/wiki/Kindle_Touch_Hacking#Disabling_Wifi_network_validation).
Compatibility decision above rests on the exact PW1 firmware bytes.
