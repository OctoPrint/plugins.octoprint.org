---
layout: plugin

id: tasmota
title: OctoPrint-Tasmota
description: Simple plugin to control sonoff devices that have been flashed with Tasmota.
author: jneilliii
license: AGPLv3

date: 2017-11-24

homepage: https://github.com/jneilliii/OctoPrint-Tasmota
source: https://github.com/jneilliii/OctoPrint-Tasmota
archive: https://github.com/jneilliii/OctoPrint-Tasmota/archive/master.zip

tags:
- sonoff
- tasmota
- smartplug
- power

featuredimage: /assets/img/plugins/tasmota/screenshot.png

compatibility:

  octoprint:
  - 1.2.0

  os:
  - linux
  - windows
  - macos
  - freebsd

---

# Tasmota

This plugin is to control ITead Sonoff devices that have been flashed with [Sonoff-Tasmota](https://github.com/arendst/Sonoff-Tasmota) via web calls.

## Screenshots

![screenshot](/assets/img/plugins/tasmota/screenshot.png)

## Settings

![settings](/assets/img/plugins/tasmota/settings.png)

Once installed go into settings and enter the ip address for your Tasmota device. Adjust additional settings as needed.

![settings](/assets/img/plugins/tasmota/tasmota_editor.png)

- **Device**
  - The ip or hostname of sonoff device.
- **Index**
  - Index number reprensenting the relay to control.
- **Warn**
  - The left checkbox will always warn when checked.
  - The right checkbox will only warn when printer is printing.
- **GCODE**
  - When checked this will enable the processing of M80 and M81 commands from gcode to power on/off plug.  Syntax for gcode command is M80/M81 followed by hostname/ip and index.  For example if your plug is 192.168.1.2 and index of 1 your gcode command would be **M80 192.168.1.2 1**
- **postConnect**
  - Automatically connect to printer after plug is powered on.
  - Will wait for number of seconds configured in **Auto Connect Delay** setting prior to attempting connection to printer.
- **preDisconnect**
  - Automatically disconnect printer prior to powering off the plug.
  - Will wait for number of seconds configured in **Auto Disconnect Delay** prior to powering off the plug.
- **Cmd On**
  - When checked will run system command configured in **System Command On** setting after a delay in seconds configured in **System Command On Delay**.
- **Cmd Off**
  - When checked will run system command configured in **System Command Off** setting after a delay in seconds configured in **System Command Off Delay**.
  
## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

### Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip if you find this plugin helpful.

[![paypal](/assets/img/plugins/tasmota/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>
