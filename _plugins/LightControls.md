---
layout: plugin

id: LightControls
title: OctoPrint-LightControls
description: Adds easily configurable PWM Light controls to Octoprint Control Tab
authors:
- RoboMagus
license: AGPLv3

# TODO
date: 2021-07-09

homepage: https://github.com/RoboMagus/OctoPrint-LightControls
source: https://github.com/RoboMagus/OctoPrint-LightControls
archive: https://github.com/RoboMagus/OctoPrint-LightControls/archive/main.zip


tags:
- Raspberry PI
- Lights
- PWM
- Slider

screenshots:
- url: /assets/img/plugins/LightControls/LightControls_ControlPanel.png
  alt: LightControls on main Control Tab
  caption: LightControls on main Control Tab
- url: /assets/img/plugins/LightControls/LightControls_Settings.png
  alt: LightControls Settings Panel
  caption: LightControls Settings Panel

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
  - 1.6.0

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

  # Compatible Python version
  #
  # Plugins should aim for compatibility for Python 2 and 3 for now, in which case the value should be ">=2.7,<4".
  #
  # Plugins that only wish to support Python 3 should set it to ">=3,<4".
  #
  # If your plugin only supports Python 2 (worst case, not recommended for newly developed plugins since Python 2
  # is EOL), leave at ">=2.7,<3" - be aware that your plugin will not be allowed to register on the
  # plugin repository if it only support Python 2.

  python: ">=3,<4"

---