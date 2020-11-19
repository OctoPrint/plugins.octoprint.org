---
layout: plugin

id: klipper
title: OctoKlipper
description: A plugin for a better integration of Klipper into OctoPrint.
author: Alice Weigt
license: AGPLv3

date: 2018-08-21

homepage: https://github.com/AliceGrey/OctoprintKlipperPlugin
source: https://github.com/AliceGrey/OctoprintKlipperPlugin
archive: https://github.com/AliceGrey/OctoprintKlipperPlugin/archive/master.zip

follow_dependency_links: false

tags:
- klipper
- firmware
- control
- monitor

screenshots:
- url: /assets/img/plugins/klipper/message-log.png
  alt: Main Tab and Message Log
  caption: Main Tab and Message Log
- url: /assets/img/plugins/klipper/bed-leveling.png
  alt: Assisted Bed Leveling
  caption: Assisted Bed Leveling
- url: /assets/img/plugins/klipper/pid-tuning.png
  alt: PID Tuning
  caption: PID Tuning
- url: /assets/img/plugins/klipper/offset.png
  alt: Coordinate Offset
  caption: Coordinate Offset
- url: /assets/img/plugins/klipper/settings.png
  alt: Plugin Settings
  caption: Plugin Settings
- url: /assets/img/plugins/klipper/klipper-config.png
  alt: Klipper Configuratin
  caption: Klipper Configuration
- url: /assets/img/plugins/klipper/performance-graph.png
  alt: Performance Graph
  caption: Performance Graph

featuredimage: /assets/img/plugins/klipper/message-log.png

compatibility:

  octoprint:
  - 1.3.8

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

#### Get Help
If you experience issues with this plugin please use the issue tracker at the plugins github linked on the right.
