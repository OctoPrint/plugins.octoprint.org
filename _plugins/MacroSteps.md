---
layout: plugin

id: MacroSteps
title: OctoPrint-MacroSteps
description: A plugin that shows a step by step any print start macro.
authors:
- Rodrigo C. C. Silva
license: AGPLv3

# TODO
date: 2023-01-11

homepage: https://github.com/SinisterRj/OctoPrint-MacroSteps
source: https://github.com/SinisterRj/OctoPrint-MacroSteps
archive: https://github.com/SinisterRj/OctoPrint-MacroSteps/archive/main.zip

# TODO
# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

# TODO
tags:
- macro
- gcode
- script
- custom
- sidebar

# TODO
# When registering a plugin on plugins.octoprint.org, all screenshots should be uploaded not linked from external sites.
screenshots:
- url: /assets/img/plugins/MacroSteps/MS.jpg
  alt: Sidebar screenshot
  caption: Sidebar screenshot

# TODO
featuredimage: /assets/img/plugins/MacroSteps/MSfeatured.png

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


# Macro Steps

Tired of searching hundreds of terminal lines for the reason of a halt on your print start? Do you want more feedback on what is happening with your printer? This is the solution for your problems. This is a simple Octoprint plugin that enables you to follow the steps of your big macros in a very intuitive way. 

It creates a sidepanel on Octoprint's UI with every step (or GCODE command) of your MACRO and updates it on the fly, indicating what is finished, what is running, what was skiped or what failed, helping to diagnose when something went wrong.

![MacroSteps Plugin sidebar](/assets/img/plugins/MacroSteps/MS.jpg)

