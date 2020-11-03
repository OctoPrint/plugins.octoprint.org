---
layout: plugin

id: rgb_status
title: RGB Status
description: Adds RGB LED support to OctoPrint with the ability to choose colors and effects based on the current status of your printer
author: Eric Higdon
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2019-02-27

homepage: https://github.com/EricHigdon/OctoPrint-RGB_status
source: https://github.com/EricHigdon/OctoPrint-RGB_status
archive: https://github.com/EricHigdon/OctoPrint-RGB_status/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- RGB LED
- Addressable LED
- Progress
- Effects
- WS2811
- WS2812

screenshots:
- url: /assets/img/plugins/rgb_status/settings.png
  alt: RGB Status Settings
  caption: Settings for the strip of attached LEDs

featuredimage: /assets/img/plugins/rgb_status/featured.png

compatibility:
  os:
  - linux

  python: ">=2.7,<4"

---

# OctoPrint-Rgb_status

Adds RGB LED support to OctoPrint with the ability to choose effects based on the current status of your printer

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/EricHigdon/OctoPrint-Rgb_status/archive/master.zip

### Running Without Root

Since OctoPrint should usually not be run as root, the default LED pin is 10 (SPI). For details about what may be required to use SPI on your instance, see https://github.com/jgarff/rpi_ws281x#spi

## Reporting Issues & Improvments

If you encounter any issues or bugs with the plugin please feel free to make an issue on the repo. I also fully support additions to the plugin from third partys. If you have an idea or an already developed solution that would implement with the plugin well please submit it to the github repo and I will gladly consider additions and contributions.

See the [github page](https://github.com/EricHigdon/OctoPrint-RGB_status/) for more details.
