---
layout: plugin

id: moonraker_connector
title: Moonraker Connector
description: Connector plugin to allow connecting to Moonraker enabled Klipper based printers
authors:
    - Gina Häußge
license: AGPL-3.0-or-later

date: 2026-11-16

homepage: https://github.com/OctoPrint/OctoPrint-MoonrakerConnector
source: https://github.com/OctoPrint/OctoPrint-MoonrakerConnector
archive: https://github.com/OctoPrint/OctoPrint-MoonrakerConnector/archive/main.zip

tags:
    - connector
    - moonraker
    - klipper

screenshots:
    - url: /assets/img/plugins/moonraker_connector/screenshot.png
      alt: Screenshot of connection and control panel with an ongoing connection to a Klipper/Moonraker based printer via the connector
      caption: Screenshot of connection and control panel with an ongoing connection to a Klipper/Moonraker based printer via the connector

featuredimage: /assets/img/plugins/moonraker_connector/screenshot.png

compatibility:
    octoprint:
        - 2.0.0
    python: ">=3.9,<4"

attributes:
#  - cloud  # if your plugin requires access to a cloud to function
#  - commercial  # if your plugin has a commercial aspect to it
#  - free-tier  # if your plugin has a free tier
---

Connector plugin to allow connecting to Moonraker enabled Klipper based printers.

Supports connecting, print start & monitoring, file management, macro access, webcam access.

Successfully tested against:
- Qidi Q1 Pro
- Snapmaker U1

This is still a work in progress, please report back any issues or successful tests
at [the plugin's issue tracker](https://github.com/OctoPrint/OctoPrint-MoonrakerConnector/issues).
