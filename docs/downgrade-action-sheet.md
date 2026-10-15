# First device stage: PW1 5.6.1.1 to 5.3.3

Prepared 2026-10-15. **Completed:** owner reported 5.3.3 (1812030015) after the
approved copy, connected wait and manual restart, with no reported errors.
See `experiments.md` for observed results. The instructions below are retained
as the historical action sheet, not authorization to repeat the downgrade.
This sheet defines the first
modification only, followed by a mandatory checkpoint. Later jailbreak, hotfix,
return firmware and SSH stages require their own reviewed actions. Outstanding
M0 preparation in `jailbreak.md` must be resolved before executing this sheet.

## Risk and recovery review

The community reports success on B024/5.6.1.1, but that does not guarantee success
on this unit. Interrupted or incompatible flashing can leave the device unable
to boot. There is no tested unbrick procedure for this unit. The verified USB
backup protects accessible documents, not system partitions or the bootloader.
Returning to 5.6.1.1 is a later planned update, not a guaranteed recovery method.
No reset, retry, recovery flashing or package substitution is included.

## Pinned payload

Source: https://s3.amazonaws.com/G7G_FirmwareUpdates_WebDownloads/update_kindle_5.3.3.bin

Local source:
`C:\Users\Alexey\Documents\KindleSetup\2026-10-15\update_kindle_5.3.3.bin`

Size: 171618740 bytes. SHA-256:
`bc1a869f0cd9cf33caa75b4b7434c1b08a875bdf1f6fb2692e6323fc0a7453d0`.

Destination: `F:\update_kindle_5.3.3.bin` (only if F: is still the Kindle).
The metadata identifies the Yoshime platform; the original PW1 downgrade
procedure supplies model-specific supporting evidence. It is not a PW2 image.

## Ordered actions after explicit approval

| Step | Exact action | Expected result / stop rule |
| --- | --- | --- |
| 1 | Confirm B024/EY21, firmware 5.6.1.1, airplane mode on, battery still fully charged or recharge before staging; use the working data cable directly to Windows. | Stop for any changed identifier, battery concern or unstable USB connection. |
| 2 | Confirm F: is the Kindle volume and inspect its root for existing BIN files. Recheck source size and SHA-256 above. | Stop if F: is absent/wrong, any update BIN is already present, or source hash/size differs. Do not delete existing files to make this check pass. |
| 3 | Run `Copy-Item -LiteralPath 'C:\Users\Alexey\Documents\KindleSetup\2026-10-15\update_kindle_5.3.3.bin' -Destination 'F:\update_kindle_5.3.3.bin' -ErrorAction Stop` once. | Only the pinned downgrade BIN is staged. Stop for any copy error; do not retry automatically. |
| 4 | Run `Get-FileHash -LiteralPath 'F:\update_kindle_5.3.3.bin' -Algorithm SHA256`; verify byte count and exact hash above. | Stop on mismatch or read error. Do not reboot with an unverified copy. |
| 5 | After copying and checking finish, wait at least two full minutes. Keep USB connected; do not eject. | This wait and connected restart are from the original procedure, not the later jailbreak instructions. |
| 6 | Owner holds the Kindle power button until it restarts, with USB still connected. The original report describes an orange LED blink and screen lighting. Release once it restarts. | This initiates the downgrade. Do not use Update Your Kindle for this stage. |
| 7 | Leave USB and power undisturbed while installation runs. | Source provides no guaranteed duration. Report an error or unexpected screen; a diagnostic pause never authorizes a power interruption, forced reboot, reset or retry. |
| 8 | Once the normal UI returns, disconnect USB as the original procedure permits, then open Settings → Device Info. Confirm exactly 5.3.3 and airplane mode on. | Stop here and report firmware plus screen outcome. Do not copy jailbreak files yet. |

Sources read:
[original PW1 boot-time procedure](https://www.mobileread.com/forums/showthread.php?t=264432),
[B024 report #41](https://www.mobileread.com/forums/showthread.php?t=264432&page=3).
The report's forced reboot after a later hung update is not an authorized
recovery action.

## SSH preparation decision for the later action sheet

Propose the selected PW1 USBNetwork package with OpenSSH backend so Windows can
prepare a unique Ed25519 server key without executing a Dropbear utility.
Generate that key privately on Windows, retain its public-key fingerprint,
and stage it via USB to `usbnet/etc/ssh_host_ed25519_key` before starting SSH.
Keep the host private key out of Git and chat output. Configure an explicit
`HostKey /mnt/us/usbnet/etc/ssh_host_ed25519_key` so bundled defaults are not used.
Back up the installed config first and confirm actual paths against the installed
package before modifying anything.

Proposed LF-only settings: `USE_WIFI="true"`, `USE_WIFI_SSHD_ONLY="true"`,
`USE_OPENSSH="true"`; keep `usbnet/auto` absent. Stage only Windows/Mac client
public keys in `usbnet/etc/authorized_keys`. Manual KUAL toggle starts/stops SSH;
USB mass storage remains selected. Compare the first connection fingerprint to
the privately generated server-key fingerprint; do not bypass host-key checks.
This is a provisioning plan, not authorization to install/configure/start SSH.

The saved Speedport port rule is configuration evidence only. Before the first
Wi-Fi connection, finish a controlled isolation verification plan; if testing
would require temporarily disconnecting the router WAN, obtain approval for
that household connectivity interruption separately. Never join an unrestricted
network merely to test the block.
