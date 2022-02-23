---
layout: plugin

id: M150Control
title: OctoPrint-M150control
description: Send M150 control through the UI
author: Jean-Philippe Alexandre
license: AGPLv3

date: 2020-07-03

homepage: https://github.com/horfee/OctoPrint-M150control
source: https://github.com/horfee/OctoPrint-M150control
archive: https://github.com/horfee/OctoPrint-M150control/archive/master.zip

# TODO
# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- M150
- color
- LED

screenshots:
- url: /assets/img/plugins/M150Control/screenshot.jpg
  caption: Main control
  alt: M150 control screenshot
featuredimage: /assets/img/plugins/M150Control/screenshot.jpg

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

  python: ">=2.7,<4"

---
This plugin allow you to control led directly with a custom ui control. It send M150 command to the printer, which can be intercepted by Octoprint with plugins like PCA9685LedStrip.
You can click and drag the color you want or validate every color to avoid flooding the printer.
http://plugins.octoprint.org/plugin/M150Control/
