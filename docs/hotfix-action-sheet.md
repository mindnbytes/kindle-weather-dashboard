# Universal hotfix 2.5.0 on jailbroken PW1 5.3.3

Prepared 2026-10-15. **Completed on 5.3.3:** owner confirmed successful package
installation, the runner's completion message, and a usable home screen after
the anticipated GUI-restart error dialog. Do not repeat this historical stage.
Owner confirmed
5.3.3 (1812030015) and the legacy JAILBREAK banner. Confirm usable normal UI
before proceeding. Keep airplane mode enabled throughout.

## Pinned file and effects

Source: https://github.com/KindleModding/Hotfix/releases/download/2.5.0/Update_hotfix_universal.bin

Local source: `C:\Users\Alexey\Documents\KindleSetup\2026-10-15\Update_hotfix_universal.bin`.
Size: 3743762 bytes. SHA-256:
`94d5c05254b70c4905392515411f620168ac238db62c7dcbc48a1e31d5de6c59`.
Matches the published GitHub asset digest and was rechecked after jailbreak.
Destination: `F:\Update_hotfix_universal.bin`, only if F: is still the Kindle.

This installs persistent system support, a startup job, MKK/Gandalf support,
shell-file library integration, the Run Hotfix action, and bundled FBInk.
The library action remounts root read-write, restores/patches support files,
returns root read-only and restarts the GUI. See the inspected package effects
in [package-review.md](package-review.md#hotfix-effects-requiring-review).
No independent power-management changes are proposed.

The package explicitly targets PW1, but the community report does not pin a
hash and exact 2.5.0 behavior on this unit is not proven. The tagged README
acknowledges incomplete testing. USB backup is not a complete rollback; no
tested uninstall/unbrick route for this unit is established. Approval must
include these system changes and residual compatibility/recovery limits.

## Exact sequence after approval

1. Confirm normal Kindle UI is usable and airplane mode remains enabled.
   Connect the working USB cable and identify the Kindle drive again.
2. Inspect its root for update BINs, remaining jailbreak payloads or an existing
   hotfix destination. Stop on leftover BINs or unexpected state; do not delete,
   overwrite, reinstall or reboot to make the check pass.
3. Recheck the source size/hash above. Copy once with:

   ```powershell
   Copy-Item -LiteralPath 'C:\Users\Alexey\Documents\KindleSetup\2026-10-15\Update_hotfix_universal.bin' -Destination 'F:\Update_hotfix_universal.bin' -ErrorAction Stop
   ```

4. Flush the destination file, then verify its byte count and SHA-256 against
   the manifest. On copy/read failure or mismatch, stop without retrying.
5. Safely eject the Kindle in Windows, then unplug USB.
6. On Kindle: Home → menu → Settings → menu → **Update Your Kindle**.
   Allow the package update and any automatic restart to complete undisturbed.
   Source provides no guaranteed duration. Report unexpected screens/errors;
   do not force a reboot or interrupt an installation.
7. Once normal UI returns without an error, find **Run Hotfix** in the library.
   Stop if it is missing. Tap it once. The inspected script displays progress,
   reports hotfix completion, and restarts the GUI. Record displayed errors
   or completion text; do not infer success from the action's presence alone.
8. Stop and report the update outcome, library action output and normal UI
   usability. Do not copy return firmware, install KUAL or enable Wi-Fi yet.

Grey update menu, disappearing BIN, error code, missing library action or
unexpected boot behavior are stop conditions, not reasons to substitute the
legacy hotfix or retry. If the runner displays an error, capture its exact text
for diagnosis before deciding whether any further interaction is appropriate.

Evidence: [B024 report #41](https://www.mobileread.com/forums/showthread.php?t=264432&page=3),
[tagged source](https://github.com/KindleModding/Hotfix/tree/2.5.0).
The report describes the universal hotfix on 5.3.3 followed by the library action,
then a later return to 5.6.1.1 and another hotfix action. Later stages are separate.

## Post-update action on confirmed 5.6.1.1 — completed

Owner approved this run. After resolving library visibility, owner reported
success, restart, no errors and normal home screen. Agent performed no hotfix
recopy or reinstall. Instructions below are retained as historical evidence,
not authorization to repeat the action.

Owner confirmed the return firmware **5.6.1.1 (2689890035)** with no errors.
The selected next action is the report's required post-update library run:

1. Keep airplane mode enabled and USB unplugged. Find the existing **Run Hotfix**
   library entry. Stop if missing; do not recopy or reinstall the BIN.
2. Tap **Run Hotfix once**. This reuses installed 2.5.0 system support and performs
   the previously reviewed root remount, support-file restoration and GUI restart.
3. Watch for **Hotfix Complete! Restarting GUI**. Let the GUI restart finish.
   If the same transient selected-application-could-not-be-started dialog appears
   during that restart, close it once and wait. Do not retry the library action.
4. Report completion text and normal UI usability. Stop for any different or
   recurring error, missing action or failed completion. No KUAL/USBNetwork or
   Wi-Fi actions included in this stage.

The exact selected package and its system effects are unchanged from the pinned
manifest; this run verifies post-update behavior rather than assuming survival.
