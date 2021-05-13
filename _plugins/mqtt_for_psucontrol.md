---
layout: plugin
id: mqtt_for_psucontrol
title: MQTT for PSU Control
description: Use MQTT and/or Home Assistant to control the switch you use with the PSU Control plugin.
archive: https://github.com/oerkel47/OctoPrint-MQTT-for-PSUcontrol/archive/main.zip
homepage: https://github.com/oerkel47/OctoPrint-MQTT-for-PSUcontrol
source: https://github.com/oerkel47/OctoPrint-MQTT-for-PSUcontrol
author: oerkel47
license: AGPLv3
featuredimage: /assets/img/plugins/mqtt_for_psucontrol/screenshot_settings.PNG
date: 2021-05-12
tags:
- Home Assistant
- control
- psucontrol
- mqtt
screenshots:
- url: /assets/img/plugins/mqtt_for_psucontrol/screenshot_settings.PNG
  alt: Screenshot of plugin settings page
  caption: Screenshot of plugin settings page
- url: /assets/img/plugins/mqtt_for_psucontrol/screenshot_HomeAssistant.PNG
  alt: Screenshot of Home Assistant MQTT device
  caption: Screenshot of Home Assistant MQTT device page
compatibility:
  python: ">=3,<4"

---

# MQTT for PSU Control
This plugin interfaces between [PSU Control](https://github.com/kantlivelong/OctoPrint-PSUControl) plugin and [MQTT](https://github.com/OctoPrint/OctoPrint-MQTT) plugin and adds support for [Home Assistant](https://www.home-assistant.io) discovery. 

For more information please visit the [homepage](https://github.com/oerkel47/OctoPrint-MQTT-for-PSUcontrol).

## What it does
- Let's you control and monitor the switch that is configured in PSU Control via the MQTT protocol.
- Supports Home Assistant discovery to integrate everything easily.

## What you need
 - configured and running [MQTT](https://github.com/OctoPrint/OctoPrint-MQTT) plugin for OctoPrint
 - [PSU Control](https://github.com/kantlivelong/OctoPrint-PSUControl) plugin for OctoPrint
 - optional: [Home Assistant](https://www.home-assistant.io)
