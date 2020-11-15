---
layout: plugin

id: fixcbdfirmware
title: Fix CBD Firmware
description: Fixes communication with a broken firmware making its rounds that identifies as "CBD make it"
author: Gina Häußge
license: AGPLv3

date: 2020-03-25

homepage: https://github.com/OctoPrint/OctoPrint-FixCBDFirmware
source: https://github.com/OctoPrint/OctoPrint-FixCBDFirmware
archive: https://github.com/OctoPrint/OctoPrint-FixCBDFirmware/archive/master.zip

tags:
- workaround
- communication
- firmware
- broken firmware
- anycubic
- xinkebot
- qidi tech
- tronxy
- cbd
- zwlf

compatibility:
  python: ">=2.7,<4"

---

This plugin works around issues with a firmware that identifies itself only with the string `CBD make it` in response
to `M115` - hence the name "CBD Firmware" due to a lack of alternatives - and which wrongly implements some parts of
the established communication protocol, causing severe issues when trying to communicate and print with it from
OctoPrint.

You can read more about this firmware and what printers are currently known to ship with it
[in this FAQ entry](https://faq.octoprint.org/warning-firmware-broken-cbd).

Installing this plugin should make any printers shipped with this broken firmware work with OctoPrint.

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/OctoPrint/OctoPrint-Fix-CBD-Firmware/archive/master.zip
