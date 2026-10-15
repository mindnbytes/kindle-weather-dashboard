# Manual Wi-Fi SSH acceptance check

**Windows acceptance passed 2026-10-15:** USB unplugged, trusted host-key match,
public-key root login, four shell checks and repeat connections. A bounded
IPv4 HTTP probe was refused on Kindle while Windows reached the same endpoint;
this is limited egress evidence, not exhaustive isolation proof. Owner also
confirmed Mac public-key access and all four shell checks, then server
stop/airplane-mode teardown before pausing. See experiments.md for exact outcomes.

Prepared 2026-10-15 on owner-requested resume. USB-only SSH and teardown passed;
Wi-Fi-only config was separately approved, applied and verified. This page
defines the remaining manual start and read-only connection check. No firmware,
power-management, automatic-startup or framebuffer changes are included.

## Before radio enable

Keep airplane mode on. Recheck USB storage config SHA-256 against the recorded
Wi-Fi hash and all four key/auth files against the successful USB-test baseline;
confirm usbnet/auto absent. Verify the saved Speedport rule is enabled, blocks
TCP and UDP 0–65535 and applies only to the privately MAC-matched Kindle entry.
If any check fails, stop without starting the server or joining Wi-Fi.

Rule confirmation establishes the intended router policy, not a measured claim
about all traffic. Report those evidence levels separately. Radio enable must
be a deliberate owner action with this selected rule already in place.

## Manual start and join

1. Safe-eject Kindle in Windows and unplug USB. Keep it unplugged for acceptance.
2. Open KUAL → USBNetwork → Toggle USBNetwork once. With the verified
   USE_WIFI_SSHD_ONLY=true setting, this starts only the key-authenticated
   OpenSSH server and retains USB mass-storage support. Do not enable startup
   at boot or change the SSH backend/settings.
3. Turn airplane mode off and join only the trusted home WLAN protected by the
   verified Kindle-specific rule. Enter any Wi-Fi password privately on Kindle.
   Do not register, visit the store, request an update or join a guest network.
4. Read the Kindle's actual address from the MAC-matched router device entry
   (formerly named PC192-168-2-79); do not assume its old address is unchanged.
   Report only its private LAN IP. USB must remain unplugged.

## Windows acceptance

Use the observed address only. Verify TCP 22, scan its Ed25519 host public key
and compare complete key bytes with the trusted unique key from USB testing.
On match, save a dedicated Wi-Fi known_hosts entry privately. Use the existing
Windows id_ed25519 identity and strict host-key checking; no global SSH changes,
password fallback or guessed credentials.

Run `uname -a`, `id`, `mount`, `df -h`; save complete output privately and record
redacted results. Repeat a connection while USB remains unplugged. Check actual
network routes/addresses without exposing full device identifiers. Only after
reviewing available tools, perform bounded, minimal connectivity probes to
evaluate the saved internet-blocking policy. Compare with a working control
from Windows so a dead endpoint is not mistaken for router enforcement. Do not
call an old TLS failure or bad device clock proof of isolation. Stop and return
to airplane mode if the expected block fails; investigate separately.

Mac acceptance remains separate until the Mac's public key is authorized and a
connection from that machine is observed. Do not mark it passed from Windows.
No client private key may be copied to Kindle or committed.

## End state / stop rules

For an authentication/host-key/connection failure, keep existing keys, record the
error, and diagnose. Do not recopy/reinstall or weaken global SSH policy.
For an unexpected device error, pause and review before mode switches/reboots.

At the end of the manual test, close SSH sessions, use KUAL's USBNetwork toggle
once to stop the server, and return to airplane mode unless the owner requests
continuing the tested LAN session. Keep automatic SSH startup disabled. Confirm
normal USB mass-storage recovery remains available. No unattended server,
refresh scheduler or power changes are included in this check.
