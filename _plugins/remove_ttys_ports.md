---
layout: plugin

id: remove_ttys_ports
title: Remove /dev/ttyS* Ports (port auto detection fix)
description: Removes any matched /dev/ttyS* ports from the serial port list again and thus works around autodetection issues with 1.4.0 on systems with such ports
author: Gina Häußge
license: AGPLv3

date: 2020-03-23

homepage: https://github.com/OctoPrint/OctoPrint-Remove-ttyS-Ports
source: https://github.com/OctoPrint/OctoPrint-Remove-ttyS-Ports
archive: https://github.com/OctoPrint/OctoPrint-Remove-ttyS-Ports/archive/master.zip

tags:
- workaround
- fix
- auto detection
- autodetection
- serial port
- port

compatibility:
  octoprint:
  - ">=1.4.0,<1.4.1"

  python: ">=2.7,<4"

---

This plugin patches the internal method inside OctoPrint that creates a list of the serial ports in your system to
filter out `/dev/ttyS*` entries, which were added to the default port pattern in OctoPrint 1.4.0.

Install this plugin if you are running into issues with port auto detection no longer working on your instance which
worked flawlessly on earlier versions, especially if you have a Raspberry Pi camera or a touch screen installed (which 
appear to add a `/dev/ttyS` port to the system at least in some cases).

This is a work around for OctoPrint 1.4.0 until a generally better port auto detection solution can be released with
1.4.1, and thus currently only works with OctoPrint 1.4.0. 
