---
layout: plugin

id: reality_check
title: Reality Check
description: Block a print if the file wants a different setup than what the printer currently reports (Prusa Buddy M865 / M862.1 Q).
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
nozzle size themselves for **file-based** prints (USB stick,
PrusaLink, Connect), where the firmware can read the file's metadata.
Printing over serial (e.g. OctoPrint) arrives one command at a time and
can't have those checks. If you're like me, you'll print a PLA gcode with
a PETG filament loaded and wonder why the print doesn't adhere to the bed. No more!

Reality Check helps by blocking prints that specify a setup that doesn't match the printer's report.

1. While the printer idles, it polls the firmware's own state:  
   1. `M865 I<tool>` for loaded filament type
   2. `M862.1 Q` for nozzle configuration
2. Plugs into "gcode-queueing" phase, reads `; filament_type` and
   `; nozzle_diameter` from the file, and compares.
3. On mismatch it cancels the print and pops an error message.  
   Can be configured to only warn and let the print go through.

The main value here is simplicity. We have no persistence and
read world state from the printer itself.
Fail open on unexpected states (no filament read from printer) -
only block when we **know** there's a mismatch.

A dedicated tab for current printer inventory and event log.

Requires a Prusa Buddy-firmware printer connected over serial with `M865`
support (test by sending `M865 I0` in the terminal - you should get
`name:<type>` back) and gcode that carries `; filament_type` /
`; nozzle_diameter` comments (PrusaSlicer does).
