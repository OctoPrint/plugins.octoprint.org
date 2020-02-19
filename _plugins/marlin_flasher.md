---
layout: plugin

id: marlin_flasher
title: Marlin Flasher
description: Plugin that allows you to flash your printer to the latest Marlin version
author: Renaud Gaspard
license: MIT

date: 2019-04-02

homepage: https://github.com/Renaud11232/OctoPrint-Marlin-Flasher
source: https://github.com/Renaud11232/OctoPrint-Marlin-Flasher
archive: https://github.com/Renaud11232/OctoPrint-Marlin-Flasher/archive/master.zip

follow_dependency_links: false

tags:
- firmware
- updater
- flasher
- arduino
- platformio
- marlin

screenshots:
- url:  /assets/img/plugins/marlin_flasher/arduino_sketch.png
  alt: arduino_sketch
  caption: The sketch menu to upload your Arduino firmware
- url: /assets/img/plugins/marlin_flasher/arduino_cores.png
  alt: arduino_cores
  caption: The core menu where you can manage the supported boards
- url:  /assets/img/plugins/marlin_flasher/arduino_libraries.png
  alt: arduino_libraries
  caption: The libraries menu where you can manage the installed libraries
- url: /assets/img/plugins/marlin_flasher/arduino_flash.png
  alt: arduino_flash
  caption: The flash menu where you start the flashing process using Arduino
- url:  /assets/img/plugins/marlin_flasher/pio_project.png
  alt: pio_project
  caption: The Platform.io project menu where you can upload your PlatformIO firmware
- url: /assets/img/plugins/marlin_flasher/pio_flash.png
  alt: arduino_flash
  caption: The flash menu where you start the flashing process using PlatformIO

featuredimage: /assets/img/plugins/marlin_flasher/arduino_flash.png

compatibility:
  octoprint:
  - 1.2.0

  os:
  - linux
  - windows
  - macos
  - freebsd

---

Adds the ability to easily update your Arduino and Platform.io based printer firmware with just a few clicks directly through OctoPrint.
You can install multiple libraries if your firmware needs it, upload your firmware code, and just hit Flash.

Please be aware that I'm not responsible for any damage made to your printer if something had to go wrong during the flashing process.

**See** the [README](https://github.com/Renaud11232/OctoPrint-Marlin-Flasher/blob/master/README.md) or the [wiki](https://github.com/Renaud11232/OctoPrint-Marlin-Flasher/wiki) for more information on how to configure and use this plugin.
