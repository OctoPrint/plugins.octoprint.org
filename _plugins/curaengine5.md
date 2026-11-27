---
layout: plugin

id: curaengine5
title: CuraEngine 5 Slicer
description: Slice STL files with CuraEngine 5 from within OctoPrint, with a printer wizard, a profile editor, a 3D view and a layer preview. Runs on a Raspberry Pi.
authors:
- technoo10201
license: AGPL-3.0-or-later

date: 2026-11-15

homepage: https://github.com/technoo10201/OctoPrint-CuraEngine5
source: https://github.com/technoo10201/OctoPrint-CuraEngine5
archive: https://github.com/technoo10201/OctoPrint-CuraEngine5/archive/main.zip

tags:
- slicer
- cura
- curaengine
- stl
- gcode
- raspberry pi

screenshots:
- url: /assets/img/plugins/curaengine5/slicer-model.png
  alt: The Slicer tab with a model on the build plate
  caption: The Slicer tab, with the printer, the profile and the model placed on the build plate
- url: /assets/img/plugins/curaengine5/slicer-preview.png
  alt: Layer preview with supports
  caption: Layer preview after slicing, with supports
- url: /assets/img/plugins/curaengine5/profile-recommended.png
  alt: Profile settings, Recommended view
  caption: Print profile, Recommended view
- url: /assets/img/plugins/curaengine5/profile-custom.png
  alt: Profile settings, Custom view
  caption: Print profile, Custom view with all Cura settings
- url: /assets/img/plugins/curaengine5/printer-settings.png
  alt: Printer settings
  caption: Printer settings
- url: /assets/img/plugins/curaengine5/add-printer.png
  alt: Add a printer wizard
  caption: Adding a printer from Cura's catalog

featuredimage: /assets/img/plugins/curaengine5/slicer-preview.png

compatibility:
  octoprint:
  - 1.10.0
  os:
  - linux
  python: ">=3.9,<4"

attributes:
- ai-developed

---

Slices STL files with **CuraEngine 5.x** (tested with 5.11.0) directly from OctoPrint. It succeeds the CuraEngine Legacy plugin, which only supports CuraEngine 15.04.

**Unofficial project:** not affiliated with or endorsed by UltiMaker. CuraEngine is free software by UltiMaker, licensed under AGPL-3.0.

## Features

- Slicer tab with a 3D view, placement tools (move, rotate, scale, lay flat) and a layer preview that shows walls, infill and supports.
- Printer wizard based on Cura's catalog of 600+ printer definitions, and a profile editor with a simple *Recommended* view and a full *Custom* view.
- Settings are resolved the way Cura does (definitions, materials, qualities, intents, variants), checked against Cura 5.11.
- Import of Cura profiles (`.curaprofile`, `.inst.cfg`, or G-code written by Cura).
- Slicing is disabled while the printer is printing or paused.
- Progress reporting and cancellation in OctoPrint.

## Setup

Install via the bundled Plugin Manager or manually using this URL:

    https://github.com/technoo10201/OctoPrint-CuraEngine5/archive/main.zip

The plugin needs a **CuraEngine 5.x binary** and Cura's resources. On a Raspberry Pi (32-bit armhf or 64-bit aarch64) or an x86_64 Linux machine, use the **Download and install CuraEngine** button in the plugin settings: it downloads an archive from the project's GitHub release over HTTPS, checks the architecture, the glibc version and the SHA-256, and installs it into the plugin's data folder. **Nothing is downloaded unless you click that button.** You can also point the plugin to your own CuraEngine build.

Requirements: OctoPrint 1.10 or later, Python 3.9 or later, Linux with glibc 2.35 or later (for example OctoPi 1.1 / Raspberry Pi OS Bookworm). The 32-bit ARM engine requires an ARMv7 CPU (Raspberry Pi 2 and later).

## Privacy and external services

The plugin does not use any cloud service, does not collect any usage data and does not contain tracking code. The only network access is the engine download described above, started manually and made over HTTPS to GitHub.

## Sources and licenses

The plugin is licensed under AGPL-3.0-or-later. The engine archives contain CuraEngine (AGPL-3.0), Cura resources (LGPL-3.0) and Intel oneTBB (Apache-2.0), with their licenses and the location of the corresponding sources. The scripts and the small portability patch used to build the ARM engines are in the `build` folder of the repository.
