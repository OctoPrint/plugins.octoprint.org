---
layout: plugin

id: gpiocontrol
title: OctoPrint-GpioControl
description: GPIO Control adds a sidebar with on/off buttons. You can add as many buttons as you want that will control each device connected to your Raspberry Pi.
authors:
- Damian Wójcik
  license: AGPLv3
date: 2021-02-16
homepage: https://github.com/catgiggle/OctoPrint-GpioControl
source: https://github.com/catgiggle/OctoPrint-GpioControl
archive: https://github.com/catgiggle/OctoPrint-GpioControl/archive/master.zip
tags:
- raspberry pi
- gpio
- control
screenshots:
- url: /assets/img/plugins/gpiocontrol/sidebar.png
  alt: GPIO Control sidebar
  caption: GPIO Control sidebar
- url: /assets/img/plugins/gpiocontrol/settings.png
  alt: GPIO Control settings
  caption: GPIO Control settings
featuredimage: /assets/img/plugins/gpiocontrol/sidebar.png
compatibility:
octoprint:
- 1.3.0
os:
- linux
python: ">=2.7,<4"

---

# OctoPrint GPIO Control

GPIO Control adds a sidebar with on/off buttons. You can add as many buttons as you want that will control each device connected to your Raspberry Pi.

Very useful if you want to add some electronic/improvements to your printer.

![GpioControl](/assets/img/plugins/gpiocontrol/sidebar.png)
![GpioControl](/assets/img/plugins/gpiocontrol/settings.png)

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/catgiggle/OctoPrint-GpioControl/archive/master.zip

## Configuration

Just add correct GPIO configuration:
- select icon using icon picker (or typing manually) for better identification
- type name for your device connected to GPIO
- type pin number according to BCM numeration - for more details please [visit this page](https://pinout.xyz/)
- select if device is driven for low or high state of GPIO
    - _active high_ means that device is **on for high state** of GPIO and **off for low state**
    - _active low_ means that device is **on for low state** of GPIO and **off for high state**
- select if device should be on or off by default eg. after startup
