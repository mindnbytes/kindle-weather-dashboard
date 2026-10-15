# M3 — Manual Kindle HTTP fetch and single draw

Prepared 2026-10-15. Owner approved; one fetch, exact hash read-back and draw
completed successfully. Mac logged the Kindle GET with HTTP 200. Temporary Mac
server stopped and exited zero. Owner accepted physical rendering; stock UI's
top line returns after approximately one minute. Commands below record the approved procedure, not authorization
to repeat it.

## Preconditions observed

- Restored OpenSSH connection passes the original strict host-key check.
- Kindle reports firmware 5.6.1.1. Installed curl help confirms -q, --fail,
  --silent, --show-error, --connect-timeout, --max-time, --max-filesize,
  --noproxy and --output. The old Kindle shell has no `command` builtin;
  `command -v` failed during inspection, while `curl --help` succeeded.
- `/mnt/us/weather-http-m3.png` is absent. Existing M2 PNG is preserved.
- Mac server: `nix develop -c python -m server.serve --bind 192.168.2.52`.
  Mac HTTP control request succeeded and matched runtime/weather.png SHA-256:
  `75ce723f35717273c226ab8678b13767fe8c8934463abb6eeab8cee7cb166992`.
- Image is the reviewed invented API fixture, 758x1024 grayscale. Keep the
  Kindle-only router blocker enabled. No live weather API involved.

## Exact proposed device actions

Run over the existing strict Mac SSH connection (original Ed25519 key and
known_hosts.kindle; no password or changed host-key acceptance).

1. Recheck destination absence, then perform one bounded local HTTP fetch:

```sh
test ! -e /mnt/us/weather-http-m3.png && test ! -L /mnt/us/weather-http-m3.png && curl -q --fail --silent --show-error --connect-timeout 5 --max-time 20 --max-filesize 1048576 --noproxy '*' --output /mnt/us/weather-http-m3.png http://192.168.2.52:8000/weather.png
```

The image is written only to a new user-storage path. No redirects or automatic
retries requested. Stop on any failure; a partial file may remain and must not
be drawn or overwritten automatically. No proxy or default .curlrc settings used.

2. Read back the exact downloaded bytes over SSH:

```sh
cat /mnt/us/weather-http-m3.png
```

On the Mac, hash this stdout with `shasum -a 256`, using pipefail so SSH failure
cannot look like successful verification. Continue only on zero status and the
exact hash above. Check the Mac HTTP log for the Kindle's GET and status 200.

3. Once verified, draw once with the already tested binary/options:

```sh
/mnt/us/libkh/bin/fbink -f -w -i /mnt/us/weather-http-m3.png
```

Owner keeps the device awake and observes the image. Do not touch through the
PNG into the underlying UI. Stock UI overwrite/touch behavior remains known;
this test does not establish persistent dashboard mode. No backend selection,
configuration edit, new binary installation, root remount, service stop, sleep
change or scheduler included.

## End state

After the single fetch/draw attempt, stop the temporary Mac server with Ctrl-C
and verify its process has exited. Record actual outcomes, including visual
owner acceptance separately from command exit status. Leave the new PNG in
user storage. When parking: owner stops SSH with KUAL Toggle USBNetwork (not
backend selection), confirms SSHD down and enables airplane mode. Router blocker
and absent automatic startup stay unchanged.
