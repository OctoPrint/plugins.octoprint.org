---
layout: plugin

id: nozzlealign
title: XY Nozzle Alignment
description: Measures the XY offset between two nozzles with a camera on the bed, and writes it to the firmware with M218.
authors:
- Chris Nesbitt-Smith
license: AGPLv3

date: 2026-09-06

homepage: https://github.com/chrisns/OctoPrint-NozzleAlign
source: https://github.com/chrisns/OctoPrint-NozzleAlign
archive: https://github.com/chrisns/OctoPrint-NozzleAlign/archive/refs/heads/main.zip

tags:
- calibration
- camera
- webcam
- marlin
- snapmaker
- dual extruder

screenshots:
- url: /assets/img/plugins/nozzlealign/tab.png
  alt: The Nozzle Align tab during a run
  caption: The camera view with the detected bore, the progress log, and the result

featuredimage: /assets/img/plugins/nozzlealign/tab.png

compatibility:
  octoprint:
  - 1.8.0
  os:
  - linux
  - windows
  - macos
  - freebsd
  python: ">=3.7,<4"
---

Put a camera on the print bed looking up at the nozzles, and press one button.
The plugin homes the machine, sweeps the bed until the toolhead comes into the
picture, closes in on it, finds the nozzle bore, sweeps Z for the sharpest
view, and steers each nozzle onto the same pixel. The difference between the
two machine positions is the true offset between the nozzles. It writes the
result with `M218`, reads it back, and refuses any value the toolhead would
throw away.

Nothing about the camera is remembered between runs. Put it anywhere on the
bed and run it again.

The plugin talks only to the printer over its serial connection and to a
camera URL you supply. It uses no cloud service and collects no data.

**Safety.** The routine drives the nozzle down onto a camera that stands on
the bed. Every Z move passes one floor check, every travel move and every
tool change happens at a safe height, and a failed or stopped run parks the
head high and homes. Set the floor for your own camera mount before the first
run.
