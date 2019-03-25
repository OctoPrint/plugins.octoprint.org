---
layout: plugin

id: marlin_flasher
title: Marlin Flasher
description: Plugin that allows you to flash your printer to the latest Marlin (or any Arduino firmware) version
author: Renaud Gaspard
license: MIT

date: 2019-03-19

homepage: https://github.com/Renaud11232/OctoPrint-Marlin-Flasher
source: https://github.com/Renaud11232/OctoPrint-Marlin-Flasher
archive: https://github.com/Renaud11232/OctoPrint-Marlin-Flasher/archive/master.zip

follow_dependency_links: false

tags:
- firmware
- updater
- flasher
- arduino

screenshots:
- url:  /assets/img/plugins/marlin_flasher/sketch.png
  alt: sketch
  caption: The sketch menu to upload your firmware code
- url: /assets/img/plugins/marlin_flasher/cores.png
  alt: cores
  caption: The core menu where you can manage the supported boards
- url:  /assets/img/plugins/marlin_flasher/libraries.png
  alt: libraries
  caption: The libraries menu where you can manage the installed libraries
- url: /assets/img/plugins/marlin_flasher/flash.png
  alt: flash
  caption: The flash menu where you start the flashing process

featuredimage: /assets/img/plugins/marlin_flasher/flash.png

compatibility:
  octoprint:
  - 1.2.0

  os:
  - linux
  - windows
  - macos
  - freebsd

---

Adds the ability to easily update your Arduino based printer firmware with just a few clicks directly through OctoPrint.
You can install multiple libraries if your firmware needs it, upload your firmware code, and just hit Flash.

Please be aware that I'm not responsible for any damage made to your printer if something had to go wrong during the flashing process.

**See** the [README](https://github.com/Renaud11232/OctoPrint-Marlin-Flasher/blob/master/README.md) for more information on how to configure and use this plugin
