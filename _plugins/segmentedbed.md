---
layout: plugin

id: segmentedbed
title: Segmented Bed Plugin
description: A plugin to display segmented heatbed temps for Prusa XL printers
authors:
- Nikhil S. Shringarpurey
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2024-10-07

homepage: https://github.com/DoubleStrike/OctoPrint-SegmentedBed
source: https://github.com/DoubleStrike/OctoPrint-SegmentedBed
archive: https://github.com/DoubleStrike/OctoPrint-SegmentedBed/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- Prusa
- PrusaXL
- XL
- tiles
- heatbed

# When registering a plugin on plugins.octoprint.org, all screenshots should be uploaded not linked from external sites.
screenshots:
- url: /assets/img/plugins/segmentedbed/segmentedbed.png
  alt: Snapshot of segmented bed UI
  caption: Snapshot of segmented bed UI

featuredimage: /assets/img/plugins/segmentedbed/segmentedbed.png

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

# If any of the below attributes apply to your project, uncomment the corresponding lines. This is MANDATORY!

attributes:
#  - cloud  # if your plugin requires access to a cloud to function
#  - commercial  # if your plugin has a commercial aspect to it
#  - free-tier  # if your plugin has a free tier

---

A plugin to display individual segmented bed temps in real-time for Prusa XL printers.  It also plays nicely with UICustomizer and dark themes.

No configuration settings at the moment. Hope to add color coding options and allow selection of number of tiles to allow use of other future printers.
