---
layout: plugin

id: cooldownfan
title: OctoPrint-Cooldownfan
description: Turn on the cooldown fan after prining finished
author: Farhad Malekpour
license: AGPLv3

date: 2020-07-15

homepage: https://github.com/fmalekpour/OctoPrint-Cooldownfan
source: https://github.com/fmalekpour/OctoPrint-Cooldownfan
archive: https://github.com/fmalekpour/OctoPrint-Cooldownfan/archive/master.zip

follow_dependency_links: false

tags:
- GPIO
- Cool down
- Fan
- External Fan
- Cool Down Fan


screenshots:
- url: https://github.com/fmalekpour/OctoPrint-Cooldownfan/blob/master/screenshots/cool-down-fan-config-screen.jpg?raw=true
  alt: Configuration Screen
  caption: Configuration Screen
- url: https://github.com/fmalekpour/OctoPrint-Cooldownfan/blob/master/screenshots/gpio-cooldownfan_bb.jpg?raw=true
  alt: External Fan Schematic
  caption: External Fan Schematic
- url: https://github.com/fmalekpour/OctoPrint-Cooldownfan/blob/master/screenshots/fan.jpg?raw=true
  alt: Sample cool down fan
  caption: Sample cool down fan
  



featuredimage: https://github.com/fmalekpour/OctoPrint-Cooldownfan/blob/master/screenshots/cool-down-fan-config-screen.jpg?raw=true

compatibility:
  python: ">=2.7,<4"

  octoprint:
  - 1.3.0
 
  os:
  - linux
---

#### Description

At the end of printing, I had to wait a long time for hotbed to cool down in order to remove the print. So I attached two large fan to top of the printer, connected them to a relay module and signalled it from GPIO on Raspberry Pi. This plugin controlls the relay module and turns ON the fan for defined amount of time at the end of printing.

<img src="https://github.com/fmalekpour/OctoPrint-Cooldownfan/blob/master/screenshots/gpio-cooldownfan_bb.jpg?raw=true" width="500px">

<img src="https://github.com/fmalekpour/OctoPrint-Cooldownfan/blob/master/screenshots/fan.jpg?raw=true" width="500px">


## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/fmalekpour/OctoPrint-Cooldownfan/archive/master.zip



## Configuration

In web interface, install the plugin and reload if necessary, then click on GPIO Shutdown, you will have:

- Pin Cooldown: Which Raspberry Pi GPIO pin (BCM Mode) your cooldown fan relay or mosfet is attached to.
- Run time: When printing finished, run the external cooldown fan for this amount of time.
- Normal State: State of the GPIO pin when fan is OFF.

In configuration screen, there are two buttons (Fan ON and Fan OFF) to test the fan functionality.

<img src="https://github.com/fmalekpour/OctoPrint-Cooldownfan/blob/master/screenshots/cool-down-fan-config-screen.jpg?raw=true" width="500px">

You can find the GPIO pin number assignments at [Raspberry Pi GPIO Pinout](https://www.raspberrypi.org/documentation/usage/gpio/).


#### Support me

This plugin was developed in my spare time.
If you find it useful and like it [Buy me a beer](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=WHCDYE3DCBW2Y&source=url), cheers :)
