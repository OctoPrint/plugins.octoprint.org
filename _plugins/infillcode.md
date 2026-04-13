---
layout: plugin

id: infillcode
title: InfillCode
description: Embeds per-layer fingerprints into 3D print infill line spacing. When a print fails, a webcam snapshot identifies the last good layer and generates a resume GCode file automatically. Includes startup bed scanning, mid-print health monitoring, and one-click resume.
author: Dr Steve Mander
license: MIT
date: 2026-04-13

homepage: https://github.com/st7ma784/infillcoder
source: https://github.com/st7ma784/infillcoder
archive: https://github.com/st7ma784/infillcoder/releases/download/v0.2.0/infillcode-0.2.0.tar.gz

tags:
- gcode
- resume
- recovery
- failure recovery
- fingerprint
- webcam
- automation
- filament runout

compatibility:
  octoprint:
  - 1.4.0
  os:
  - linux
  - windows
  - macos
  - freebsd
  python: ">=3.7"
---
