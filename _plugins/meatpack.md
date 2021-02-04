---
layout: plugin

id: meatpack
title: MeatPack
description: Automatic G-Code Compression
authors:
- Scott Mudge
license: AGPLv3

date: 2021-01-26

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
- marlin

screenshots:
- url: /assets/img/plugins/meatpack/ss1.png
  alt: An example of the TX Statistics, showing compression ratio.
  caption: An example of the TX Statistics, showing compression ratio.

featuredimage: /assets/img/plugins/meatpack/meatpack.png

compatibility:
  python: ">=2.7,<4"

---


## MeatPack 
### Easy, fast, effective, and automatic g-code compression!

MeatPack is a plugin which automatically compresses/packs outgoing g-code to compatible firmware (\*see below!). It uses a unique data packing method which leverages the limited character-set inherent to most g-code. It is able to pack the most common characters in g-code into 4-bit blocks, while also retaining the ability to send full-width characters where needed. It also has the option to strip outgoing whitespace characters for an even greater compression ratio (ensure your firmware supports this).

It compresses/packs outgoing g-code by a ratio of 0.55 (or 0.61 without whitespace removal enabled). Meaning that what would normally be a 115,200 baud connection effectively becomes a 210,000 baud connection, with no changes to hardware. And it does all this with virtually zero computational overhead, so it is compatible with even the most speed-limited 16-MHz controllers.

**MeatPack does require firmware support!**, so do *NOT* install this plugin without first upgrading your firmware to a compatible build (where available). If you do not have a compatible firmware and install this plugin, connection to your printer may fail.

### Firmware with MeatPack Support:

To check if your firmware has MeatPack support, please check here: https://github.com/scottmudge/OctoPrint-MeatPack#firmware-with-meatpack-support

Adding support is fairly straight-forward, so if you'd like to add support into other firmware, please contact me and I can provide the latest firmware-side source code (also available in Prusa fork above).