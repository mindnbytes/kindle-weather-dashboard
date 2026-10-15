# KUAL Kindlet and MRPI on PW1 5.6.1.1

Prepared 2026-10-15. **Completed:** KUAL and nine MRPI files copied and
hash-verified; owner confirmed KUAL opens and Helper → Install MR Packages is
available. Historical instructions below do not authorize a repeat installation.
Prerequisites: confirmed PW1 firmware 5.6.1.1, successful post-update hotfix and
usable home screen reported by owner. Keep airplane mode enabled throughout.

## Exact selected artifacts

Use the regular `KUAL-v2.7.37-gfcb45b5-20250419.tar.xz`, not coplate/booklet.
Archive SHA-256:
`40c4b68712213adc7b667b9502cdd0c8099761fce1e1bf2b161b84102af54135`.
Copy only its `KUAL-KDK-2.0.azw2`, 131070 bytes, SHA-256
`1d7cf02741be9e8f9c541af4eb5e1a97c00ab158819236749dba9250ad1fd4a9`,
to the Kindle's `documents/KUAL-KDK-2.0.azw2` (currently F: when connected).
This matches the archive README's PW1 instructions and October B024 report.

MRPI archive: `kual-mrinstaller-1.7.N-r19303.tar.xz`, SHA-256
`36b3c28a44ad1a91609cc82d2bb9836ad6d7125ba1f63596307bf93f17a9255e`.
Copy its `extensions/MRInstaller` directory tree and `mrpackages` directory to
the USB root. Do not put any installer BINs into `mrpackages` in this stage.
Exact archive URLs, sizes and provenance are in [package-review.md](package-review.md).
The selected source archive and KUAL inner-file hashes were rechecked locally.

## Actions after approval

1. Connect the working USB cable. Re-identify Kindle volume; do not assume F:.
   Stop on existing root update BINs, an existing KUAL target file, existing
   `extensions/MRInstaller`, or any nonempty existing `mrpackages` directory.
   Inspect without deleting or overwriting. Existing unrelated extensions, if
   present, must be preserved.
2. Reverify source archives and selected KUAL hash. Extract MRPI into a fresh
   PC-only folder. Check archive member paths and types before extraction;
   refuse absolute paths, traversal, symlinks or unexpected content. Build
   a per-file SHA-256 inventory of the selected MRInstaller tree.
3. Copy `KUAL-KDK-2.0.azw2` with a literal-path copy to `documents/`.
   Copy the selected MRInstaller tree once to `extensions/MRInstaller` and
   create the empty `mrpackages` directory if absent. No other KUAL artifacts,
   root BINs, helper installers or package payloads are included.
4. Flush copied files and compare their sizes and SHA-256 with the source
   inventory. Verify `mrpackages` is empty. Stop on any failure; no retry.
5. Safely eject in Windows, then unplug USB. Open the KUAL library item once.
   If hidden, check All Items/search. Stop if it cannot be found or opened;
   do not substitute a different launcher or modify certificates.
6. Expected: KUAL opens, with **Helper → Install MR Packages** available.
   Report that menu's presence; do not select Install MR Packages yet.
7. Stop for developer-certificate errors, application errors, freezes or
   unexpected behavior. No extra reboot, MKK reinstall or hotfix rerun is
   authorized by this stage. Return to the home screen normally when done.

This stage adds launcher/installer support to user storage and launches KUAL.
It does not authorize a USBNetwork installation, SSH startup or Wi-Fi connection.
MRPI can later make system changes when invoked with approved packages; its
mere menu presence does not establish that any package has installed.

Evidence: archive README,
[B024 report #41](https://www.mobileread.com/forums/showthread.php?t=264432&page=3),
[MRPI maintainer installation instructions](https://www.mobileread.com/forums/showthread.php?t=251143).
