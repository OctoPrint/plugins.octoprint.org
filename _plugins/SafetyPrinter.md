---
layout: plugin

id: SafetyPrinter
title: Safety Printer
description: This plugin interfaces with Safety Printer MCU to improve your printer's safety. 
authors:
- Rodrigo C. C. Silva
license: AGPLv3

date: 2021-08-30

homepage: https://github.com/SinisterRj/SafetyPrinter/wiki
source: https://github.com/SinisterRj/Octoprint_SafetyPrinter
archive: https://github.com/SinisterRj/Octoprint_SafetyPrinter/archive/refs/heads/main.zip

tags:
- fire
- smoke
- notification
- bed temperature
- hotend temperature
- safety
- flame detector
- emergency
- shutdown
- trip

screenshots:
- url: /assets/img/plugins/SafetyPrinter/Plugin1.PNG
  alt: Sidebar1
  caption: Sensor information sidebar in normal operation.
- url: /assets/img/plugins/SafetyPrinter/Plugin2.PNG
  alt: Sidebar2
  caption: Sensor information sidebar in shutdown mode.
- url: /assets/img/plugins/SafetyPrinter/Plugin3.PNG
  alt: Setup
  caption: Setup options.
- url: /assets/img/plugins/SafetyPrinter/Plugin4.PNG
  alt: Terminal
  caption: Terminal (advanced users).

featuredimage: /assets/img/plugins/SafetyPrinter/icon.PNG

compatibility:

  os:
  - linux
  - windows

  python: ">=2.7,<3"

---

# Safety Printer

This plugin interfaces with [Safety Printer MCU](https://github.com/SinisterRj/SafetyPrinter) to improve your printer's safety. You can find more information on [Wiki](https://github.com/SinisterRj/SafetyPrinter/wiki).

P.S.: It also integrates with [Octopod](https://plugins.octoprint.org/plugins/octopod/) notifications, so is highly recommended its installation.

With this plugin you will be able to setup, supervise and trobleshoot your Safety Printer MCU. It provides: Sidebar sensor monitoring, Plugin and Sensor setup and Safety Printer MCU communications terminal (for advanced users).

### Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's source page linked on the right.

### Join the project

If you think that you can contribute with the project, join us, send me a message: [SinisteRrj](https://community.octoprint.org/u/sinisterrj/summary)
