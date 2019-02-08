---
layout: plugin

id: LCD1602_I2cdisplay
title: octoprint-LCD1602 v0.1.1
description: This plug-in allows you to control a 16X2 lcd display (hd44780 connected to port I2C) to display the octoprint status. It is useful for people like me who have a printer without a display. It indicates on which port the printer is connected, the progress of printing. It also displays the remaining print time (thanks to a simple method). See https://github.com/n3bojs4/octoprint-LCD1602/blob/master/CHANGELOG.md for more details.
author: n3bojs4
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2019-02-08

homepage: https://github.com/n3bojs4/octoprint-LCD1602
source: https://github.com/n3bojs4/octoprint-LCD1602
archive: https://github.com/n3bojs4/OctoPrint-Lcd1602/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- display
- loading bar
- events

screenshots:
- url: /assets/img/plugins/LCD1602_I2cdisplay/connect.jpg
  alt: connection screen
- url: /assets/img/plugins/LCD1602_I2cdisplay/progress.jpg
  alt: Progress bar

featuredimage: /assets/img/plugins/LCD1602_I2cdisplay/progress.jpg

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
  - 1.3.10

  # List of compatible operating systems
  #
  # Possible values:
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
  - windows
  - macos
  - freebsd

---
