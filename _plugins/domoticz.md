---
layout: plugin

id: domoticz
title: OctoPrint-Domoticz
description: Simple plugin to control light switches via Domoticz server.
author: jneilliii
license: AGPLv3

date: 2018-07-07

homepage: https://github.com/jneilliii/OctoPrint-Domoticz
source: https://github.com/jneilliii/OctoPrint-Domoticz
archive: https://github.com/jneilliii/OctoPrint-Domoticz/archive/master.zip

tags:
- domoticz
- smartplug
- power
- switch

screenshots:
- url: /assets/img/plugins/domoticz/screenshot.png
  alt: Screenshot
  caption: Navbar screenshot
- url: /assets/img/plugins/domoticz/settings.png
  alt: Settings
  caption: Settings screenshot
- url: /assets/img/plugins/domoticz/domoticz_editor.png
  alt: Domoticz Editor
  caption: Detailed switch settings

featuredimage: /assets/img/plugins/domoticz/screenshot.png

compatibility:

  octoprint:
  - 1.2.0

  os:
  - linux
  - windows
  - macos
  - freebsd

---
This plugin is to control switches through Domoticz via web calls.

## Configuration

Once installed go into settings and enter the connection details for your Domoticz server and switch index. Adjust additional settings as needed.

## Settings Explained

- **IP:PORT**
  - The ip and port of Domoticz server.
- **Index**
  - Index number reprensenting the switch to control.
- **Icon**
  - Icon class name from the [fontawesome](https://fontawesome.com/v3.2.1/icons/) library.
- **Label**
  - Title attribute on icon that shows on mouseover.
- **Username**
  - Username used to connect to web interface. If authentication is not configured on your Domoticz server leave this blank.
- **Password**
  - Password used to connect to web interface. If authentication is not configured on your Domoticz server leave this blank.
- **Warn**
  - The left checkbox will always warn when checked.
  - The right checkbox will only warn when printer is printing.
- **GCODE**
  - When checked this will enable the processing of M80 and M81 commands from gcode to power on/off switch.  Syntax for gcode command is M80/M81 followed by IP:PORT and index.  For example if your Domoticz server is 192.168.1.2:8080 and switch index is 1 your gcode command would be **M80 192.168.1.2:8080 1**
- **postConnect**
  - Automatically connect to printer after switch is powered on.
  - Will wait for number of seconds configured in **Auto Connect Delay** setting prior to attempting connection to printer.
- **preDisconnect**
  - Automatically disconnect printer prior to powering off the switch.
  - Will wait for number of seconds configured in **Auto Disconnect Delay** prior to powering off the switch.
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

[![paypal](/assets/img/plugins/domoticz/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>
