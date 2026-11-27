---
layout: plugin
id: mqttforusbrelaycontrol
title: MQTT for USB Relay Control
description: Expose USB Relay Control channels to Home Assistant through OctoPrint-MQTT
author: Eitschman
license: AGPL-3.0-or-later
date: 2026-11-27
homepage: https://github.com/Eitschman/OctoPrint-MQTTForUSBRelayControl
source: https://github.com/Eitschman/OctoPrint-MQTTForUSBRelayControl
archive: https://github.com/Eitschman/OctoPrint-MQTTForUSBRelayControl/archive/refs/tags/0.1.0.zip
featuredimage: /assets/img/plugins/mqttforusbrelaycontrol/settings-light.png
screenshots:
  - url: /assets/img/plugins/mqttforusbrelaycontrol/settings-light.png
    alt: English settings in a light host theme
    caption: English settings in a light host theme
  - url: /assets/img/plugins/mqttforusbrelaycontrol/settings-dark.png
    alt: English settings in a dark host theme
    caption: English settings in a dark host theme
  - url: /assets/img/plugins/mqttforusbrelaycontrol/settings-german.png
    alt: German settings
    caption: German settings
  - url: /assets/img/plugins/mqttforusbrelaycontrol/settings-compact.png
    alt: Compact settings layout
    caption: Compact settings layout
  - url: /assets/img/plugins/mqttforusbrelaycontrol/diagnostics.png
    alt: Runtime and dependency diagnostics
    caption: Runtime and dependency diagnostics
  - url: /assets/img/plugins/mqttforusbrelaycontrol/ha-device.png
    alt: Synthetic Home Assistant device and relay control
    caption: Synthetic Home Assistant device and relay control
  - url: /assets/img/plugins/mqttforusbrelaycontrol/ha-entities.png
    alt: Synthetic Home Assistant entity listing
    caption: Synthetic Home Assistant entity listing
attributes:
  - ai-developed
tags:
  - mqtt
  - relay
  - homeassistant
compatibility:
  python: ">=3.11"
  octoprint:
    - ">=1.11.2"
  os:
    - linux
---

<!-- Registration draft. Verify the approved stable archive URL, actual registration
date and complete screenshot bundle before submitting this file. -->

Expose USB Relay Control channels as Home Assistant MQTT switches, lights or fans.
All three entity types provide binary on/off control.

Requires Python 3.11 or later, USB Relay Control 1.0.0 and OctoPrint-MQTT 0.8.19
or 0.8.20. Configure the relay hardware and MQTT connection in those plugins first.
The companion reuses their existing relay objects and MQTT connection. It installs
no USB driver, creates no additional MQTT connection and changes no foreign settings.
Enable the existing MQTT plugin's Last Will before enabling the integration.

A broker connection is required for MQTT commands and discovery. An unavailable
broker disables companion communication without stopping OctoPrint. Configure
broker authentication, topic permissions and TLS in OctoPrint-MQTT for your network;
use TLS with certificate verification for a remote broker. This companion does not
read or store broker credentials and sends no tracking or analytics.

The owner confirms human review and successful installation and testing on real
hardware. Screenshots show isolated synthetic data. Automated tests use
synthetic hardware and loopback services; they do not certify a hardware model.

See the [installation guide](https://github.com/Eitschman/OctoPrint-MQTTForUSBRelayControl/blob/main/docs/public/installation.md),
[German instructions](https://github.com/Eitschman/OctoPrint-MQTTForUSBRelayControl/blob/main/docs/public/installation-de.md)
and [dependency review](https://github.com/Eitschman/OctoPrint-MQTTForUSBRelayControl/blob/main/docs/public/dependency-review.md).
