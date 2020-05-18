---
layout: plugin

id: display_eta
title: OctoPrint-Display-ETA
description: Show finish time (ETA) for current print.
author: AlexVerrico, originally by Pablo Ventura
license: AGPLv3

date: 2017-12-19

homepage: https://github.com/AlexVerrico/Octoprint-Display-ETA
source: https://github.com/AlexVerrico/Octoprint-Display-ETA
archive: https://github.com/AlexVerrico/Octoprint-Display-ETA/archive/master.zip

tags:
- time
- eta
- finish time

screenshots:
- url: /assets/img/plugins/display_eta/screenshot.png
  alt: ETA time for current print.
  caption: ETA time for current print.

featuredimage: /assets/img/plugins/display_eta/screenshot.png


compatibility:

  octoprint:
  - 1.3.6

  os:
  - linux
  - windows
  - macos
  - freebsd

  python: ">=2.7,<4"

---

Display estimated time of finish for current print (Estimated Time of Arrival). Day of finish is displayed only when current print will not finish today.

![ETA time for current print](/assets/img/plugins/display_eta/screenshot.png)

## Setup


You must have the time zone configured on the host, otherwise you will see the time in UTC.
In Debian the following commands are made "sudo dpkg-reconfigure tzdata", then follow the wizard.
