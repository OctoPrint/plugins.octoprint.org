---
layout: plugin
    
id: tplinksmartplug
title: OctoPrint-TPLinkSmartplug
description: Plugin to control TP-Link Smartplug devices from OctoPrint web interface.
author: jneilliii
license: AGPLv3

date: 2017-09-03
    
homepage: https://github.com/jneilliii/OctoPrint-TPLinkSmartplug
source: https://github.com/jneilliii/OctoPrint-TPLinkSmartplug
archive: https://github.com/jneilliii/OctoPrint-TPLinkSmartplug/archive/master.zip
    
follow_dependency_links: false
    
tags:
- TPLink
- TP-Link
- Smartplug
- Power

compatibility:
  python: ">=2.7,<4"

featuredimage: /assets/img/plugins/TPLinkSmartplug/screenshot_on.png

---

# TP-Link Smartplug
    
Work inspired by [OctoPrint-PSUControl](https://github.com/kantlivelong/OctoPrint-PSUControl) and [TP-Link WiFi SmartPlug Client](https://github.com/softScheck/tplink-smartplug), this plugin controls a TP-Link Smartplug via OctoPrint's nav bar. 

## Screenshots

![on](/assets/img/plugins/TPLinkSmartplug/screenshot_on.png)

![off](/assets/img/plugins/TPLinkSmartplug/screenshot_off.png)

## Settings

![screenshot](/assets/img/plugins/TPLinkSmartplug/settings.png)

Once installed go into settings and enter the ip address for your TP-Link Smartplug device. Adjust additional settings as needed.

![screenshot](/assets/img/plugins/TPLinkSmartplug/smartplug_editor.png)

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

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

### Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip or become a Patron if you find this plugin helpful and want me to continue future development.

[![Patreon](/assets/img/plugins/TPLinkSmartplug/patreon-with-text-new.png)](https://www.patreon.com/jneilliii) [![paypal](/assets/img/plugins/TPLinkSmartplug/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>

