# Restore the previously verified OpenSSH selection

Prepared 2026-10-15 after USB read-only diagnosis. Owner approved restoration and
requested agent execution. Completed by direct USB config edit rather than the
menu procedure below: private config backup, exact false→true replacement,
flush/fsync, exact read-back and unchanged support-file hashes verified. See
experiments.md. Network reconnection remains pending. Steps below preserve the
original menu proposal, not authorization to repeat it.
Only intended device configuration change: USE_OPENSSH="false" → "true" in
usbnet/etc/config, using the installed KUAL action. Preserve all keys, other
settings and the Mac's trusted known_hosts entry.

Evidence: installed usbnetwork selects Dropbear when false and OpenSSH when
true. Installed KUAL "SSHD: Use OpenSSH" calls use_openssh, which edits that
setting to true. Unique OpenSSH public host key still matches trusted Mac key.
No private-key contents need reading; no key generation or root remount proposed.

After approval:

1. Back up the current USB config privately on Mac and record its SHA-256;
   retain an inventory of the public-key fingerprint and sshd_config hash.
2. Owner safely ejects Kindle and unplugs USB, keeping airplane mode enabled
   and SSH stopped. Open KUAL → USBNetwork → **SSHD: Use OpenSSH** once.
   This is the backend selection action, not Toggle USBNetwork. Stop on error.
3. Reconnect USB storage while airplane mode remains on. Agent verifies that
   only USE_OPENSSH changed to true, other configuration/key evidence is
   unchanged, and usbnet/auto is absent. Stop on an unexpected difference.
4. After successful read-back, use the established protected-WLAN/manual SSH
   startup sequence, with the router blocker still enabled. Retry strict Mac
   host-key checking against the observed IP. Stop on any further mismatch;
   do not accept a new key or disable verification.

This restoration does not authorize image fetching/drawing, unattended startup,
firmware actions, cleanup or power-management changes. Those retain their gates.
