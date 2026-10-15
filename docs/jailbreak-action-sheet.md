# Legacy jailbreak on confirmed PW1 5.3.3

Prepared 2026-10-15. **Owner approved; all seven files staged and verified.**
Owner confirmed the JAILBREAK banner; normal UI usability remains to be confirmed
before the hotfix stage. Owner confirmed 5.3.3
(1812030015) after the reviewed downgrade completed without reported errors.

## Exact payload and destinations

Use only `JailBreak/kindle-5.4-jailbreak.zip` from the pinned
`kindle-jailbreak-1.16.N-r19426.tar.xz`. Inner ZIP SHA-256:
`f9d4414555b95f1714b874f95d4e9451e567c293749b71cc0f83761689ef93e0`.

All seven files were extracted on Windows and their sizes/hashes matched
[the per-file manifest](package-review.md#legacy-jailbreak):

- `bridge.conf`
- `bridge.sh`
- `developer.keystore`
- `gandalf`
- `jb.sh`
- `json_simple-1.1.jar`
- `Update_jb_$(cd mnt && cd us && sh jb.sh).bin`

Destination: each file directly at the Kindle USB storage root, currently F:.
Preserve file bytes, names and LF endings. The unusual BIN name is intentional;
use literal paths, never evaluate its text as shell code. Do not copy the
outer archive, ZIP itself, bridge/hotfix installer BINs or uninstallers.

## Actions after approval

1. Keep airplane mode enabled. Connect the working data cable and confirm the
   Kindle returns to USB Drive Mode. Re-identify the actual drive; do not assume
   F: remains correct. Stop on any unexpected device state.
2. Inspect the root for an existing update BIN and any of the seven target names.
   Stop on any collision or leftover firmware; do not delete or overwrite it
   without separate diagnosis.
3. Reverify the pinned ZIP and all seven staged files against the manifest.
   Copy each file once to the confirmed root with `Copy-Item -LiteralPath`
   using the enumerated source file object's FullName and the confirmed root as
   destination. No shell invocation or filename interpretation is required.
4. Flush the destination files and compare each copied file's byte count and
   SHA-256 with the manifest. Stop on any mismatch or copy/read failure; no retry.
5. Safely eject through Windows, then unplug USB. Unlike the downgrade, this
   jailbreak stage must be unplugged before its menu action.
6. On Kindle: Home → menu → Settings → menu → **Update Your Kindle**.
   The maintainer says this is a fake update: after a few seconds,
   `**** JAILBREAK ****` should appear at the bottom of the screen.
   A full firmware installation is not the expected result.
7. Stop and report the banner and whether the normal UI remains usable. Do not
   reboot, install another package, enable Wi-Fi or run the hotfix yet.

Stop for a grey menu, disappearing file, missing banner, error or unexpected
screen. Do not infer success from copied files or improvise a reinstall/reset.
The package installs jailbreak support and bundles MKK; its README notes MKK
becomes active on the next boot. That does not authorize an extra reboot here.
This is a system modification; the USB backup is not a complete rollback image.

Source: [maintainer installation instructions](https://www.mobileread.com/forums/showthread.php?t=186645),
also read in full from the downloaded archive's README and README.txt.
