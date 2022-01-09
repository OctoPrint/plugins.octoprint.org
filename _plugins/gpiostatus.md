---
layout: plugin

id: gpiostatus
title: GPIO Status
description: This plugin allows to check the Raspberry GPIO status.

authors:
- danieleborgo
#- second autor name
license: GPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2022-01-08

homepage: https://github.com/danieleborgo/OctoPrint-GPIOStatus
source: https://github.com/danieleborgo/OctoPrint-GPIOStatus
archive: https://github.com/danieleborgo/OctoPrint-GPIOStatus/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- gpio
- raspberry
- raspberrypi
- raspbian
- linux
- gpiostatus
- pin
- pins
- bcm

screenshots:
- url: /assets/img/plugins/gpiostatus/GPIO.png
  alt: GPIO.png
  caption: GPIO status representation
- url: /assets/img/plugins/gpiostatus/Hardware.png
  alt: Hardware.png
  caption: Hardware page data
- url: /assets/img/plugins/gpiostatus/Services.png
  alt: Services.png
  caption: Services page data
- url: /assets/img/plugins/gpiostatus/Refresh.png
  alt: Refresh.png
  caption: Refresh button

featuredimage: /assets/img/plugins/gpiostatus/GPIO.png

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
  - 1.7.2

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

  # Compatible Python version
  #
  # Plugins should aim for compatibility for Python 2 and 3 for now, in which case the value should be ">=2.7,<4".
  #
  # Plugins that only wish to support Python 3 should set it to ">=3,<4".
  #
  # If your plugin only supports Python 2 it will no longer be accepted on the plugin repository.
  #
  # Uncomment the appropriate setting

  #python: ">=2.7,<3" # Python 2 & 3
  python: ">=3,<4" # Python 3 only

---

# GPIO Status

This OctoPrint plugin allows to check the GPIO status
by its web interface, without the need to connect via SSH.
In addition, it permits knowing services' status and
hardware information.

This plugin doesn't know which pins are in use and which
are free, since its purpose is to just show their state.

## Prerequisites

This plugin must be executed on a Rasperry and  requires
the two commands __*raspi-config*__ and __*raspi-gpio*__.
They're usually installed by default but, if they are not,
the plugin will show a notification message on its
settings page.

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/danieleborgo/OctoPrint-GPIOStatus/archive/master.zip


## Screenshots

![Refresh](/assets/img/plugins/gpiostatus/Refresh.png)
![GPIO](/assets/img/plugins/gpiostatus/GPIO.png)
![Services](/assets/img/plugins/gpiostatus/Services.png)
![Hardware](/assets/img/plugins/gpiostatus/Hardware.png)

## License

This software is distributed on GPLv3.0.
