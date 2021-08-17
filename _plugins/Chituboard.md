---
layout: plugin

id: Chituboard
title: Octoprint-Chituboard
description: compatibility layer for SLA printers with Chituboards like the Photon and Mars series
authors:Vikram Sarkhel
license: AGPLv3

date: 2021-07-10

homepage: https://github.com/rudetrooper/Octoprint-Chituboard
source: https://github.com/rudetrooper/Octoprint-Chituboard
archive: https://github.com/rudetrooper/Octoprint-Chituboard/archive/main.zip

follow_dependency_links: false

tags:
- anycubic
- cbd
- printer
- resin printer
- broken firmware
- workaround

screenshots:
- url: /assets/img/plugins/Chituboard/octoprint_chituboard.png
  alt: printing test file
  caption: printing file from octoprint
- url: /assets/img/plugins/Chituboard/Fileanalysistest.png
  alt: file dropdown
  caption: data on printable file

featuredimage: /assets/img/Chituboard/octoprint_chituboard.png

compatibility:
  octoprint:
  - 1.6.1
  os:
  - linux
  python:">=3.7,<4"

---

# Octoprint-Chituboard

Added basic support chituboard based printers(Elegoo Mars, Anycubic Photon, Phrozen, etc.) to octoprint.
* upload files to folder `~/.octoprint/uploads/resin`
* pause and resume are still somewhat buggy due to a timeout issue
* File analysis CLI command works `octoprint plugins Chituboard:sla_analysis NAME`

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

https://github.com/rudetrooper/Octoprint-Chituboard/archive/main.zip

## Requirements
1. **Raspberry Pi Zero W, Zero WH, 3A+ or 4B** only supports raspberry pi's with USB-OTG ports
2. Supported printers: SLA printers with chitu3d mainboard
  * Anycubic Photon
  * Elegoo Mars
  * Elegoo Mars Pro
  * Elegoo Mars 2
  * Elegoo Mars 2 Pro
  * Elegoo Saturn
  * Phrozen Sonic Mighty 4K
  * Phrozen Sonic Mini 4K
  * Creality LD-002H
  * Creality LD-002R
  * Voxelab Proxima
  * Peopoly Phenom L
  * EPAX E10/X10

##configuration

**Follow hardware setup instructions in source repo**
https://github.com/rudetrooper/Octoprint-Chituboard

### Connecting Pi to printers USB port

Our goal here is to use the Pi as a USB flash drive. The printer mainboards use the USB port to read USB FAT storage devices not for serial control. The printer can only supply around 500 mA via the 5V line so its best to power you pi with an external power source.
Follow one of these steps.
1. Put some tape on the 5V line of your USB cable. This [tutorial](https://l9o.dev/posts/controlling-an-elegoo-mars-pro-remotely/) is a good reference on how to do this.
2. Cut the connection between the 5V line and the USB port on the Pi. Some people online do this, but I didn’t want to do any permanent changes to my Pi.
3. The USB-OTG port on the Raspberry pi 4B is also the USB host port
  * users should put tape on the USB-A end of your USB C to USB A cable
  * users will also need to power the pi via the GPIO pins, I suggest using the [X735](https://wiki.geekworm.com/X735).
  * users who forget to tape over the 5V pin on will risk frying their pi 4B

### Connecting the Pi to the printer’s serial port

Connect the jumper wires from the pi's UART0 port to the Elegoo Mars 2 motherboard like this.
![pi_UART](/assets/img/plugins/Chituboard/schematic.png)
pinout.xyz is a good reference if you’re unfamiliar with the Raspberry Pi’s GPIO pins. Note that the Pi’s TX pin is connected to the motherboard’s RX pin and vice-versa. Connect GND to GND, Rx to Tx, and Tx to Rx

