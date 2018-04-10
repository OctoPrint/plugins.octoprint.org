---
layout: plugin

id: powerfailure
title: Power Failure Recovery
description: Recovers a print after a power failure.
author: Pablo Ventura
license: AGPLv3

date: 2017-12-24

homepage: https://github.com/pablogventura/OctoPrint-PowerFailure
source: https://github.com/pablogventura/OctoPrint-PowerFailure
archive: https://github.com/pablogventura/OctoPrint-PowerFailure/archive/master.zip

tags:
- power failure
- recovery

screenshots:
- url: /assets/img/plugins/powerfailure/settings_screenshot.png
  alt: alt-text of a screenshot
  caption: Settings

featuredimage: /assets/img/plugins/powerfailure/settings_screenshot.png


compatibility:

  octoprint:
  - 1.3.6

  os:
  - linux
  - windows
  - macos
  - freebsd

---

Recovers a print after a power failure. This plugin generates a recovery gcode from the pre-fault offset.
It can be configured to start the printing automatically with the return of the power supply or wait to user  or wait for user intervention.

![alt text](/assets/img/plugins/powerfailure/settings_screenshot.png)


