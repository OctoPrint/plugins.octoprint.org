---
layout: plugin

id: navbarclock
title: Navbar Clock
description: Displays the current time on the OctoPrint navigation bar
author: Manuel McLure
license: AGPLv3

date: 2021-06-01

homepage: https://github.com/ManuelMcLure/OctoPrint-NavbarClock
source: https://github.com/ManuelMcLure/OctoPrint-NavbarClock
archive: https://github.com/ManuelMcLure/OctoPrint-NavbarClock/archive/main.zip
featuredimage: /assets/img/plugins/navbarclock/NavbarClock.png

tags:
- navbar
- ui

screenshots:
- url: /assets/img/plugins/navbarclock/NavbarClock.png
  alt: Navbar Clock screenshot
  caption: Navbar Clock screenshot

compatibility:
  python: ">=3.7,<4"

---
This plugin will add a clock to the navigation bar. The time displayed may be the server time (default), browser time or UTC. Both 24 hour and AM/PM formats are supported, and display of seconds is optional.

This plugin will only work if OctoPrint is running under Python 3.7 or higher. See <https://github.com/cp2004/Octoprint-Upgrade-To-Py3> if you wish to upgrade your OctoPrint installation to use Python 3.
