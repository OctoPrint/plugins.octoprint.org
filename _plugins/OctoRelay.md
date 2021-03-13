---
layout: plugin

id: OctoRelay
title: OctoRelay
description: A plugin to control relays or other things on the GPIO pins of your raspberry pi. For example turn the power of printer, the light or a fan ON and OFF via the web interface.

authors:
- Boris Burgstaller
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2021-03-13

homepage: https://github.com/borisbu/OctoRelay
source: https://github.com/borisbu/OctoRelay
archive: https://github.com/borisbu/OctoRelay/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- raspberry pi
- GPIO
- relay
- power
- switch

screenshots:
- url: /assets/img/plugins/OctoRelay/screenshot.png
  alt: navbar customization
  caption: navbar customization
- url: /assets/img/plugins/OctoRelay/settings.png
  alt: settings
  caption: settings

featuredimage: /assets/img/plugins/OctoRelay/screenshot.png

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
  - 1.3.0

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
  # If your plugin only supports Python 2 (worst case, not recommended for newly developed plugins since Python 2
  # is EOL), leave at ">=2.7,<3"

  python: ">=2.7,<3"

---

A plugin that adds buttons to the navigation bar to toggle GPIO pins on the Raspberry Pi.
I use it with a 4 relay board, and printed this case for it: https://www.thingiverse.com/thing:2975944

Just hooked up the GPIO pins with the relay board, and now I can turn the power of the printer, the fan and the light on and foo with OctoPrint.
