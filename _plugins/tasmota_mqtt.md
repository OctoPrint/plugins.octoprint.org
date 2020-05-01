---
layout: plugin

id: tasmota_mqtt
title: OctoPrint-TasmotaMQTT
description: Plugin to control Tasmota devices via MQTT protocol.
author: jneilliii
license: AGPLv3

date: 2018-01-17

homepage: https://github.com/jneilliii/OctoPrint-TasmotaMQTT
source: https://github.com/jneilliii/OctoPrint-TasmotaMQTT
archive: https://github.com/jneilliii/OctoPrint-TasmotaMQTT/archive/master.zip

follow_dependency_links: false

tags:
- tasmota
- mqtt
- power

compatibility:
  python: ">=2.7,<4"

featuredimage: /assets/img/plugins/tasmota_mqtt/navbar.png

---

# Tasmota-MQTT

This plugin allows the control of [Tasmota](https://github.com/arendst/Sonoff-Tasmota) devices from within OctoPrint via [MQTT](https://github.com/arendst/Sonoff-Tasmota/wiki/MQTT-Overview#mqtt-overview) commands.

## Screenshots

![screenshot](/assets/img/plugins/tasmota_mqtt/navbar.png)

## Prerequisites

Install the [MQTT](https://github.com/OctoPrint/OctoPrint-MQTT) plugin via the Plugin Manager or manually using this url:

	https://github.com/OctoPrint/OctoPrint-MQTT/archive/master.zip
	
## Settings

![settings](/assets/img/plugins/tasmota_mqtt/settings.png)

![settings](/assets/img/plugins/tasmota_mqtt/relay_editor.png)

- Set the Full Topic settings to match your tasmota settings.
- Use the Tasmota device's topic in the Tasmota-MQTT Plugin settings for the individual relays.
- For multiple relay devices enter the index number that matches your desired relay.
- For single relay devices like the [iTead Sonoff S20 Smart Socket](https://www.itead.cc/smart-socket.html), leave Relay # blank.

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

### Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip if you find this plugin helpful.

[![paypal](/assets/img/plugins/tasmota_mqtt/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>