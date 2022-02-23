---
layout: plugin

id: tuyasmartplug
title: OctoPrint-TuyaSmartplug
description: Plugin to control Tuya based Smartplug devices from OctoPrint web interface.
author: ziirish
license: AGPLv3

date: 2018-11-12

homepage: https://github.com/ziirish/OctoPrint-TuyaSmartplug
source: https://github.com/ziirish/OctoPrint-TuyaSmartplug
archive: https://github.com/ziirish/OctoPrint-TuyaSmartplug/archive/master.zip

follow_dependency_links: false

tags:
- Tuya
- Smartplug
- Power

featuredimage: /assets/img/plugins/TuyaSmartplug/screenshot.png

---

# Tuya Smartplug

Work based on [OctoPrint-TPLinkSmartplug](https://github.com/jneilliii/OctoPrint-TPLinkSmartplug) and [python-tuya](https://github.com/clach04/python-tuya).
This plugin controlls [Tuya-based](https://en.tuya.com/) SmartPlugs.

## Screenshots

![overview](/assets/img/plugins/TuyaSmartplug/screenshot.png)

## Settings

![settings](/assets/img/plugins/TuyaSmartplug/settings.png)

Once installed go into settings and enter the ip address for your Tuya Smartplug device. Adjust additional settings as needed.

![screenshot](/assets/img/plugins/TuyaSmartplug/plugeditor.png)

- **IP**
  - IP or hostname of plug to control.
- **Label**
  - Label to use for title attribute on hover over button in navbar.
- **Icon Class**
  - Class name from [fontawesome](http://fontawesome.io/3.2.1/cheatsheet/) to use for icon on button.
- **Device ID**
  - Plug ID.
- **Local Key**
  - Local key to cypher data.
- **Warn**
  - The left checkbox will always warn when checked.
  - The right checkbox will only warn when printer is printing.
- **GCODE**
  - When checked this will enable the processing of M80 and M81 commands from gcode to power on/off plug.  Syntax for gcode command is M80/M81 followed by hostname/ip.  For example if your plug is 192.168.1.2 your gcode command would be **M80 192.168.1.2**
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

## Preparatory work

In order to be able to interact with your Tuya smart plugs, you need to retrieve
both the `Device ID` and the `Local Key`. You'll find information to get those
in the [python-tuya wiki](https://github.com/clach04/python-tuya/wiki).
