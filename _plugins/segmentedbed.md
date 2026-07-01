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

A plugin to display individual segmented bed temps in real-time for Prusa XL printers.

As of version 2.0.0, the colors are now configurable via a settings page, and the tiles now show a variable-color heatmap increasing in intensity the hotter 
or colder a tile is versus the target temperature. Font colors are dynamically set based on tile color to increase readability. It also plays nicely with 
UICustomizer and dark themes.

**Note that as of 2.0.0, the color scheme has changed based on user feedback.** Instead of showing red for heating and blue for cooling, the gradient heatmap now
shows blue=cold and red=hot. This way, the heatmap tracks more closely with a normal thermometer, and not with the cooling behavior. The maximum variation 
is 10 degrees C. Any tile farther from the target than that will show maximum hot or cold color.

The colors used for hot and cold can be configured in the settings page. This page also shows a live preview of the Hot/Neutral/Cold colors to let you see how 
they will interact with your theme in real-time.
