---
layout: plugin

id: mote_lighting_control
title: OctoPrint-MoteLightingControl
description: Control a set of Mote lights - with different OctoPrint conditions causing changes in the lighting colour and state.
authors:
- Nigel Metheringham
license: AGPLv3

date: 2021-07-14

homepage: https://github.com/nigelm/OctoPrint-MoteLightingControl
source: https://github.com/nigelm/OctoPrint-MoteLightingControl
archive: https://github.com/nigelm/OctoPrint-MoteLightingControl/archive/main.zip

tags:
- lights
- led
- rgb

screenshots:
- url: /assets/img/plugins/mote_lighting_control/mote_lights_configuration.png
  alt: Configuration Screen
  caption: Configuration Screen
- url: /assets/img/plugins/mote_lighting_control/mote_lights_navbar.png
  alt: Nav Bar lighting button
  caption: Nav Bar lighting button

featuredimage: /assets/img/plugins/mote_lighting_control/mote_lights.jpg

# TODO
# You only need the following if your plugin requires specific OctoPrint versions or
# specific operating systems to function - you can safely remove the whole
# "compatibility" block if this is not the case.

compatibility:
  # Python 3 only so we restrict octoprint too.  Allow windows, but don't realistically
  # expect it to work there!
  octoprint:
  - 1.4.0
  os:
  - linux
  - windows
  - macos
  - freebsd
  python: ">=3,<4"

---

Control a set of [Pimoroni Mote](https://shop.pimoroni.com/products/mote)
lights - with different OctoPrint conditions causing changes in the lighting colour and state.

Lighting changes can happen on changes in state - for example a print start or
finish - or via a manual button on the navbar.

This code only supports the USB version of the Mote controllers.  Since a Pi
Zero is not suitable for running OctoPrint, and is not likely to be used, and
I do not have the relevant hardware, the PHAT version of the Mote controller
is not supported.

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/nigelm/OctoPrint-MoteLightingControl/archive/main.zip


## Configuration

The configuration allows you to select the colours used for each OctoPrint state.

You can enable/disable automatic lighting changes on any state change, and
additionally enable/disable each state individually.   By default all state
changes do cause lighting changes,

The selectable states, and their default colours are:-

- *On OctoPrint Startup* - Blue
- *Printer Connected* - Green
- *Printer Disconnected* - Black (lights off)
- *File Uploaded* - Yellow for a few seconds
- *Active Printing* - White
- *Print Finished* - Pink
- *Error* or *Print Failed* - Red


## Credits

This plugin draws very heavily on
[`OctoPrintMote`](https://github.com/topshed/OctoPrintMote) by
[Richard Hayler](https://github.com/topshed)

Additionally some code was used from
[`OctoLight`](https://plugins.octoprint.org/plugins/octolight/)
(the API handling code and js), and
[`TP-Link Smartplug`](https://plugins.octoprint.org/plugins/tplinksmartplug/).
