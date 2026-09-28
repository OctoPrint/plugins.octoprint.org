---
layout: plugin

id: knomi
title: KNOMI
description: Drive the BigTreeTech KNOMI / KNOMI 2 round display from OctoPrint. Status, homing/QGL/mesh/pause animations and an optional Bluetooth LE link, no Moonraker needed.
authors:
- Binnacle-Tech
license: AGPLv3

date: 2026-09-28

homepage: https://github.com/Binnacle-Tech/OctoPrint-KNOMI
source: https://github.com/Binnacle-Tech/OctoPrint-KNOMI
archive: https://github.com/Binnacle-Tech/OctoPrint-KNOMI/archive/main.zip

tags:
- knomi
- bigtreetech
- btt
- klipper
- display
- lcd
- touchscreen
- status
- ui
- wifi
- voron
- stealthburner
- bluetooth
- animation

compatibility:
  octoprint:
  - 1.9.0

  os:
  - posix

  python: ">=3.8,<4"

attributes:
- ai-developed

screenshots:
- url: /assets/img/plugins/knomi/knomi-screens.png
  alt: KNOMI 2 screens driven by OctoPrint
  caption: The KNOMI showing idle, homing, printing (time left, temps, Z) and a UI-color tinted face
- url: /assets/img/plugins/knomi/octoprint-settings.png
  alt: OctoPrint-KNOMI settings
  caption: Plugin settings. Tool, and the optional Bluetooth link to the KNOMI
- url: /assets/img/plugins/knomi/knomi-animations.png
  alt: KNOMI custom animation page
  caption: The KNOMI firmware's page for uploading custom GIFs per animation state

featuredimage: /assets/img/plugins/knomi/knomi-screens.png
---

Companion plugin for the **[KNOMI for OctoPrint firmware](https://github.com/Binnacle-Tech/KNOMI)**, a fork of BigTreeTech's KNOMI firmware that adds an OctoPrint backend. Together they let the KNOMI / KNOMI 2 display (the round Voron Stealthburner screen) work with OctoPrint, including OctoPrint + Klipper (OctoKlipper) setups, without running Moonraker or Mainsail.

**Only tested on a KNOMI 2 with OctoPrint on a Raspberry Pi 5.**

## Features

- **Animations for what the printer is doing:** homing, probing / bed mesh, QGL, input shaper, PID tuning, nozzle cleaning, filament load/unload and pause. The plugin raises these from:
  - commands OctoPrint sends (G28, QUAD_GANTRY_LEVEL, BED_MESH_CALIBRATE, M109/M190, SHAPER_CALIBRATE, PAUSE/M600, and so on), cleared on their `ok`
  - `// KNOMI <flag>=1` lines from Klipper macros, so steps inside PRINT_START show up too
  - `// action:paused` / `// action:resumed` lines
- **Instant updates.** Status is pushed to the KNOMI over OctoPrint's websocket. Also available at `GET /api/plugin/knomi`.
- **Optional Bluetooth LE link** to the KNOMI 2. It pushes status and the file list, and runs the KNOMI's buttons inside OctoPrint without an API key. The KNOMI can keep its WiFi off while the link is up.

## Requirements

- A KNOMI running the [KNOMI for OctoPrint firmware](https://github.com/Binnacle-Tech/KNOMI) with its backend set to OctoPrint
- For Bluetooth: a Pi with Bluetooth enabled and BlueZ, and a one-time `bluetoothctl` pairing (the KNOMI shows the code). Installs [bleak](https://github.com/hbldh/bleak).

## Setup

See the [README](https://github.com/Binnacle-Tech/OctoPrint-KNOMI#readme) and the firmware's [setup guide](https://github.com/Binnacle-Tech/KNOMI/blob/octoprint/OCTOPRINT.md).
