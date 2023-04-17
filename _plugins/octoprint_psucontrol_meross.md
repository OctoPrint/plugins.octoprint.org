---
layout: plugin

id: octoprint_psucontrol_meross
title: PSU Control - Meross
description: Adds Meross IOT device support to PSUControl
authors:
- Ilja Orlovs
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2022-02-22

homepage: https://github.com/VRGhost/OctoPrint-PSUControl-Meross
source: https://github.com/VRGhost/OctoPrint-PSUControl-Meross
archive: https://github.com/VRGhost/OctoPrint-PSUControl-Meross/archive/refs/tags/stable-latest.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- control
- meross
- power
- psu
- psucontrol
- psucontrol subplugin

# screenshots: []

# featuredimage: null

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
  - 1.7.3

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
  # If your plugin only supports Python 2 it will no longer be accepted on the plugin repository.
  #
  # Uncomment the appropriate setting

  python: ">=3,<4" # Python 3 only

---

This plugin enables the "PSU Control" plugin to control Meross devices.

# Requirements:
- [PSU Control plugin for OctoPrint](https://plugins.octoprint.org/plugins/psucontrol/)
