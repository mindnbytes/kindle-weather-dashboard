# M2 — Existing FBInk preflight

Prepared 2026-10-15. Historical preflight plan, subsequently executed successfully:
FBInk 1.25.0 with PNG support was found. Transfer and single draw then passed,
and owner accepted physical display. See experiments.md for outcomes. Instructions
below retain the original preflight scope, not authorization to repeat it.

## Candidate and evidence

The pinned hotfix package inspection recorded `/mnt/us/libkh/bin/fbink` as a
supplied binary (see package-review.md). Check this existing candidate before
considering any new installation. Its current presence, version, compiled image
support and runtime compatibility on this PW1 remain unverified.

Upstream references checked on 2026-10-15:

- [FBInk CLI](https://github.com/NiLuJe/FBInk/blob/master/CLI.md): image support
  is conditional on compilation; `-i` selects an image and `-f` requests a
  flashing refresh.
- [CLI source](https://github.com/NiLuJe/FBInk/blob/master/fbink_cmd.c): the
  explicit `--help` path exits before opening/initializing the framebuffer.
  This is current upstream behavior, not a version match to the installed binary.
  Use the long `--help` option; `-h` means invert.

## Owner preflight

Keep the existing Kindle-only router blocker enabled. Resume the previously
tested protected WLAN/manual KUAL USBNetwork startup procedure, leave USB
unplugged, and use the observed current IP and the Mac's existing public-key SSH
command with strict host-key checking and dedicated known_hosts.kindle. Stop on
a changed host key, connection error or unexpected device behavior; preserve the
working keys/settings.

In that Kindle SSH shell, run these separately and retain their output:

```sh
ls -l /mnt/us/libkh/bin/fbink
test -x /mnt/us/libkh/bin/fbink && /mnt/us/libkh/bin/fbink --help
ls -ld /mnt/us/weather.png /mnt/us/weather-m2.png
```

Missing image paths are expected and useful collision checks. If FBInk is absent
or not executable, stop; do not chmod, replace or install it. Record the complete
help output, including version, target and image/refresh options. No image draw,
root remount, stock UI stop, sleep change or persistent configuration change is
included. This preflight does not establish framebuffer/device detection yet.

## Following checkpoint

After reviewing the actual output, prepare the exact approved transfer and
single-draw commands. Prefer a new user-storage image path, verify transferred
bytes, and use only options supported by the installed binary. Modern Mac scp
may need its legacy SCP mode (`-O`) with this old server; do not change the
working SSH service to add SFTP. Do not execute a transfer or framebuffer command
under this preflight.

The existing Mac image was rechecked with `file`: 758x1024, 8-bit grayscale PNG.
Before transfer, recheck its hash and dimensions in the Nix environment. Inspect
actual orientation, full image coverage, contrast, ghosting and stock UI
overwrite on the device. Do not fix overwrites by stopping services or changing
power management in this milestone.

At the end of a session, use the established manual KUAL toggle to stop SSH,
confirm SSHD down, and enable airplane mode. Leave the router blocker enabled.
