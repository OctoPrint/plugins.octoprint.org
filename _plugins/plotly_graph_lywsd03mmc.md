---
layout: plugin

id: plotly_graph_lywsd03mmc
title: OctoPrint-PlotlyGraph-LYWSD03MMC
description: Plugin to add LYWSD03MMC temperature and humidity sensor data to PlotlyTempGraph
author: yutaka551
license: MIT

date: 2026-02-22

homepage: https://github.com/yutaka551/lywsd03mmc-plotly-graph
source: https://github.com/yutaka551/lywsd03mmc-plotly-graph
archive: https://github.com/yutaka551/lywsd03mmc-plotly-graph/archive/master.zip

follow_dependency_links: false

tags:
- temperature
- humidity
- bluetooth
- sensor
- plotly

compatibility:
  octoprint:
  - 1.3.6
  python: ">=3,<4"

---

# OctoPrint-PlotlyGraph-LYWSD03MMC

OctoPrint plugin to add [LYWSD03MMC](https://www.aliexpress.com/item/4000351449649.html) (Xiaomi Mijia) Bluetooth temperature and humidity sensor data to [PlotlyTempGraph](https://github.com/jneilliii/OctoPrint-PlotlyTempGraph).

## Requirements

- [PlotlyTempGraph plugin](https://github.com/jneilliii/OctoPrint-PlotlyTempGraph)
- LYWSD03MMC Bluetooth temperature and humidity sensor
- Bluetooth support on your OctoPrint host (e.g., Raspberry Pi with built-in Bluetooth)

## Features

- Read temperature and humidity from LYWSD03MMC Bluetooth sensors
- Display sensor data in OctoPrint's temperature graph
- Configurable update interval
- Optional display of humidity and battery level
- Customizable graph labels

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.
