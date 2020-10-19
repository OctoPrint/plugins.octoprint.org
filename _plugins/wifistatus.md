---
layout: plugin

id: wifistatus
title: WiFi Status
description: Displays the WiFi connection status on the OctoPrint navigation bar.
author: Manuel McLure
license: AGPLv3

date: 2020-10-08

homepage: https://github.com/ManuelMcLure/OctoPrint-WiFiStatus
source: https://github.com/ManuelMcLure/OctoPrint-WiFiStatus
archive: https://github.com/ManuelMcLure/OctoPrint-WiFiStatus/archive/master.zip
featuredimage: /assets/img/plugins/wifistatus/WiFiStatus.png

tags:
- navbar
- network
- status
- ui

screenshots:
- url: /assets/img/plugins/wifistatus/WiFiStatus.png
  alt: WiFi Status screenshot
  caption: WiFi Status screenshot

compatibility:
  os:
  - linux
  python: ">=3.7,<4"

---
This plugin will add a WiFi status indicator to the OctoPrint navigation bar to give an at-a-glance indication of the quality of the WiFi connection. Mousing over the indicator will provide more details on the connection.

This plugin will only work on Linux and if OctoPrint is running under Python 3.7 or higher. See <https://github.com/cp2004/Octoprint-Upgrade-To-Py3> if you wish to upgrade your OctoPrint installation to use Python 3.
