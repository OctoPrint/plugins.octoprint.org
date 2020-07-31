---
layout: plugin

id: virtual_printer2
title: Virtual Printer Settings
description: Add configurable settings to the Virtual Printer plugin under OctoPrint's settings
author: Charlie Powell
license: AGPLv3

# TODO
date: 2020-07-30

homepage: https://github.com/cp2004/OctoPrint-VirtualPrinterSettings
source: https://github.com/cp2004/OctoPrint-VirtualPrinterSettings
archive: https://github.com/cp2004/OctoPrint-VirtualPrinterSettings/archive/master.zip

tags:
- development
- settings
- virtual printer

# TODO
screenshots:
- url: /assets/img/plugins/virtual_printer2/settings.png
  alt: settings screenshot
  caption: Screenshot of the settings interface

featuredimage: /assets/img/plugins/virtual_printer_2/settings.png


compatibility:

  octoprint:
  - 1.4.1

  os:
  - linux
  - windows
  - macos
  - freebsd

  python: ">=2.7,<4"

---

Add easily configurable and well organised settings for OctoPrint's virtual printer.
Overrides the default template which only has an enabling checkbox.

Very useful if you are developing plugins, or even core OctoPrint. No more digging deep into config.yaml and hoping you typed the settings correctly!

Note that this plugin is only compatible with OctoPrint 1.4.1 and higher.