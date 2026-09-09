---
layout: plugin

id: reality_check
title: Reality Check
description: Blocks a print streamed over serial when the gcode's filament type or nozzle size contradicts what the printer's firmware reports loaded/fitted (Prusa Buddy M865 / M862.1 Q).
authors:
- Nitzan Raz
license: AGPLv3

date: 2026-09-09

homepage: https://github.com/BackSlasher/OctoPrint-Reality-Check
source: https://github.com/BackSlasher/OctoPrint-Reality-Check
archive: https://github.com/BackSlasher/OctoPrint-Reality-Check/archive/main.zip

tags:
- filament
- nozzle
- validation
- safety
- prusa
- buddy
- mismatch
- gcode check

screenshots:
- url: /assets/img/plugins/reality_check/block-popup.png
  alt: A print sliced for PLA blocked because the printer reports PETG loaded
  caption: A PLA-sliced print blocked because the printer reports PETG loaded
- url: /assets/img/plugins/reality_check/pass-popup.png
  alt: The Reality Check tab with the printer inventory and recent check results
  caption: The Reality Check tab - printer inventory and recent checks
- url: /assets/img/plugins/reality_check/settings.png
  alt: The settings panel
  caption: Settings

featuredimage: /assets/img/plugins/reality_check/block-popup.png

compatibility:
  octoprint:
  - 1.5.0

  os:
  - posix
  - windows
  - macos
  - freebsd

  python: ">=3.7,<4"

attributes:
- ai-developed
---

Prusa Buddy printers (CORE One, MK4 family, XL...) validate filament type and
nozzle size themselves - but only for **file-based** prints (USB stick,
PrusaLink, Connect), where the firmware can read the file's metadata. A print
streamed from OctoPrint over serial arrives one command at a time and
bypasses every one of those checks. Slice with the wrong preset and the
printer lays PETG on a 60°C bed without a word.

Reality Check restores the missing gate:

1. While the printer idles, it polls the firmware's own state: `M865 I<tool>`
   (loaded filament type - the same state the printer's file-print preview
   trusts) and `M862.1 Q` (fitted nozzle diameter / hardened / high-flow,
   from EEPROM).
2. When a print starts, it holds the first job command in OctoPrint's
   gcode-queuing phase, reads `; filament_type` and `; nozzle_diameter` from
   the selected file, and compares.
3. On mismatch it cancels the print and pops an error naming both sides and
   the ways out (reslice, reload, or ignore via settings). A warn-only mode
   shows the popup without cancelling.

No spool database, no bookkeeping, no companion plugins: the printer is the
single source of truth. Anything that updates the printer's loaded filament -
its own load/change UI, or an external `M865 S"PETG" L0` - feeds the check
automatically. Unknown states fail open with an explanation; the plugin only
blocks on a positive contradiction.

A **Reality Check tab** shows the current printer inventory (per-tool
filament and nozzle, with flags), the cache age, a manual refresh button and
a collapsible table of recent check results. Tool count follows OctoPrint's
printer profile.

Requires a Prusa Buddy-firmware printer connected over serial with `M865`
support (test by sending `M865 I0` in the terminal - you should get
`name:<type>` back) and gcode that carries `; filament_type` /
`; nozzle_diameter` comments (PrusaSlicer does).
