# USB-only SSH smoke check on Windows

Prepared 2026-10-15 at owner's request, before pending Wi-Fi setup.
**USB smoke check passed:** adapter recognized after reviewed signed-driver
installation, unique host key matched, public-key root login and all four
read-only commands succeeded. Session exited normally; restored Windows DHCP/DNS
and Kindle mass-storage mode were verified. Test and teardown are complete.
Wi-Fi remains disabled and airplane mode stays on throughout.

## Read-only preflight evidence

Kindle USB volume F: is available. Installed settings: KINDLE_IP=192.168.15.244,
USE_WIFI=false, USE_WIFI_SSHD_ONLY=false, USE_OPENSSH=false. No authorized_keys,
selected unique server key, or usbnet/auto exists. Windows has no non-default
IPv4 route matching the proposed Kindle address. No Kindle USB Ethernet adapter
is currently enumerated while the device is in mass-storage mode.

Installation logs and original config/sshd_config were backed up and hash-verified
privately. Device-stage commits are 322ae96 and 0fcc75b. The Wi-Fi configuration
action sheet remains pending and is not applied for this test.

## Proposed device actions

1. Reconfirm F: as Kindle and original configs unchanged. Keep airplane mode on.
   Stop on existing selected key destinations or unexpected state.
2. Stage the five prepared files from the private PC ssh-prep folder to
   `F:\usbnet\etc\`, with literal-path copies. A private byte-count/SHA-256
   inventory pins the exact prepared bytes before copying:

   | Source | Device destination | Effect |
   | --- | --- | --- |
   | config.usb-only | config | Change only USE_OPENSSH to true from installed default. USE_WIFI and USE_WIFI_SSHD_ONLY stay false; KINDLE_IP stays 192.168.15.244. |
   | sshd_config | sshd_config | Explicit unique Ed25519 HostKey path and authorized_keys path; public-key auth enabled, password/keyboard-interactive auth disabled; root login restricted to keys. Other original settings preserved. |
   | authorized_keys | authorized_keys | Existing Windows id_ed25519 public key only; client private key stays on Windows. |
   | ssh_host_ed25519_key_pw1 | ssh_host_ed25519_key_pw1 | Unique generated server private key; preserves bundled default keys under other filenames. |
   | ssh_host_ed25519_key_pw1.pub | ssh_host_ed25519_key_pw1.pub | Matching public key; fingerprint recorded privately for verification. |

3. Flush and SHA-256 verify all copied files. Keep usbnet/auto absent; verify
   Wi-Fi flags remain false. Stop on any mismatch; no automatic retry.
4. Windows safe eject, unplug. Open KUAL → USBNetwork → **Toggle USBNetwork**
   once. This is the reviewed manual server start and USB networking switch.
   Do not select Enable SSH at boot or any Wi-Fi configuration option.
5. Reconnect USB. Expect F: to disappear and a USB Ethernet/RNDIS/CDC adapter to
   appear. Inspect Windows adapters/Device Manager. If missing or unknown,
   stop at diagnosis: no arbitrary drivers, unsigned drivers or security changes.

## Windows connection check

1. Identify the newly appeared USB adapter by before/after inventory and device
   association. Record its original IPv4/DNS settings before any change.
2. Configure **only that adapter** to host 192.168.15.201/24, with no default
   gateway or DNS. Confirm no subnet conflict. Prepare exact commands using the
   observed interface index before execution. No change to normal LAN/Wi-Fi,
   Internet Connection Sharing, bridge, global firewall or global SSH options.
3. Read port 22 availability at 192.168.15.244. Obtain the offered Ed25519 public
   host key, compare its SHA-256 fingerprint to the key generated privately on
   Windows, and stop on mismatch. A network scan alone does not establish trust.
   Use a dedicated private known_hosts file only after that comparison.
4. Invoke Windows OpenSSH with explicit existing Windows id_ed25519 identity,
   IdentitiesOnly=yes, StrictHostKeyChecking=yes, dedicated known_hosts,
   PasswordAuthentication=no, KbdInteractiveAuthentication=no, connection timeout,
   and root@192.168.15.244. Use an agent/unlocked key or let the owner handle a
   local passphrase prompt; never request or log the passphrase.
5. Execute only `uname -a`, `id`, `mount`, `df -h`. Keep complete output private;
   record redacted evidence in experiments.md. No root remount, clock correction,
   firmware change or framebuffer operation is included.

## Teardown

Exit SSH normally. Restore the recorded Windows USB adapter settings while
the interface is still available, then unplug USB. On PW1, use the documented
KUAL USBNetwork toggle once to stop SSH and return to USB mass storage; reconnect
and verify F: returns. No reboot is part of teardown. Keep airplane mode on and
automatic SSH startup disabled. The key-only USB config may remain as the
reviewed baseline; Wi-Fi setup remains a separate later action.

Stop for authentication, host-key, driver, mode-switch or startup errors. Record
actual evidence and review the next step; do not broaden algorithms, change
passwords, enable Wi-Fi or improvise retries.

Sources already read: selected USBNetwork README_FIRST.txt, default config,
sshd_config, usbnetwork toggle script and KUAL menu. The maintainer explicitly
supports keys with OpenSSH and the default USB addresses 192.168.15.244/201.
