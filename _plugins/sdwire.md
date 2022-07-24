---
layout: plugin

id: sdwire
title: OctoPrint-Sdwire
description: Fast file upload to SD card using sdwire hardware
authors:
- Arkadiusz Miśkiewicz
license: AGPLv3

date: 2022-07-24

homepage: https://github.com/arekm/OctoPrint-Sdwire
source: https://github.com/arekm/OctoPrint-Sdwire
archive: https://github.com/arekm/OctoPrint-Sdwire/archive/master.zip

tags:
- file
- file upload
- transfer
- sdwire
- upload

screenshots:
- url: /assets/img/plugins/sdwire/sdwire-octoprint.jpg
  alt: Uploading to sdwire
  caption: Uploading to sdwire
- url: /assets/img/plugins/sdwire/sdwire-hw.jpg
  alt: sdwire hardware
  caption: sdwire hardware

featuredimage: /assets/img/plugins/sdwire/sdwire-hw.jpg

compatibility:
  octoprint:
  - 1.4.0

  os:
  - linux

  python: ">=3,<4"

---

plugin uses sdwire hardware to handle *fast* `Upload to SD`.

`sdwire` is a device with *micro sd card* (inserted into it), *micro sd connector* (inserted into 3d printer) and a *micro USB
connector* to connect to host (like raspberry pi or other Linux based system).

Inserted sd card can be then made visible to the 3d printer or to the USB host (as regular usb-storage).
Copying to sd card from raspberry pi host using sdwire is fast (~10MB/s) compared to 115.2k serial port (~3KB/s; serial port slowness and g-code protocol overhead).
