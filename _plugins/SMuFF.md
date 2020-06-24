---
layout: plugin

id: SMuFF
title: OctoPrint-Smuff
description: A plugin for controlling tool changes on the SMuFF from OctoPrint as published on Thingiverse https://www.thingiverse.com/thing:3431438
author: Technik Gegg
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2020-06-11

homepage: https://github.com/technik-gegg/OctoPrint-Smuff
source: https://github.com/technik-gegg/OctoPrint-Smuff
archive: https://github.com/technik-gegg/OctoPrint-Smuff/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- SMuFF
- MMU
- Tool changer
- Multi material
- Marlin 2.0

screenshots:
- url: /assets/img/plugins/SMuFF/SMuFF-Settings.jpg
  alt: SMuFF plugin settings
  caption: The SMuFF plugin 
- url: /assets/img/plugins/SMuFF/SMuFF-V5.png
  alt: Smart Multi Filament Feeder 
  caption: The SMuFF V5

featuredimage: /assets/img/plugins/SMuFF/SMuFF_V5.jpg

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

This is a plugin for OctoPrint which handles tool changes for the SMuFF (as published on [Thingiverse](https://www.thingiverse.com/thing:3431438)).
This plugin runs in the background and tracks tool changes (Tx) via the **octoprint.comm.protocol.gcode.queuing** hook of OctoPrint.
When triggered, it'll send the according command to the SMuFF via the Raspberry's second onboard UART ttyS0.

For further information on how to configure your Raspberry Pi, please visit this [Github repository](https://github.com/technik-gegg/OctoPrint-Smuff).

      
