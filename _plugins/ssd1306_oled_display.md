---
layout: plugin

id: ssd1306_oled_display
title: SSD1306 OLED Display
description: Use a 128x32 SSD1306-based display to display printer and job status for OctoPrint.
authors:
- Fredrik Baberg
license: AGPLv3

date: 2023-03-25

homepage: https://github.com/fredrikbaberg/OctoPrint-SSD1306
source: https://github.com/fredrikbaberg/OctoPrint-SSD1306
archive: https://github.com/fredrikbaberg/OctoPrint-SSD1306/archive/main.zip

follow_dependency_links: false

tags:
- display
- ssd1306
- PiOLED

# When registering a plugin on plugins.octoprint.org, all screenshots should be uploaded not linked from external sites.
screenshots:
- url: /assets/img/plugins/ssd1306_oled_display/pioled.jpg
  alt: PiOLED on Raspberry Pi
  caption: Display information on PiOLED display

featuredimage: /assets/img/plugins/ssd1306_oled_display/pioled.jpg

# You only need the following if your plugin requires specific OctoPrint versions or
# specific operating systems to function - you can safely remove the whole
# "compatibility" block if this is not the case.

compatibility:

  # List of compatible versions
  #
  # A single version number will be interpretated as a minimum version requirement,
  # e.g. "1.3.1" will show the plugin as compatible to OctoPrint versions 1.3.1 and up.
  # More sophisticated version requirements can be modelled too by using PEP440
  # compatible version specifiers.
  #
  # You can also remove the whole "octoprint" block. Removing it will default to all
  # OctoPrint versions being supported.

  octoprint:
  - 1.4.0

  # List of compatible operating systems
  #
  # Valid values:
  #
  # - windows
  # - linux
  # - macos
  # - freebsd
  #
  # There are also two OS groups defined that get expanded on usage:
  #
  # - posix: linux, macos and freebsd
  # - nix: linux and freebsd
  #
  # You can also remove the whole "os" block. Removing it will default to all
  # operating systems being supported.

  os:
  - linux
  # - windows
  # - macos
  # - freebsd

  # Compatible Python version
  #
  # It is recommended to only support Python 3 for new plugins, in which case this should be ">=3,<4"
  # 
  # Plugins that wish to support both Python 2 and 3 should set it to ">=2.7,<4".
  #
  # Plugins that only support Python 2 will not be accepted into the plugin repository.

  python: ">=3,<4"

---

This plugin enables the use of a SSD1306-based display to present printer- and job- status for OctoPrint.
Presents connection status, latest M117 message, temperature, job percentage completed and estimated remaining time.

The plugin assumes the SSD1306 is connected by I2C through SDA, SCL.

It's based on [https://github.com/jhoos/OctoPrint-SSD1306](https://github.com/jhoos/OctoPrint-SSD1306).
Testing has been done with a Pi OLED display, 128x32, but it should be possible to change the resolution in plugin settings.
