# M2 — First PNG transfer and single draw

Prepared 2026-10-15. Owner approved; transfer, hash read-back and single draw
completed with exit status zero. Owner confirmed the image rendered and looked
good, accepting the first physical display. Long-term behavior is unmeasured.
Commands below record the approved procedure, not authorization to repeat it.
Existing FBInk 1.25.0 executes and advertises Kindle/PNG support. This is not
yet proof of framebuffer compatibility or physical display quality.

Use the existing Mac terminal from the project root; keep the Kindle-only router
blocker enabled and the current manually started SSH session available. Owner
keeps the Kindle awake on its normal portrait UI and observes the screen.
No renderer regeneration or binary installation is needed.

Define a local Mac shell array to preserve the working SSH options:

```sh
kindle_ssh_opts=(
  -i /Users/alex/.ssh/id_ed25519
  -o IdentitiesOnly=yes
  -o PasswordAuthentication=no
  -o HostKeyAlgorithms=ssh-ed25519
  -o UserKnownHostsFile=/Users/alex/.ssh/known_hosts.kindle
  -o StrictHostKeyChecking=yes
  -o BatchMode=yes
  -o ConnectTimeout=10
)
```

1. Recheck that the new image path is absent (including dangling symlinks).
   Continue only on status zero; stop on collision or network failure.

```sh
ssh "${kindle_ssh_opts[@]}" root@192.168.2.79 'test ! -e /mnt/us/weather-m2.png && test ! -L /mnt/us/weather-m2.png'
```

2. Copy the verified existing PNG once to user storage. `-O` uses legacy SCP
   with the old SSH server. Stop on an error; do not retry automatically.

```sh
scp -O "${kindle_ssh_opts[@]}" /Users/alex/Projects/mindnbytes/kindle-weather-dashboard/weather.png root@192.168.2.79:/mnt/us/weather-m2.png
```

3. Read back the remote bytes and compare the SHA-256 with the local PNG.
   Continue only when SSH succeeds and hashes match exactly. A transfer error
   or mismatch does not authorize deletion, recopy or draw.

```sh
shasum -a 256 /Users/alex/Projects/mindnbytes/kindle-weather-dashboard/weather.png
set -o pipefail
ssh "${kindle_ssh_opts[@]}" root@192.168.2.79 'cat /mnt/us/weather-m2.png' | shasum -a 256
```

4. Draw once with the installed binary, requesting a flashing refresh and
   waiting for completion. Leave the stock UI/power services running. Capture
   diagnostics and exit status; stop on error or unexpected behavior.

```sh
ssh "${kindle_ssh_opts[@]}" root@192.168.2.79 '/mnt/us/libkh/bin/fbink -f -w -i /mnt/us/weather-m2.png'
```

Owner reports whether the full portrait image appeared, whether text/icons are
readable and unclipped, visible ghosting, and whether/when the stock UI overwrites
it. A successful command alone is not physical acceptance. No stock UI shutdown,
root remount, waveform experimentation, scheduler or sleep changes are included.
The PNG remains in user storage; removal requires a separately reviewed command.

After observations, follow the existing owner teardown: close SSH sessions,
KUAL USBNetwork toggle once to stop SSH, confirm SSHD down, enable airplane mode.
Keep the router blocker enabled and automatic SSH startup disabled.
