---
layout: plugin

id: malyan_connection_fix
title: Malyan/Monoprice Connection Fix
description: Fixes connection issues with Malyan/Monoprice printers
author: Gina Häußge
license: AGPLv3

date: 2018-02-07

homepage: https://github.com/OctoPrint/OctoPrint-MalyanConnectionFix
source: https://github.com/OctoPrint/OctoPrint-MalyanConnectionFix
archive: https://github.com/OctoPrint/OctoPrint-MalyanConnectionFix/archive/master.zip

tags:
- monoprice
- monoprice select mini
- monoprice mini delta
- malyan
- malyan m100
- malyan m200
- turnigy
- turnigy fabrikator 2
- turnigy fabrikator ii
- connection
- fix

compatibility:

  octoprint:
  - 1.3.6

  os:
  - linux
  - macos
  - freebsd

---

Due to some weird issue with some Malyan/Monoprice printers, the initial connection to the printer via the 
Connect button may fail. Only the second connection succeeds. 

This plugin is supposed to fix this by invoking a specific serial port opening sequence that has been found
to solve this problem. Note that due to the nature of this sequence this fix can't work for OctoPrint installations
on Windows and is therefore not supported for that OS. 

Printer models known to be affected by this and confirmed as issues resolved with this fix:

  * Turnigy Fabrikator II Mini (Malyan M100)
  * Monoprice Select Mini (Malyan M200)
  * Monoprice Mini Delta (Malyan ?)

For more details please refer to [this ticket on the OctoPrint issue tracker](https://github.com/foosel/OctoPrint/issues/2271).

