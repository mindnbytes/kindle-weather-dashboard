# Windows RNDIS driver review — 2026-10-15

USB SSH is blocked at Windows device recognition. Correlated Kindle gadget
VID_0525/PID_A4A2 currently binds to Microsoft usbser.inf as COM3, not a network
adapter. Unplug/replug correlation was observed. The inbox rndiscmp.inf Have Disk
route was rejected; user then showed the model picker limited to serial drivers.
No driver was installed by that attempted selection.

## Selected package

[Microsoft Update Catalog exact hardware-ID query](https://www.catalog.update.microsoft.com/Search.aspx?q=usb%5Cvid_0525%26pid_a4a2)
lists Acer Incorporated USB Ethernet/RNDIS Gadget, version 1.0.0.0, with
AMD64/X86 support and hardware ID USB\VID_0525&PID_A4A2.
Selected update ID: `38c84d13-eb1b-4327-aae5-e36e8cb7933d`.

Exact Microsoft-hosted download:
https://catalog.s.download.windowsupdate.com/msdownload/update/driver/drvs/2012/12/20342322_4b9970e3174b23b5cb2371af0837f939a71271ea.cab

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| CAB | 21926 | `aec19e7a9cadbc0b6c3369a71beb3286c53363007c3fe209315d0d8b988574c7` |
| RNDIS.inf | 3145 | `d4be3054b3d780d2dd7bed4cdc35824b324e7df59a390a54a43f84de1fb75666` |
| rndis.cat | 7077 | `da482926d12e97b04dc2d03b648905bbeb450d81554b8c76c57689f3b67e55be` |

Downloaded directly from Microsoft, extracted privately under the dated PC
KindleSetup rndis-review folder. No INF modifications or binary downloads from
other sources. INF explicitly matches the observed hardware ID in its AMD64
section and declares Net class. It references inbox usb8023.sys and rndismp.sys;
both exist locally and identify Microsoft Corporation as vendor.

Get-AuthenticodeSignature reports catalog Valid, signed by Microsoft Windows
Hardware Compatibility Publisher with Microsoft timestamp. Installed Windows
SDK x64 SignTool `verify /kp /v /c rndis.cat RNDIS.inf` verified catalog membership
and kernel signing policy: one verified file, zero warnings, zero errors.
This does not guarantee successful runtime behavior on Windows build 26300.

## Reviewed user-operated installation route

1. Leave airplane mode on and USBNetwork toggled on; Kindle connected.
2. Cancel the serial-model picker. Reopen Update driver for only the correlated
   USB Serial Device (COM3), then Browse my computer for drivers.
3. Select the private extracted folder containing this RNDIS.inf and rndis.cat,
   with Include subfolders selected. Let Windows evaluate the exact hardware
   match; do not select a different serial model or edit INF to force a match.
4. Proceed with the matched USB Ethernet/RNDIS Gadget package. Stop for signature,
   compatibility, restart-required or security-policy warnings and report them.
   Do not disable signature enforcement or security features.
5. Reinspect PnP driver binding, problem code and network adapter appearance.
   Only then configure the reviewed USB adapter address and attempt key-verified
   SSH. No unrelated network adapter, firewall or sharing changes.

Package registration may persist on Windows after the USB test. No driver-store
removal is part of normal teardown. If correction fails, diagnose separately;
the old serial binding was Microsoft usbser.inf. No automatic removal/rebind or
Windows restart is authorized as a troubleshooting retry.

Sources: Microsoft Update Catalog package/metadata and locally inspected signed
INF/catalog; [Microsoft RNDIS documentation](https://learn.microsoft.com/en-us/windows-hardware/drivers/network/remote-ndis--rndis-2).
