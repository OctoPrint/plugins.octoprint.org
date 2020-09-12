---
layout: plugin

id: klipper_python3
title: OctoKlipper3
description: A plugin for a better integration of Klipper into OctoPrint with Python 3 compatibility.
author: Stephan Weber
license: GPLv3

date: 2020-09-12

homepage: https://github.com/cowboy3d/OctoprintKlipper3Plugin
source: https://github.com/cowboy3d/OctoprintKlipper3Plugin
archive: https://github.com/cowboy3d/OctoPrintKlipper3/archive/master.zip

follow_dependency_links: false

tags:
- klipper
- python3
- firmware
- control
- monitor

screenshots:
- url: /assets/img/plugins/klipper_python3/message-log.png
  alt: Main Tab and Message Log
  caption: Main Tab and Message Log
- url: /assets/img/plugins/klipper_python3/bed-leveling.png
  alt: Assisted Bed Leveling
  caption: Assisted Bed Leveling
- url: /assets/img/plugins/klipper_python3/pid-tuning.png
  alt: PID Tuning
  caption: PID Tuning
- url: /assets/img/plugins/klipper_python3/offset.png
  alt: Coordinate Offset
  caption: Coordinate Offset
- url: /assets/img/plugins/klipper_python3/settings.png
  alt: Plugin Settings
  caption: Plugin Settings
- url: /assets/img/plugins/klipper_python3/klipper-config.png
  alt: Klipper Configuratin
  caption: Klipper Configuration
- url: /assets/img/plugins/klipper_python3/performance-graph.png
  alt: Performance Graph
  caption: Performance Graph

featuredimage: /assets/img/plugins/klipper_python3/message-log.png

compatibility:

  octoprint:
  - 1.3.8

  python: ">=2.7,<4"

---

OctoKlipper assists in configuring, controlling and monitoring the [Klipper](https://github.com/KevinOConnor/klipper) 3D-printer firmware.

It provides the following functions:

- Simplified connection dialog.
- Buttons for restarting Klippers host and MCU processes.
- User definable macro buttons that let you execute custom GCODE and Klipper commands.
- An assisted bed leveling wizard with user definable probe points to simplify manual bed leveling.
- A dialog for Klippers PID Tuning.
- A dialog to set a coordinate offset for future GCODE move commands.
- A log displaying only Klipper messages.
- A basic configuration editor to configure Klipper directly through your browser.
- A performance graph displaying key parameters extracted from the Klipper logs, helpful when debugging performance issues.

The plugin was initially developed by Martin Mühlhäuser. All I did was to enable it to run with Python 3. Currently it doesn't contain any new functionality.

#### Get Help
If you experience issues with this plugin please use the issue tracker at the plugins github linked on the right.
