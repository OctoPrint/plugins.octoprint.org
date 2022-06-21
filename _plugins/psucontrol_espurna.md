---
layout: plugin

id: psucontrol_espurna
title: Octoprint-PSUControl-ESPurna
description: Plugin to control devices with ESPurna firmware
authors:
- Luis Diaz
license: AGPLv3


date: 2022-06-21

homepage: https://github.com/luismanson/Octoprint-PSUControl-ESPurna
source: https://github.com/luismanson/Octoprint-PSUControl-ESPurna
archive: https://github.com/luismanson/Octoprint-PSUControl-ESPurna/archive/master.zip


tags:
- psucontrol subplugin
- control
- power
- psu
- psucontrol
- espurna


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
  - windows
  - macos
  - freebsd

  # Compatible Python version
  #
  # It is recommended to only support Python 3 for new plugins, in which case this should be ">=3,<4"
  # 
  # Plugins that wish to support both Python 2 and 3 should set it to ">=2.7,<4".
  #
  # Plugins that only support Python 2 will not be accepted into the plugin repository.

  python: ">=3,<4"

---

See <https://github.com/luismanson/Octoprint-PSUControl-ESPurna> for information on configuration.
