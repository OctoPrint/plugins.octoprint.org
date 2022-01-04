---
layout: plugin
id: mqtt_for_psucontrol
title: MQTT exposure for PSU Control
description: Control your PSU Control with MQTT or Home Assistant
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
  alt: Screenshot of Home Assistant MQTT device page
  caption: Screenshot of Home Assistant MQTT device page
compatibility:
  python: ">=3,<4"

---

# MQTT exposure for PSU Control
Exposes [PSU Control](https://github.com/kantlivelong/OctoPrint-PSUControl) switch on MQTT so you can access it from somewhere else. Supports Home Assistant discovery for easy setup.

This plugin does **not** connect a smart plug to PSU Control. If this is what you need , take a look at "PSU Control - MQTT" instead.

**Please check the [github repo](https://github.com/oerkel47/OctoPrint-MQTT-for-PSUcontrol) for up to date information and more details**

# Requirements:
- [MQTT plugin for OctoPrint](https://plugins.octoprint.org/plugins/mqtt/)
- [PSU Control plugin for OctoPrint](https://plugins.octoprint.org/plugins/psucontrol/)


