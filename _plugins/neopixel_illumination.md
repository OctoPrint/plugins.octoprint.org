---
layout: plugin

id: neopixel_illumination
title: OctoPrint-NeoPixel Illumination
description: Control NeoPixels through color picker and GCODE.
authors:
- brettvitaz
license: AGPLv3
date: 2022-05-24

homepage: https://github.com/brettvitaz/OctoPrint-Neopixel_Illumination
source: https://github.com/brettvitaz/OctoPrint-Neopixel_Illumination
archive: https://github.com/brettvitaz/OctoPrint-Neopixel_Illumination/archive/master.zip
tags:
- neopixel
- m150
- light
- led
- neo
- pixel
screenshots:
- url: /assets/img/plugins/neopixel_illumination/navbar_control.png
  alt: Navbar control
  caption: Navbar Control
- url: /assets/img/plugins/neopixel_illumination/tab_control.png
  alt: Tab control
  caption: Tab Control
- url: /assets/img/plugins/neopixel_illumination/settings.png
  alt: Settings
  caption: Settings

featuredimage: /assets/img/plugins/neopixel_illumination/navbar_control.png

compatibility:
  os:
  - linux
  - windows
  - macos
  - freebsd
  python: ">=3,<4"

---

# NeoPixel Illumination

This plugin will allow control of NeoPixels from OctoPrint.

- Use your Raspberry Pi to power and control your NeoPixels. (I have tested powering up to 25 pixels from a Raspberry Pi 4).
- Change color and intensity from a color picker dialog.
- Intercept GCODE [M150][M150] commands and execute them on the Raspberry Pi.

## Configuration

| Setting | Description | Default |
| :--- | :--- | :--- |
| Enable | Enable/Disable NeoPixel strip | |
| Watch GCODE for M150 | Supports parsing [M150][M150] commands in GCODE | |
| Pixel Pin | GPIO control pin | [18][PIN18]  |
| Number of Pixels | Number of pixels to control | 24 |
| Pixel Order | Color order supported by neopixel strip | [GRBW][GRBW] |
| Brightness | Startup brightness | 1.0 |
| sudo Password | Password for the 'pi' user | raspberry |

## More

Please see [OctoPrint-Neopixel_Illumination on GitHub](https://github.com/brettvitaz/OctoPrint-Neopixel_Illumination) for more information.

[M150]: https://marlinfw.org/docs/gcode/M150.html
[PIN18]: https://pinout.xyz/pinout/pin12_gpio18#
[GRBW]: https://learn.adafruit.com/adafruit-neopixel-uberguide/python-circuitpython
