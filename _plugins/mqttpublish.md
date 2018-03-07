---
layout: plugin

id: mqttpublish
title: OctoPrint-MQTTPublish
description: Add buttons to navbar to publish messages to MQTT server.
author: jneilliii
license: AGPLv3

date: 2018-01-17

homepage: https://github.com/jneilliii/OctoPrint-MQTTPublish
source: https://github.com/jneilliii/OctoPrint-MQTTPublish
archive: https://github.com/jneilliii/OctoPrint-MQTTPublish/archive/master.zip

tags:
- MQTT
- NavBar

screenshots:
- url: /assets/img/plugins/mqttpublish/navbar.png
  alt: NavBar buttons
  caption: NavBar Buttons
- url: /assets/img/plugins/mqttpublish/settings.png
  alt: MQTTPublish Settings
  caption: MQTTPublish Settings Dialog

featuredimage: /assets/img/plugins/mqttpublish/navbar.png

---

This plugin simply adds buttons to the navbar of OctoPrint to send configured MQTT commands to the MQTT server configured in the [MQTT Plugin](https://plugins.octoprint.org/plugins/mqtt/).

## Prerequisites

Install the [MQTT](https://github.com/OctoPrint/OctoPrint-MQTT) plugin via the Plugin Manager or manually using this url:

	https://github.com/OctoPrint/OctoPrint-MQTT/archive/master.zip

## Setup

Install via the Plugin Manager or manually using this URL:

    https://github.com/jneilliii/OctoPrint-MQTTPublish/archive/master.zip

## Configuration

Once the MQTT plugin and this plugin are installed, configure the MQTT plugin for connecting to your MQTT server.  Then in this plugin's settings configure the topics/commands you want to publish to that server.

## Settings

- Topic: topic to publish command to.
- Command: comand to send to topic.
- Icon: icon class name from [fontawesome](http://fontawesome.io/3.2.1/cheatsheet/).
