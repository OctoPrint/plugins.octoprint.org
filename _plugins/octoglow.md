---
layout: plugin
id: octoglow
title: OctoGlow
description: Display OctoPrint status on a PiGlow board.
author: Dan Malec
license: CC BY-NC-SA 4.0
date: 2015-05-12
homepage: https://github.com/dmalec/OctoPrint-OctoGlow
source: https://github.com/dmalec/OctoPrint-OctoGlow
archive: https://github.com/dmalec/OctoPrint-OctoGlow/archive/master.zip
tags:
- notification
screenshots:
- url: /assets/img/plugins/octoglow/progress.png
  alt: Example progress indicator
  caption: Example progress indicator for a print job in progress
featuredimage: /assets/img/plugins/octoglow/progress.png
---

The OctoGlow plugin for OctoPrint displays status on a [Pimoroni PiGlow](http://shop.pimoroni.com/products/piglow) attached to a Raspberry Pi.  It displays animations for the following events:

  * Printer connected
  * Printjob started
  * Printjob progress updated
  * Printjob done
  * Printjob cancelled
  * Printjob failed

## Configuration

The PiGlow board requires i2c to be enabled on the Raspberry Pi.  Please follow the [Pimoroni guide on enabling i2c](https://github.com/pimoroni/piglow) on the Raspberry Pi.

Additionally, the pi user must be added to the i2c group in order to allow OctoPrint to send commands to the PiGlow without needing root privileges:

``` bash
sudo adduser pi i2c
```
