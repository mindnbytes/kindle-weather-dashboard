# Return jailbroken PW1 to 5.6.1.1

Prepared 2026-10-15. **Completed:** owner confirmed normal return without errors
and firmware 5.6.1.1 (2689890035). Retained as historical instructions, not
authorization to repeat the firmware update. Post-update Run Hotfix is pending.
Prerequisites observed: owner confirmed 5.3.3, legacy JAILBREAK banner, successful
universal hotfix 2.5.0 installation, its Run Hotfix completion message and usable
normal UI after the GUI restart. Keep airplane mode on throughout this stage.

## Pinned firmware

Source: https://s3.amazonaws.com/G7G_FirmwareUpdates_WebDownloads/update_kindle_5.6.1.1.bin

Local source: `C:\Users\Alexey\Documents\KindleSetup\2026-10-15\update_kindle_5.6.1.1.bin`.
Size: 217523739 bytes. SHA-256:
`6be62d30df26894b08083dbc55d23774756710c3a44c9a1d0075dd02d12090c9`.
Rechecked after the hotfix checkpoint. KindleTool header inspection explicitly
lists PaperWhite WiFi, Yoshime platform and target OTA **2689890035**.
Destination: `F:\update_kindle_5.6.1.1.bin`, if F: is still the Kindle.

This is a firmware write, with risk of boot failure if interrupted. Existing USB
backup is not a system recovery image and no tested unbrick procedure exists
for this unit. Prior checkpoints do not guarantee jailbreak persistence.

## Exact actions after approval

1. Confirm normal UI, airplane mode and sufficient battery charge; use the
   working data cable. If charge is low, recharge before staging. Connect USB
   and re-identify the Kindle drive.
2. Inspect the USB root for existing update BINs or an existing destination;
   stop on any collision. Do not delete, overwrite or retry automatically.
3. Recheck source size/hash above. Copy once:

   ```powershell
   Copy-Item -LiteralPath 'C:\Users\Alexey\Documents\KindleSetup\2026-10-15\update_kindle_5.6.1.1.bin' -Destination 'F:\update_kindle_5.6.1.1.bin' -ErrorAction Stop
   ```

4. Flush the destination, then verify its byte count and SHA-256. On failure,
   stop before ejecting or starting an update; no automatic retry.
5. Safely eject in Windows, then unplug USB. Unlike the earlier downgrade,
   this stage uses the normal manual firmware-update menu.
6. On Kindle: Home → menu → Settings → menu → **Update Your Kindle**.
   Allow the firmware update and automatic restart to finish undisturbed.
7. The community report says the first boot can remain on the tree screen for
   several minutes. No guaranteed duration is established; a slow screen does
   not authorize power interruption or a forced reboot. Report exact screen,
   elapsed time and any error before any further action. Do not repeat the
   report's improvised forced reboot.
8. Once normal UI returns, open Settings → menu → Device Info. Expected:
   **5.6.1.1 (2689890035)**. Confirm airplane mode is still enabled.
9. Stop and report firmware version and normal UI usability. Do not install
   KUAL, enable Wi-Fi or recopy the hotfix BIN. The next reviewed action will
   be running the existing Run Hotfix library entry after this checkpoint.

Stop for a grey update option, disappearing BIN, error, unexpected firmware or
boot behavior. No reset, replacement firmware or recovery attempt is included.

Evidence: [B024 report #41](https://www.mobileread.com/forums/showthread.php?t=264432&page=3)
and the already-inspected official package metadata. Hotfix persistence must
be checked after this update; do not assume the mere presence of library files
proves it survived.
