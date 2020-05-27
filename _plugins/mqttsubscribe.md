---
layout: plugin

id: mqttsubscribe
title: MQTT Subscribe
description: This plugin allows controlling OctoPrint via MQTT messages.
author: jneilliii
license: AGPLv3

date: 2020-05-29

homepage: https://github.com/jneilliii/OctoPrint-MQTTSubscribe
source: https://github.com/jneilliii/OctoPrint-MQTTSubscribe
archive: https://github.com/jneilliii/OctoPrint-MQTTSubscribe/archive/master.zip

follow_dependency_links: false

tags:
- MQTT
- control

compatibility:
  python: ">=2.7,<4"

---

# MQTT Subscribe

This plugin can control OctoPrint by submitting commands to the [OctoPrint REST API](http://docs.octoprint.org/en/master/api/index.html).

## Prerequisites

Install the [MQTT](https://github.com/OctoPrint/OctoPrint-MQTT) plugin via the Plugin Manager or manually using this url:

	https://github.com/OctoPrint/OctoPrint-MQTT/archive/master.zip

Once installed configure the MQTT server connection in the MQTT plugin's settings. This will be the same server that the MQTT Subscribe plugin will connect to for subscribing configured topics.

## Setup

Install via the Plugin Manager or manually using this URL:

    https://github.com/jneilliii/OctoPrint-MQTTSubscribe/archive/master.zip

## Configuration

Once both plugins are installed configure the topics/commands you want to subscribe/submit to and generate your API key.

## Settings

![settings screenshot](/assets/img/plugins/mqttsubscribe/settings.png)

### Topics
- List of configured topics
  - Click the plus button in the top right to add new topics
  - Click the pencil button to edit a configured topic
  - Click the copy button to duplicate a topic
  - Click the trash icon to delete a topic
### General
- API Key: API key to use to authenticate to the [OctoPrint REST API](http://docs.octoprint.org/en/master/api/index.html)
  - Click the plus button to generate your API key and accept the request
  - Click the trash icon to clear your API key
  - Click the copy button to copy the API key to your clipboard

## MQTT Topic Editor

![topic editor screenshot](/assets/img/plugins/mqttsubscribe/settings_topic_editor.png)

- Topic: MQTT topic to subscribe
- JSONPath Extract: JSON Path expression to extract from sent data, see [here](https://github.com/jneilliii/OctoPrint-MQTTSubscribe/issues/7#issuecomment-582166178) for an example, leave blank if substitution is not necessary in the `REST Parameters` described below
- Type: The type of REST API submission, either post or get
- REST API: The [OctoPrint REST API](http://docs.octoprint.org/en/master/api/index.html) command that you want to submit
- REST Parameters: The `JSON parameters` to submit to the REST API configured above

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii).

### Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip or become a Patron if you find this plugin helpful and want me to continue future development.

[![Patreon](/assets/img/plugins/mqttsubscribe/patreon-with-text-new.png)](https://www.patreon.com/jneilliii) [![paypal](/assets/img/plugins/mqttsubscribe/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>
