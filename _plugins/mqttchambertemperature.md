---
layout: plugin

id: mqttchambertemperature
title: MQTT Chamber Temperature
description: Enables Chamber temperature reporting via subscribing to an MQTT topic
authors:
- Shell M. Shrader
license: WTFPL

date: 2024-01-02

homepage: https://github.com/synman/OctoPrint-MqttChamberTemperature
source: https://github.com/synman/OctoPrint-MqttChamberTemperature
archive: https://github.com/synman/OctoPrint-MqttChamberTemperature/archive/master.zip

tags:
- administration
- ui
- chamber
- temperature
- mqtt

compatibility:
  octoprint:
  - 1.3.0
  os:
  - linux
  - windows
  python: ">=2.7,<4"

featuredimage: /assets/img/plugins/mqttchambertemperature/toptemp.png

---

## MQTT Chamber Temperature Plugin for Octoprint
 
* Requires the [MQTT](https://plugins.octoprint.org/plugins/mqtt/) Plugin to be installed and configured
* Subcribed topic configurable via Plugin Settings
* Can convert retrieved temperature to Celcius if provided in Fahrenheit
* Control enclosure temperature via MQTT state topics

## Screenshots

<img width="430" alt="Top Temp" src="/assets/img/plugins/mqttchambertemperature/toptemp.png">
 
<img width="986" alt="Plotly Temperature Graph" src="/assets/img/plugins/mqttchambertemperature/tempgraph.png">

<img width="979" alt="Plugin Settings" src="/assets/img/plugins/mqttchambertemperature/settings.png">

## Temperature Sensor Ideas

* ESP8266/ESP32 BME280 - https://github.com/synman/BME280
* ESP8266/ESP32 SHT30 & LCD - https://github.com/synman/SHT-Sensor

## Heater and Power Plug Reference

The easiest way to manage temperature control is by use of a [miniature heater](https://www.amazon.com/dp/B07573FKSG) connected to a Home Assistant integrated power plug such as the [TP-LINK HS103](https://www.tp-link.com/us/home-networking/smart-plug/hs103/).  Creating automations for managing the requested and actual power state values via MQTT is then fairly trivial.