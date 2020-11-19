---
layout: plugin

id: firmwareupdater
title: Firmware Updater
description: Flash pre-compiled firmware images from OctoPrint
authors:
- Ben Lye
- Gina Häußge
- Nicanor Romero Venier
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2018-01-15

homepage: https://github.com/OctoPrint/OctoPrint-FirmwareUpdater
source: https://github.com/OctoPrint/OctoPrint-FirmwareUpdater
archive: https://github.com/OctoPrint/OctoPrint-FirmwareUpdater/archive/master.zip

tags:
- firmware
- avrdude
- firmware updater
- flashing
- arduino
- due
- bossac

compatibility:
  python: ">=2.7,<4"

screenshots:
- url: /assets/img/plugins/firmwareupdater/firmware-updater.png
  alt: Firmware Updater
  caption: Firmware Updater
- url: /assets/img/plugins/firmwareupdater/avrdude-config.png
  alt: Avrdude Configuration Options
  caption: Avrdude Configuration Options
- url: /assets/img/plugins/firmwareupdater/bossac-config.png
  alt: Bossac Configuration Options
  caption: Bossac Configuration Options
- url: /assets/img/plugins/firmwareupdater/post-flash-config.png
  alt: Post-flash Configuration Options
  caption: Post-flash Configuration Options

featuredimage: /assets/img/plugins/firmwareupdater/firmware-updater.png

---
## About
Allows you to flash pre-compiled firmware images to boards with Atmel AVR family 8-bit MCUs (`Atmega1280`, `Atmega1284p`, and `Atmega2560`, e.g. RAMPS, Anet, etc.), and Atmel SAM family 32-bit MCUs (e.g. `Arduino DUE`).

More boards can be added, please request additions via a [Github issue](https://github.com/OctoPrint/OctoPrint-FirmwareUpdater/issues).

Full documentation is available on the [plugin's homepage](https://github.com/OctoPrint/OctoPrint-FirmwareUpdater).
