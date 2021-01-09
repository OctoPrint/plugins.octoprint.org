---
layout: plugin

id: meatpack
title: MeatPack
description: Automatic G-Code Compression
authors:
- Scott Mudge
license: AGPLv3

date: 2021-01-09

homepage: https://github.com/scottmudge/OctoPrint-MeatPack
source: https://github.com/scottmudge/OctoPrint-MeatPack
archive: https://github.com/scottmudge/OctoPrint-MeatPack/archive/master.zip

tags:
- gcode
- compression
- firmware
- serial
- packing
- prusa

screenshots:
- url: /assets/img/plugins/meatpack/ss1.png
  alt: An example of the TX Statistics, showing compression ratio.
  caption: An example of the TX Statistics, showing compression ratio.

featuredimage: /assets/img/plugins/meatpack/meatpack.png

compatibility:
  python: ">=2.7,<4"

---

## About

MeatPack is a plugin which automatically compresses/packs outgoing g-code to compatible firmware (\*see below!). It uses a unique data packing method which leverages the limited character-set inherent to most g-code. It is able to pack the most common characters in g-code into 4-bit blocks, while also retaining the ability to send full-width characters where needed.

It compresses/packs outgoing g-code by a ratio of 0.61. Meaning that what would normally be a 115,200 baud connection effectively becomes a 188,850 baud connection, with no changes to hardware. And it does all this with virtually zero computational overhead, so it is compatible with even the most speed-limited 16-MHz controllers.

**MeatPack does require modifications to firmware**, so do ***NOT*** install this plugin without first upgrading your firmware to a compatible build (where available). If you do not have a compatible version of controller firmware, the plugin will simply do nothing.

**NOTE:** MeatPack is currently only compatible with my custom build of Prusa MK3 firmware. You can find builds of the latest v3.9.3 firmware here: https://github.com/scottmudge/Prusa-Firmware-MeatPack

This custom build of the Prusa MK3 firmware is functionally identical to the official build, however it has added functionality for MeatPack. I currently have a pull-request open for adding this feature to the official firmware, but it is currently pending. The firmware is compatible with both uncompressed and compressed g-code, and the OctoPrint plugin will manage and synchronize the settings automatically. Just install and go!