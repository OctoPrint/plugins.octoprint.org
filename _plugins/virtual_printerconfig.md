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
  - 1.5.0

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

#### This plugin is not under _active_ development, but if you have any problems, or feature requests I would be happy to take a look & see what I can do.

## Compatibility

The lastest version of the plugin is only compatible with OctoPrint 1.5.x.
To find a version compatible with your instance, take a look in the table below

{:.table}
| OctoPrint version | Plugin version | Install URL                                                                    |
| ----------------- | -------------- | ------------------------------------------------------------------------------ |
| 1.5.x             | 1.5.x          | `https://github.com/cp2004/OctoPrint-VirtualPrinterSettings/archive/1.5.0.zip` |
| 1.4.1/2           | 0.1.3          | `https://github.com/cp2004/OctoPrint-VirtualPrinterSettings/archive/0.1.3.zip` |

Use the above URLs in OctoPrint's [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html) >
Get More > ...from URL field.

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/cp2004/OctoPrint-VirtualPrinterSettings/archive/master.zip

## Configuration

Plugin adds settings to OctoPrint's UI that are [documented here](https://docs.octoprint.org/en/master/development/virtual_printer.html#virtual-printer-configuration-options)

It replaces the original implementation, introduced in OctoPrint 1.4.1
