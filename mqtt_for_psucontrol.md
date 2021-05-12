---
layout: plugin
id: mqtt_for_psucontrol
title: MQTT for PSU Control
description: Use MQTT and/or HomeAssistant to control the switch you use with the PSU Control plugin
archive: https://github.com/oerkel47/OctoPrint-MQTT-for-PSUcontrol/archive/main.zip
homepage: https://github.com/oerkel47/OctoPrint-MQTT-for-PSUcontrol
source: https://github.com/oerkel47/OctoPrint-MQTT-for-PSUcontrol
author: oerkel47
license: AGPLv3
featuredimage: https://github.com/oerkel47/OctoPrint-MQTT-for-PSUcontrol/blob/main/screenshot_settings.PNG
date: 2021-05-12
tags:
- Home Assistant
- control
- psucontrol
- mqtt
screenshots:
- url: https://github.com/oerkel47/OctoPrint-MQTT-for-PSUcontrol/blob/main/screenshot_HomeAssistant.PNG
  alt: Screenshot from Home Assistant device
  caption: Screenshot from Home Assistant device
compatibility:
  python: ">=3,<4"

---

This plugin interfaces between [PSUControl](https://github.com/kantlivelong/OctoPrint-PSUControl) plugin and [MQTT](https://github.com/OctoPrint/OctoPrint-MQTT) plugin and adds support for [HomeAssistant](https://www.home-assistant.io) discovery. 

# What it does
- Let's you control and monitor the switch that is configured in PSUControl via the MQTT protocol.
- Supports HomeAssistant discovery to integrate everything without hassle.

# What you need
 - configured and running MQTT plugin for OctoPrint
 - PSU Control plugin for OctoPrint
 - optional: Home Assistant
