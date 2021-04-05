---
layout: plugin

id: energeniecontrol
title: OctoPrint-EnergenieControl
description: Controls Energenie sockets to turn printer on and off.
authors:
- Arlo Blythe
license: AGPLv3


date: 2021-04-05

homepage: https://github.com/arlohb/OctoPrint-EnergenieControl
source: https://github.com/arlohb/OctoPrint-EnergenieControl
archive: https://github.com/arlohb/OctoPrint-EnergenieControl/archive/main.zip

tags:
- raspberry pi
- GPIO
- power
- wireless


compatibility:

  os:
  - linux

  python: ">=2.7,<4"

---

Uses the Energenie remote control sockets to turn the 3d printer on when OctoPrint connects, and turn it off when it disconnects.
The control board and two sockets can be found [here](https://energenie4u.co.uk/catalogue/product/ENER002-2PI)

The plugin doesn't add any UI to OctoPrint, it just runs when OctoPrint connects to, or disconnects from, the printer. This can be done from the OctoPrint sidebar, but any automatic connections or disconnections will also trigger it.