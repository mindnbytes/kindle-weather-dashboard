Read `kindle-weather-dashboard.md` before working here. It defines device safety,
milestones, and review gates. Read `README.md` and `docs/experiments.md` for current
implementation and evidence. Use `nix develop` for development.

Current scope: owner-directed Windows M1 device setup. Downgrade, jailbreak,
hotfix, return to 5.6.1.1, KUAL/MRPI and PW1 USBNetwork installation have passed
their recorded checkpoints. USB public-key SSH smoke check and teardown passed;
USB mass-storage mode is restored. Wi-Fi-only SSH config is applied/verified,
but radio and server have not been started. Owner paused before reconfirming
the Speedport Kindle-only internet blocker. On resume, reconfirm that rule and
review deliberate Wi-Fi connection/isolation, then test Windows and Mac access.
Keep airplane mode on. Device modification requires explicit approval of exact
commands; consult the action sheets and latest experiment entries. Renderer
development remains on Mac/Nix; do not regenerate it on Windows.
