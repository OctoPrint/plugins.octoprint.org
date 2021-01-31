---
layout: plugin

id: firmwareupdater
title: Firmware Updater
description: Update your printer's firmware from OctoPrint
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
- lpc1768
- lpc1769
- stm32

compatibility:
  python: ">=2.7,<4"

screenshots:
- url: /assets/img/plugins/firmwareupdater/firmware-updater.png
  alt: Firmware Updater
  caption: Firmware Updater
- url: /assets/img/plugins/firmwareupdater/avrdude.png
  alt: Avrdude Configuration
  caption: Avrdude Configuration
- url: /assets/img/plugins/firmwareupdater/bossac.png
  alt: Bossac Configuration
  caption: Bossac Configuration
- url: /assets/img/plugins/firmwareupdater/dfu-prog.png
  alt: Dfu Programmer Configuration
  caption: Dfu Programmer Configuration
- url: /assets/img/plugins/firmwareupdater/lpc176x.png
  alt: LPC176x Configuration
  caption: LPC176x Configuration
- url: /assets/img/plugins/firmwareupdater/stm32flash.png
  alt: STM32Flash Configuration
  caption: STM32Flash Configuration
- url: /assets/img/plugins/firmwareupdater/pre-post.png
  alt: Pre and Post-flash Options
  caption: Pre and Post-flash Options
- url: /assets/img/plugins/firmwareupdater/plugin-options.png
  alt: Plugin Options
  caption: Plugin Options

featuredimage: /assets/img/plugins/firmwareupdater/firmware-updater.png

---
## About
Allows you to flash pre-compiled firmware to your printer right from OctoPrint.

A large number of boards are supported, based on the MCU (processor) they have:
* Atmel Atmega (AVR) family 8-bit MCUs (e.g. RAMPS, Sanguinololu, Melzi, Anet, Creality, Ender, Prusa MMU, Prusa CW1 many others)
* Atmel AT90USB family 8-bit MCUs (e.g. Printrboard)
* Atmel SAM family 32-bit MCUs (e.g. Arduino DUE)
* NXP LPC1768 & LPC1769 MCUs (MKS SBASE, BigTreeTech SKR v1.1, v1.3, v1.4, etc., also SKR Pro v1.1)
* STM32 family 32-bits MCUs with embedded ST serial bootloader (e.g. FYSETC Cheetah, not SKR Pro)
* STM32 family 32-bit MCUs which update from the SD card using the same method as LPC176x boards (e.g. SKR Pro v1.1, SKR Mini E3 v2, etc.)

More boards can be added, please request additions via a [Github issue](https://github.com/OctoPrint/OctoPrint-FirmwareUpdater/issues).

### Additional Features
* Advanced options allow the flash methods to be configured or customized
* Pre and post-flash options allow gcode or system commands to be run before and after flashing
* A navbar icon can be enabled to give quick access to the Firmware Updater user interface

Full documentation is available on the [plugin's homepage](https://github.com/OctoPrint/OctoPrint-FirmwareUpdater).
