---
layout: plugin

id: virtual_printerconfig
title: Virtual Printer Settings
description: Add configurable settings to the Virtual Printer plugin under OctoPrint's settings
author: Charlie Powell
license: AGPLv3

date: 2020-08-04

homepage: https://github.com/cp2004/OctoPrint-VirtualPrinterSettings
source: https://github.com/cp2004/OctoPrint-VirtualPrinterSettings
archive: https://github.com/cp2004/OctoPrint-VirtualPrinterSettings/releases/latest/download/release.zip

tags:
- development
- settings
- virtual printer

screenshots:
- url: /assets/img/plugins/virtual_printerconfig/settings.png
  alt: settings screenshot
  caption: Screenshot of settings interface

featuredimage: /assets/img/plugins/virtual_printerconfig/settings.png


compatibility:

  octoprint:
  - 1.8.0

  os:
  - linux
  - windows
  - macos
  - freebsd

  python: ">=3.7,<4"

---

Add easily configurable and well organised settings for OctoPrint's virtual printer.
Overrides the default template which only has an enabling checkbox.

Very useful if you are developing plugins, or even core OctoPrint. No more digging deep into config.yaml and hoping you typed the settings correctly!

#### This plugin is not under _active_ development, but if you have any problems, or feature requests I would be happy to take a look & see what I can do.

## Compatibility

The latest version of the plugin is only tested with the most recent OctoPrint version, and since the settings available can change between OctoPrint
releases, the current version of the plugin may not work with older versions of OctoPrint.

If you are using an older version of OctoPrint, you can find details on which plugin versions to use [on the plugin's homepage.](https://github.com/cp2004/OctoPrint-VirtualPrinterSettings#octoprint)

## Setup

Installation can be performed with from within OctoPrint's plugin manager or manually using the install URL above.

## Configuration

Plugin adds settings to OctoPrint's UI that are [documented here](https://docs.octoprint.org/en/master/development/virtual_printer.html#virtual-printer-configuration-options)

It replaces the original implementation, introduced in OctoPrint 1.4.1.
