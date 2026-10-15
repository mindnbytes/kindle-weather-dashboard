# Prepare manual Wi-Fi SSH through USB storage

Prepared 2026-10-15; updated after successful USB SSH test and teardown.
**Wi-Fi changes remain pending approval.** PW1 USBNetwork and USB public-key SSH
passed on 5.6.1.1. Airplane mode stays on and no server start is included here.

## Prepared changes

Original `usbnet/etc/config` and `sshd_config` are backed up privately on Windows,
with matching SHA-256. The subsequent approved USB test installed key-only
OpenSSH support and unique server keys, all verified. Prepared Wi-Fi config is
under the private dated KindleSetup ssh-prep directory, not Git. Do not replace
or regenerate the working keys. No private-key contents are written into logs/chat.

| File under `usbnet/etc/` | Selected change |
| --- | --- |
| `config` | Pending: change only USE_WIFI and USE_WIFI_SSHD_ONLY from false to true; USE_OPENSSH is already true. Preserve other settings and LF endings. |
| `sshd_config` | Already applied/verified through USB: unique HostKey, explicit authorized_keys path, public-key-only root authentication. Preserve unchanged. |
| `authorized_keys` | Already applied/verified: existing Windows id_ed25519 public key only. Preserve unchanged; Mac public key is a later addition. |
| `ssh_host_ed25519_key_pw1` | Unique server private key already installed; preserve unchanged. |
| `ssh_host_ed25519_key_pw1.pub` | Matching host public key already verified against the USB connection; preserve unchanged. |

The explicit HostKey selects the unique key instead of bundled default host keys.
USE_WIFI_SSHD_ONLY keeps USB mass storage selected when the server is later
started manually. Keep `usbnet/auto` absent. These settings permit a future
key-authenticated root SSH connection; approval does not include starting it.

## Exact actions after approval

1. Confirm Kindle USB volume and airplane mode. Verify usbnet/auto absent,
   current config matches the privately recorded USB-only baseline and the
   four key/auth files match the successful USB-test inventory. Stop on mismatch.
2. Back up the current working USB-only config privately and verify its hash.
   Compare prepared Wi-Fi config against it: only the two flags above may differ;
   preserve LF endings and record the prepared source hash.
3. After separate Wi-Fi-stage approval, copy only prepared `config` to
   `F:\usbnet\etc\config` with a literal path after volume confirmation. Do not
   recopy keys, authorized_keys or sshd_config. This sheet remains unapproved;
   approval given to the prior USB-only setup does not enable Wi-Fi.
4. Flush and verify config size/hash, re-read the selected directives, and
   verify other four files unchanged. Confirm usbnet/auto remains absent.
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
