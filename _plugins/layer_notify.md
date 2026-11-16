---
layout: plugin

id: layer_notify
title: Layer Notify
description: Receive visual and sound alerts when specific layers are reached during printing, with optional GCODE commands per layer (e.g. M600 for filament change).
authors:
- Benaa42
license: AGPLv3

date: 2026-06-01

homepage: https://github.com/Benaa42/octoprint-layer-notify
source: https://github.com/Benaa42/octoprint-layer-notify
archive: https://github.com/Benaa42/octoprint-layer-notify/archive/main.zip

follow_dependency_links: false

tags:
- notification
- layer
- gcode
- alert
- sound
- filament change
- M600

screenshots:
- url: https://raw.githubusercontent.com/Benaa42/octoprint-layer-notify/main/docs/screenshot_settings.png
  alt: Settings panel showing layer list and sound configuration
  caption: Configure target layers with optional GCODE commands and sound alerts
- url: https://raw.githubusercontent.com/Benaa42/octoprint-layer-notify/main/docs/screenshot_tab.png
  alt: Layer Notify tab with real-time status
  caption: Dedicated tab showing which layers have fired and which are waiting

featuredimage: https://raw.githubusercontent.com/Benaa42/octoprint-layer-notify/main/docs/screenshot_tab.png

compatibility:
  python: ">=3,<4"
  octoprint:
  - 1.4.0

---

Layer Notify lets you set one or more target layers and receive an alert — visual (browser toast + OS notification) and audible (configurable sound) — the moment that layer starts printing.

Each entry can also trigger a GCODE command automatically, making it easy to pause for a filament change (`M600`), show a message on the printer display (`M117 Check print`), or run any other command at a specific point in the print.

**Features:**

- Multiple target layers, each with its own optional GCODE command
- 4 built-in sound types (single beep, triple beep, alternating alarm, rising tone)
- Adjustable volume and repeat count (1–10 times)
- Real-time status tab: see which layers have fired and which are still waiting
- Works with Cura, PrusaSlicer, SuperSlicer — and any slicer via Z-movement detection
- Each layer fires only once per print job
