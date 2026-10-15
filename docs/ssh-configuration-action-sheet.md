# Prepare manual Wi-Fi SSH through USB storage

Prepared 2026-10-15. **Pending approval; prepared on Windows only.**
PW1 USBNetwork installation has passed owner and log checks on 5.6.1.1.
Airplane mode stays on and no server start is included in this stage.

## Prepared changes

Original `usbnet/etc/config` and `sshd_config` are backed up privately on Windows,
with matching SHA-256. New files are prepared under the private dated KindleSetup
ssh-prep directory, not Git. No private-key contents are written into logs/chat.

| File under `usbnet/etc/` | Selected change |
| --- | --- |
| `config` | Change only USE_WIFI, USE_WIFI_SSHD_ONLY and USE_OPENSSH from false to true; preserve other settings and LF endings. |
| `sshd_config` | Use only `/mnt/us/usbnet/etc/ssh_host_ed25519_key_pw1` as HostKey; explicit AuthorizedKeysFile `/mnt/us/usbnet/etc/authorized_keys`; PubkeyAuthentication yes; PasswordAuthentication no; KbdInteractiveAuthentication no; replace PermitRootLogin yes with prohibit-password. Preserve other existing settings. |
| `authorized_keys` | One existing Windows id_ed25519 public key in OpenSSH format, with a generic comment. No client private key copied. |
| `ssh_host_ed25519_key_pw1` | Newly generated unique Ed25519 server private key; dedicated filename preserves the package's existing host keys. |
| `ssh_host_ed25519_key_pw1.pub` | Matching host public key; its fingerprint is retained privately on Windows for first-connection verification. |

The explicit HostKey selects the unique key instead of bundled default host keys.
USE_WIFI_SSHD_ONLY keeps USB mass storage selected when the server is later
started manually. Keep `usbnet/auto` absent. These settings permit a future
key-authenticated root SSH connection; approval does not include starting it.

## Exact actions after approval

1. Confirm Kindle USB volume and airplane mode. Verify usbnet/auto absent,
   installed config and sshd_config still match the private originals, and no
   existing authorized_keys or selected unique-host-key destination would be
   overwritten. Stop on any mismatch/collision; inspect rather than retry.
2. Recheck prepared Windows files: LF-only configs/authorized_keys, one valid
   selected public key, matching generated host keypair/fingerprint. Build a
   private source byte-count/SHA-256 inventory before device writes.
3. Copy only the five files above to `F:\usbnet\etc\` (after volume confirmation)
   with literal paths. The two config replacements are explicitly approved;
   the other three destinations must be absent before copying. Preserve old
   configs in the verified private PC backup.
4. Flush each file and verify destination sizes and SHA-256 against the private
   source inventory, without printing private keys. Re-read only the selected
   configuration directives. Confirm usbnet/auto remains absent.
5. Stop with USB mass storage available, airplane mode on, SSH server unstarted.
   No KUAL toggle, reboot, firmware update, Wi-Fi join or router change included.

Mac public-key authorization is a later addition using only the Mac's public key.
Neither Windows nor Mac client private keys may be copied to the Kindle.
No global Windows SSH settings need changing.

## Next separate network gate

Speedport's Kindle-only TCP/UDP 0–65535 blocker is saved, but traffic blocking
and LAN peer access are untested. Before any Kindle Wi-Fi connection, agree a
controlled verification procedure. If it requires temporarily disconnecting the
router's WAN, obtain approval for that connectivity interruption separately.
Do not treat the saved rule alone as proof of isolation. Starting SSH is also
a separate reviewed action after this USB configuration step.
