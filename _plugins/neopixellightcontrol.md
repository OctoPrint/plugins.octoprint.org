---
layout: plugin

id: neopixellightcontrol
title: Neopixel Light Control
description: Uses PI GPIO to control an external RGB LED Neopixel Strip (Including Power Control)
authors:
- Lucas Härtel
#- second autor name
license: GNU General Public License

# today's date in format YYYY-MM-DD, e.g.
date: 2022-01-11

homepage: https://github.com/lucashaertel/octopi-neopixellightcontrol
source: https://github.com/lucashaertel/octopi-neopixellightcontrol
archive: https://github.com/lucashaertel/octopi-neopixellightcontrol/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- rgb
- neopixel
- gpio
- WS2812B
- LED

# screenshots:
# - url: url of a screenshot, /assets/img/...
#   alt: alt-text of a screenshot
#   caption: caption of a screenshot
# - url: url of another screenshot, /assets/img/...
#   alt: alt-text of another screenshot
#   caption: caption of another screenshot
# - ...

# featuredimage: url of a featured image for your plugin, /assets/img/...

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

#  octoprint:
#  - 1.2.0

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

#  os:
#  - linux
#  - windows
#  - macos
#  - freebsd

  # Compatible Python version
  #
  # Plugins should aim for compatibility for Python 2 and 3 for now, in which case the value should be ">=2.7,<4".
  #
  # Plugins that only wish to support Python 3 should set it to ">=3,<4".
  #
  # If your plugin only supports Python 2 (worst case, not recommended for newly developed plugins since Python 2
  # is EOL), leave at ">=2.7,<3" - be aware that your plugin will not be allowed to register on the
  # plugin repository if it only support Python 2.

  python: ">=2.7,<4"

---

#Neopixel Light Control

For now it is still WIP (not working) and based on the Plugin GpioRgbController from Erik Gundersen.

DO NOT USE!