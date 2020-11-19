---
layout: plugin

id: wemoswitch
title: OctoPrint-WemoSwitch
description: Plugin to control Belkin Wemo devices from OctoPrint web interface.
author: jneilliii
license: AGPLv3

date: 2018-09-18

homepage: https://github.com/jneilliii/OctoPrint-WemoSwitch
source: https://github.com/jneilliii/OctoPrint-WemoSwitch
archive: https://github.com/jneilliii/OctoPrint-WemoSwitch/archive/master.zip

follow_dependency_links: false

tags:
- Belkin
- Wemo
- Smartplug
- Power

compatibility:
  python: ">=2.7,<4"

featuredimage: /assets/img/plugins/wemoswitch/screenshot_on.png

---

# Wemo Switch

This plugin allows for the control of Belkin Wemo devices via navbar buttons and gcode commands.

## Screenshots

![on](/assets/img/plugins/wemoswitch/screenshot_on.png)

![off](/assets/img/plugins/wemoswitch/screenshot_off.png)

## Settings

![screenshot](/assets/img/plugins/wemoswitch/settings.png)

Once installed go into settings and enter the name of your wemo device. Adjust additional settings as needed.

![screenshot](/assets/img/plugins/wemoswitch/settings_wemo_editor.png)

- **Device Name**
  - Name configured in the Wemo App associated with the plug.
- **Label**
  - Label to use for title attribute on hover over button in navbar.
- **Icon Class**
  - Class name from [fontawesome](http://fontawesome.io/3.2.1/cheatsheet/) to use for icon on button.
- **Warn**
  - The left checkbox will always warn when checked.
  - The right checkbox will only warn when printer is printing.
- **GCODE**
  - When checked this will enable the processing of M80 and M81 commands from gcode to power on/off plug.  Syntax for gcode command is M80/M81 followed by device name.  For example if your plug is `living_room` your gcode command would be **M80 living_room**
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

[![Patreon](/assets/img/plugins/wemoswitch/patreon-with-text-new.png)](https://www.patreon.com/jneilliii) [![paypal](/assets/img/plugins/wemoswitch/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>
