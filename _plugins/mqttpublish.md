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

compatibility:
  python: ">=2.7,<4"

featuredimage: /assets/img/plugins/mqttpublish/navbar.png

---

# MQTT Publish

This plugin simply adds buttons to the navbar of OctoPrint to send configured MQTT commands to the MQTT server configured in the [MQTT Plugin](https://plugins.octoprint.org/plugins/mqtt/).

## Screenshots

![screenshot](/assets/img/plugins/mqttpublish/navbar.png)

## Prerequisites

Install the [MQTT](https://github.com/OctoPrint/OctoPrint-MQTT) plugin via the Plugin Manager or manually using this url:

	https://github.com/OctoPrint/OctoPrint-MQTT/archive/master.zip

## Settings

![settings](/assets/img/plugins/mqttpublish/settings.png)

Once the MQTT plugin and this plugin are installed, configure the MQTT plugin for connecting to your MQTT server.  Then in this plugin's settings configure the topics/commands you want to publish to that server.

- Topic: topic to publish command to.
- Command: comand to send to topic.
- Icon: icon class name from [fontawesome](http://fontawesome.io/3.2.1/cheatsheet/).

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

### Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip if you find this plugin helpful.

[![paypal](/assets/img/plugins/mqttpublish/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>
