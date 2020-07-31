---
layout: plugin

id: vp_settings
title: Virtual Printer Settings
description: Add configurable settings to the Virtual Printer plugin under OctoPrint's settings
author: Charlie Powell
license: AGPLv3

date: 2020-07-30

homepage: https://github.com/cp2004/OctoPrint-VirtualPrinterSettings
source: https://github.com/cp2004/OctoPrint-VirtualPrinterSettings
archive: https://github.com/cp2004/OctoPrint-VirtualPrinterSettings/archive/master.zip

tags:
- development
- settings
- virtual printer

screenshots:
- url: /assets/img/plugins/vp_settings/settings.png
  alt: settings screenshot
  caption: Screenshot of the settings interface

featuredimage: /assets/img/plugins/vp_settings/settings.png


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