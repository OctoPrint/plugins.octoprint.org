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

# MQTT Chamber Temperature Plugin

Enables Chamber temperature reporting via subscribing to an MQTT topic.

* Requires the [MQTT](https://plugins.octoprint.org/plugins/mqtt/) Plugin to be installed and configured
* Subcribed topic configurable via Plugin Settings
* Can convert retrieved temperature to Celcius if provided in Fahrenheit
* OctoPrint must be restarted for configuration changes to take effect

## Screenshots

<img width="430" alt="Screenshot 2024-01-02 at 3 33 09 AM" src="/assets/img/plugins/mqttchambertemperature/toptemp.png">
 
<img width="986" alt="Screenshot 2024-01-02 at 3 32 49 AM" src="/assets/img/plugins/mqttchambertemperature/tempgraph.png">

<img width="979" alt="Screenshot 2024-01-02 at 3 43 44 AM" src="/assets/img/plugins/mqttchambertemperature/settings.png">