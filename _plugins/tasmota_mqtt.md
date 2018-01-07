---
layout: plugin

id: tasmota_mqtt
title: OctoPrint-TasmotaMQTT
description: Plugin to control Tasmota devices via MQTT protocol.
author: jneilliii
license: AGPLv3

date: 2018-01-06

homepage: https://github.com/jneilliii/OctoPrint-TasmotaMQTT
source: https://github.com/jneilliii/OctoPrint-TasmotaMQTT
archive: https://github.com/jneilliii/OctoPrint-TasmotaMQTT/archive/master.zip

follow_dependency_links: false

tags:
- tasmota
- mqtt
- power

screenshots:
- url: /assets/img/plugins/tasmota-mqtt/navbar.png
  alt: Navbar
  caption: Buttons on navigation bar
- url: /assets/img/plugins/tasmota-mqtt/settings.png
  alt: Settings
  caption: Tasmota-MQTT Settings
- url: /assets/img/plugins/tasmota-mqtt/relay_editor.png
  alt: Relay Editor
  caption: Tasmota-MQTT Relay Editor

featuredimage: /assets/img/plugins/tasmota-mqtt/navbar.png

---

This plugin allows the control of [Tasmota](https://github.com/arendst/Sonoff-Tasmota) devices from within OctoPrint via [MQTT](https://github.com/arendst/Sonoff-Tasmota/wiki/MQTT-Overview#mqtt-overview) commands.

## Prerequisites

Install the [MQTT](https://github.com/OctoPrint/OctoPrint-MQTT) plugin via the Plugin Manager or manually using this url:

	https://github.com/OctoPrint/OctoPrint-MQTT/archive/master.zip
	
## Setup

Install via the Plugin Manager or manually using this URL:

    https://github.com/jneilliii/OctoPrint-TasmotaMQTT/archive/master.zip

## Configuration

- Once installed your Tasmota devices will need to have the FullTopic configured as **%topic%/%prefix%/**
- Use the Tasmota device's topic in the Tasmota-MQTT Plugin settings for the individual relays.
- For multiple relay devices enter the index number that matches your desired relay.
- For single relay devices like the [iTead Sonoff S20 Smart Socket](https://www.itead.cc/smart-socket.html), leave Relay # blank.
