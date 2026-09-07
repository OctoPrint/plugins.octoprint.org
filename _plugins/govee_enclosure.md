---
layout: plugin

id: govee_enclosure
title: Govee Enclosure
description: Monitor a Govee H5179/GV5179 enclosure sensor over local Bluetooth LE and add enclosure temperature to OctoPrint's native Temperature graph.
authors:
- Robert A. Wells
license: MIT

date: 2026-08-19

homepage: https://github.com/RobertAWells/OctoPrint-GoveeEnclosure
source: https://github.com/RobertAWells/OctoPrint-GoveeEnclosure
archive: https://github.com/RobertAWells/OctoPrint-GoveeEnclosure/archive/main.zip

tags:
- bluetooth
- enclosure
- govee
- humidity
- monitoring
- sensor
- temperature

screenshots:
- url: /assets/img/plugins/govee_enclosure/sidebar.png
  alt: Govee Enclosure sidebar showing temperature, humidity and battery
  caption: Live enclosure temperature, relative humidity and battery status in the OctoPrint sidebar.
- url: /assets/img/plugins/govee_enclosure/temperature-graph.png
  alt: OctoPrint Temperature graph with Actual Enclosure series
  caption: Enclosure temperature appears alongside tool and bed temperatures in OctoPrint's native graph.
featuredimage: /assets/img/plugins/govee_enclosure/temperature-graph.png

compatibility:
  octoprint:
  - ">=1.11,<2"
  os:
  - linux
  python: ">=3.9,<4"

attributes:
- ai-developed
---

**Govee Enclosure** monitors a Govee H5179/GV5179 temperature-humidity sensor locally over Bluetooth LE and adds the enclosure temperature to OctoPrint's native Temperature graph.

The plugin also provides a sidebar panel with temperature, humidity, battery level, sensor name and reading freshness. Sidebar temperature can be displayed in Celsius or Fahrenheit.

### Requirements

- Linux / Raspberry Pi OS / OctoPi with BlueZ and a powered BLE adapter
- Govee H5179/GV5179
- No Govee cloud account or API key is required

The sensor does not need to be paired. The plugin passively listens for BLE advertisements. It performs no cloud communication, analytics or tracking.

The enclosure series is monitoring-only. The plugin does not create a chamber-heater target, send `M141`, alter firmware thermal protection or modify printer safety settings.
