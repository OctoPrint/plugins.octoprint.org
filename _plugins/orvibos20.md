---
layout: plugin
    
id: orvibos20
title: OctoPrint-OrviboS20
description: Plugin to control Orvibo S20 Smart Plug from the OctoPrint web interface.
author: cprasmu
license: AGPLv3

date: 2019-10-03
    
homepage: https://github.com/cprasmu/OctoPrint-OrviboS20
source: https://github.com/cprasmu/OctoPrint-OrviboS20
archive: https://github.com/cprasmu/OctoPrint-OrviboS20/archive/master.zip
    
follow_dependency_links: false
    
tags:
- Orvibo
- S20
- Smartplug
- Power

featuredimage: /assets/img/plugins/orvibos20/power_on_dark.png

---

# Orvibo S20
    
Work inspired by [OctoPrint TP-Link WiFi SmartPlug](https://github.com/jneilliii/OctoPrint-TPLinkSmartplug) and [Orvibo](https://github.com/cherezov/orvibo), this plugin controls an Orvibo S20 smart-plug via OctoPrint's nav bar. 

## Screenshots

![on](/assets/img/plugins/orvibos20/power_on_dark.png)

![off](/assets/img/plugins/orvibos20/power_off_dark.png)

## Settings

![screenshot](/assets/img/plugins/orvibos20/settings_dark.png)

Once installed go into settings and enter the ip address for your Orvibo S20. 

![screenshot](/assets/img/plugins/orvibos20/editor_dark.png)

- **IP**
  - IP or hostname of plug to control.
- **Label**
  - Label to use for title attribute on hover over button in navbar.
- **Icon Class**
  - Class name from [fontawesome](http://fontawesome.io/3.2.1/cheatsheet/) to use for icon on button.
- **Warn**
  - The left checkbox will always warn when checked.
  - The right checkbox will only warn when printer is printing.
- **GCODE**
  - When checked this will enable the processing of M80 and M81 commands from gcode to power on/off plug.  Syntax for gcode command is M80/M81 followed by hostname/ip.  For example if your plug is 192.168.1.133 your gcode command would be **M80 192.168.1.133**
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
  

