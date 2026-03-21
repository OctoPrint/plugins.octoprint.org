---
layout: plugin

id: mesh_repeatability
title: Mesh Repeatability
description: Captures Marlin M420 V bed meshes after prints finish, fail, or are cancelled, then compares them against previous captures.
authors:
- jperry004
license: AGPLv3

date: 2026-03-21

homepage: https://github.com/jperry004/OctoPrint-MeshRepeatability
source: https://github.com/jperry004/OctoPrint-MeshRepeatability
archive: https://github.com/jperry004/OctoPrint-MeshRepeatability/archive/refs/heads/main.zip

tags:
- marlin
- bed leveling
- mesh
- analysis
- tab

screenshots:
- url: /assets/img/plugins/mesh_repeatability/mesh_screenshot.png
  alt: Mesh Repeatability tab showing saved captures and parsed mesh details
  caption: Mesh Repeatability capture history and mesh details

featuredimage: /assets/img/plugins/mesh_repeatability/mesh_screenshot.png

compatibility:
  octoprint:
  - ">=1.8.0"
  python: ">=3.7,<4"

---

# Mesh Repeatability

Mesh Repeatability captures the active Marlin bilinear bed mesh by sending `M420 V`
after a print completes, fails, or is cancelled. Each capture is saved as its own
JSON record and compared against the previous successful capture so you can track
how stable your printer's leveling data is over time.

## Features

- Automatic capture on `PRINT_DONE`, `PRINT_FAILED`, and `PRINT_CANCELLED`
- Manual mesh capture from the plugin tab
- Parsing of Marlin bilinear `M420 V` output, including firmware that inserts
  blank lines between rows
- Per-capture history with raw output, parsed mesh data, and delta statistics
- CSV export of saved capture history
- Automatic pruning of older records to keep the newest 50 captures

## Requirements

- OctoPrint 1.8 or newer
- Python 3.7 or newer
- Marlin firmware with bilinear mesh output available through `M420 V`

## Installation

Install through OctoPrint's Plugin Manager using:

```text
https://github.com/jperry004/OctoPrint-MeshRepeatability/archive/refs/heads/main.zip
```

## Notes

This plugin is intended for Marlin bilinear meshes. It is not designed for UBL
parsing.
