---
layout: plugin

id: TemperatureFailsafe
title: TemperatureFailsafe
description: Execute shell commands when temperatures violate thresholds
author: Uriah Welcome
license: Apache 2

date: 2017-04-14

homepage: https://github.com/google/OctoPrint-TemperatureFailsafe
source: https://github.com/google/OctoPrint-TemperatureFailsafe
archive: https://github.com/google/OctoPrint-TemperatureFailsafe/archive/master.zip

follow_dependency_links: false

tags:
- raspberry pi
- temperature
screenshots:
- url: /assets/img/plugins/temperaturefailsafe/configuration.png
  alt: Configuration Screen
  caption: Configure Failsafes

compatibility:
  octoprint:
  - 1.3.1
  os:
  - linux
  python: ">=2.7,<4"
---

OctoPrint Plugin that executes shell commands on temperature violations.
