---
layout: plugin

id: alexaoctoprint
title: Alexa OctoPrint
description: Control selected OctoPrint and 3D printer actions through Alexa over the local network without a cloud backend.
authors:
- RICLAMER
license: Proprietary

date: 2026-07-16

homepage: https://github.com/RICLAMER/AlexaOctoPrint
source: https://github.com/RICLAMER/AlexaOctoPrint
archive: https://raw.githubusercontent.com/RICLAMER/AlexaOctoPrint/main/plugin/OctoPrint-AlexaOctoPrint.zip

tags:
- alexa
- automation
- control
- raspberrypi

compatibility:
  octoprint:
  - ">=1.6.0"
  os:
  - linux
  python: ">=3.7,<4"

attributes:
- ai-developed

---

Alexa OctoPrint exposes enabled printer actions as local Philips Hue compatible devices. Discovery and control stay on the LAN; no external backend, Alexa skill, account, or cloud relay is required by the plugin.

The plugin supports print control, homing and leveling, configurable Z and extrusion moves, bed and hotend temperatures, motor shutdown, guarded cancellation, configured print files, and optional OctoPrint-Enclosure outputs for printer power and lighting.

**Additional setup is required on OctoPi.** Alexa local Hue discovery expects HTTP port 80 and root Hue paths. OctoPi's existing HAProxy remains the only listener on port 80 and must selectively forward `/description.xml`, `POST /api`, and Hue light paths to the plugin on OctoPrint's internal port 5000. The project README provides a tested configuration snippet and safety instructions. The plugin does not modify system services automatically.

The Software Update hook reads the latest version from the public distribution repository and installs the matching package through OctoPrint's bundled Software Update plugin.
