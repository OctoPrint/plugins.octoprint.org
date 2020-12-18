---
layout: plugin

id: display_panel
title: OctoPrint Display Panel
description: Simple control and status paired with a physical button panel and OLED display
author: Seth Voltz
license: MIT

date: 2020-12-16

homepage: https://github.com/sethvoltz/OctoPrint-DisplayPanel
source: https://github.com/sethvoltz/OctoPrint-DisplayPanel
archive: https://github.com/sethvoltz/OctoPrint-DisplayPanel/archive/main.zip

tags:
- monitoring
- hardware
- physical hardware
- oled

screenshots:
- url: /assets/img/plugins/display_panel/in-situ.jpeg
  alt: Installed and running button hardware installed on the printer, OLED display showing stats
  caption: Control Panel on the Printer
- url: /assets/img/plugins/display_panel/glamour.jpeg
  alt: Glamour shot of the hardware before installation on a blue background
  caption: Look how pretty it is...
- url: /assets/img/plugins/display_panel/wiring-diagram.png
  alt: Wiring diagram describing placement of parts, wires and how to plug into the Raspberry Pi
  caption: Wiring Diagram

featuredimage: /assets/img/plugins/display_panel/in-situ.jpeg

compatibility:

  octoprint:
  - 1.3.0

  os:
  - linux

  python: ">=3,<4"

---

This plugin implements the software control side of an OctoPrint Control Panel for Octopi. The hardware half is a series of 4 buttons, an OLED screen and a 3D printed case that mounts on the printer next to the Raspnerry Pi so it can be plugged in to the header pins.

**Watch a demo of the panel in action!** More photos are at the end of this readme.

[![Screenshot of demo video](/assets/img/plugins/display_panel/youtube-cover.jpg)](https://youtu.be/78emT1ollu4 "Click here to watch a demo on YouTube")

## Hardware

3D models are available on [Thingiverse](https://www.thingiverse.com/thing:4674214).

Please see the [plugin repository](https://github.com/sethvoltz/OctoPrint-DisplayPanel) for the latest hardware and wiring instructions. The wiring instructions at the time of publishing are below.

![Wiring diagram for the control panel](/assets/img/plugins/display_panel/wiring-diagram.png)

## Setup

**NOTE:** This plugin required OctoPrint to be updated to run on Python 3. Please follow [these instructions](https://community.octoprint.org/t/upgrade-your-octoprint-install-to-python-3/23973) if you are not already on Python 3.

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/sethvoltz/OctoPrint-DisplayPanel/archive/main.zip
