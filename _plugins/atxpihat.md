---
layout: plugin

id: atxpihat
title: ATXPiHat
description: Software support for the ATXPiHat
author: Brian Anichowski
license: Creative Commons

# today's date in format YYYY-MM-DD, e.g.
date: 2018-01-25

homepage: https://www.baprojectworkshop.com
source: https://github.com/banichow/OctoPrint-Atxpihat
archive: https://github.com/banichow/OctoPrint-Atxpihat/archive/master.zip

follow_dependency_links: true

tags:
- psu
- led
- emergency
- atx
- fan
- monitor
- epo 
- control

screenshots:
- url: /assets/img/plugins/atxpihat/screenshot1.png
- url: /assets/img/plugins/atxpihat/board1.jpg
- url: /assets/img/plugins/atxpihat/screenshot2.png
- url: /assets/img/plugins/atxpihat/screenshot3.png

featuredimage: /assets/img/plugins/atxpihat/screenshot2.png

compatibility:
   octoprint: 
   - 1.3.6
   os:
   - linux

---

## Software support for the ATXPiHat expansion board.

Read all about this board and it's usage at [baprojectworkshop.com](https://wp.me/p98gmw-7g). The installation instructions are located on [my Github site](https://github.com/banichow/OctoPrint-Atxpihat). **These need to be reviewed prior to installation of the plugin**


* Fully compatible with Octoprint 1.3.6 or greater.
* Directly power the Raspberry Pi 3B, no more external power source.
* ATX 24 Molex connector, no more cutting up the supply cables
* Amperage support to handle 19 amps at 12v for heat bed and hot end
* Screw connectors make easy connection to the main board, External Mosfet, etc
* Direct 12v RGB LED support, can also be controlled by GCODE
* Emergency power off (EPO)
* Power On/Off monitoring
* Visual indicator of the 12v supply being active and powering the external devices
* 12v monitored (RPM) cooling fan port
* Upon fan failure it can be configured to automatically shuts the printer down
* Auxiliary 5v support for external powered items
* Monitoring of the 12v rail, for amperage and voltage
* Automatic shutdown when an amperage threshold is reached. Meltdown protection
* Switchable 12 or 5 v connector for controlling external items via GCODE



