---
layout: plugin

id: filamentscale
title: MultiFilamentScale WiFi
description: Shows the remaining filament on up to five spools, weighed by a separate ESP8266 WiFi scale, in the sidebar
authors:
- Jakub Jelínek
license: AGPL-3.0-or-later

date: 2026-10-23

homepage: https://github.com/jelinj8/plugin-OctoPrint-FilamentScale
source: https://github.com/jelinj8/plugin-OctoPrint-FilamentScale
archive: https://github.com/jelinj8/plugin-OctoPrint-FilamentScale/archive/master.zip

tags:
- filament
- sidebar
- monitoring
- sensor
- esp8266
- hx711

screenshots:
- url: /assets/img/plugins/filamentscale/weights.png
  alt: Sidebar panel with five spools, their weights and the change since the last save
  caption: The sidebar shows every spool's weight and, after pressing Save, how much was used since.
- url: /assets/img/plugins/filamentscale/setup.png
  alt: Plugin settings with the scale address and a table of sensors
  caption: Settings - scale address, plus show/hide, rename, tare and set current weight for each sensor.

featuredimage: /assets/img/plugins/filamentscale/weights.png

compatibility:
  octoprint:
  - 1.11.0

  os:
  - linux
  - windows
  - macos
  - freebsd

  python: ">=3,<4"

---

Shows the weights from a [FilamentScale](https://github.com/jelinj8/firmware-FilamentScale), a WiFi scale for up to five
filament spools (ESP8266 with HX711 load cells; firmware, schematic, printed parts and build guide are in that repository),
in a slim sidebar panel.

* **Live weights** of all calibrated spools, pushed to every open browser.
* **Save / Clear** a snapshot of the weights to see how much filament a print used.
* **Settings** to show or hide each spool, rename it, tare it or set its current weight. Calibration stays in the
  scale's own web interface, which the settings page links to.

OctoPrint polls the scale's JSON API on your local network (every 2 s by default); the browser never talks to the scale
directly, so the panel also works over remote access. The plugin uses no cloud services and sends nothing to the internet.
The scale serves plain HTTP, as embedded devices on a local network usually do.
