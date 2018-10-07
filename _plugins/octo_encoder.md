---
layout: plugin

id: octo_encoder
title: Octo_Filament_Encoder
description: filament checker with encoder
author: Alex
license: AGPLv3

# TODO
date: 2018-05-10

homepage: https://github.com/Akex2/Octo_Filament_Encoder
source: https://github.com/Akex2/Octo_Filament_Encoder
archive: https://github.com/Akex2/Octo_Filament_Encoder/archive/master.zip

# TODO
# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

# TODO
tags:
- action
- automatic
- commands
- control
- filament
- monitoring
- encoder

# TODO
screenshots:
- url: /assets/img/plugins/octo_encoder/setting_octo.png
  alt: Settings Dialog
  caption: The settings dialog allows configuring the all setup of octo encoder
- url: /assets/img/plugins/octo_encoder/setting_octo2.png
  alt: Settings Dialog
  caption: The settings dialog allows configuring the all setup of octo encoder

# TODO
featuredimage: /assets/img/plugins/octo_encoder/setting_octo2.png

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

---

This plugin is only for Raspberry-pi
It detect filament run-out/blocked nozzle

How it works :
It read the gcode sent at the printer and compare to the encoder step, if the diferance is too hight, the plugin send the commande block (pause print)

The encoder is wirring on the raspberry gpio 17 and 18
