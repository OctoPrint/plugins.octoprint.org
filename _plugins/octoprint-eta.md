---
layout: plugin

id: display-eta
title: OctoPrint-Display-ETA
description: Show finish time (ETA time) for current print.
author: Pablo Ventura
license: AGPLv3

date: 2017-12-19

homepage: https://github.com/pablogventura/Octoprint-ETA
source: https://github.com/pablogventura/Octoprint-ETA
archive: https://github.com/pablogventura/Octoprint-ETA/archive/master.zip

tags:
- time
- eta
- finish time

screenshots:
- url: /assets/img/plugins/octoprint_eta/screenshot.png
  alt: alt-text of a screenshot
  caption: ETA time for current print.

featuredimage: /assets/img/plugins/octoprint_eta/screenshot.png


compatibility:

  octoprint:
  - 1.3.6

  os:
  - linux
  - windows
  - macos
  - freebsd

---

Display estimated time of finish for current print (Estimated Time of Arrival). Day of finish is displayed only when current print will not finish today.

![alt text](/assets/img/plugins/octoprint_eta/screenshot.png)

## Setup


You must have the time zone configured on the host, otherwise you will see the time in UTC.
In Debian the following commands are made "sudo dpkg-reconfigure tzdata", then follow the wizard.
