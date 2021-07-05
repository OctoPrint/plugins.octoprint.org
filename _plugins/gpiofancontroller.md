---
layout: plugin

id: gpiofancontroller
title: OctoPrint-GpioFanController
description: Uses PI GPIO pins to control a variable speed fan with PWM
author: Erik Gundersen
license: AGPLv3

date: 2021-07-04

homepage: https://github.com/z4gunn/OctoPrint-GpioFanController
source: https://github.com/z4gunn/OctoPrint-GpioFanController
archive: https://github.com/z4gunn/OctoPrint-GpioFanController/archive/master.zip

# TODO
# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

# TODO
tags:
- fan
- gpio
- pwm

# TODO
screenshots:
- url: /assets/img/plugins/gpiofancontroller/sidebar.png
  alt: Sidebar speed control
  caption: Sidebar speed control
- url: /assets/img/plugins/gpiofancontroller/settings.png
  alt: Pin and PWM frequency settings
  caption: Pin and PWM frequency settings

# TODO
featuredimage: /assets/img/plugins/gpiofancontroller/featured.png

# TODO
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
  - 1.2.0

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
  - windows
  - macos
  - freebsd
  
  # Compatible Python version
  #
  # Plugins should aim for compatibility for Python 2 and 3 for now, in which case the value should be ">=2.7,<4".
  #
  # Plugins that only wish to support Python 3 should set it to ">=3,<4". 
  #
  # If your plugin only supports Python 2 (worst case, not recommended for newly developed plugins since Python 2
  # is EOL), leave at ">=2.7,<3"
  
  python: ">=3,<4"

---

This is a plugin to control an external fan via Raspberry Pi GPIO pin. This plugin allows you to set the pin number and PWM frequency in the settings and control the FAN speed via sidebar control.
