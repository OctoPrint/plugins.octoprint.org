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
archive: https://github.com/st7ma784/infillcoder/archive/refs/heads/main.zip
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

The Plugin embeds per-layer fingerprints into 3D print infill line spacing. When a print fails, a webcam snapshot identifies the last good layer and generates a resume GCode file automatically. Includes startup bed scanning, mid-print health monitoring, and one-click resume.

#### Support my Efforts

If you like it, I would be thankful about a cup of coffee :)

[![paypal](/assets/img/plugins/bedlevelvisualizer/paypal-with-text.png)](https://www.paypal.com/donate/?business=FM3XGWAZJNGXU&no_recurring=0&currency_code=GBP)

For implementation details please visit the [homepage]({{ page.homepage | absolute_url }}).
