---
layout: plugin

id: Gcode-chocolate
title: Gcode-chocolate
description: Modify the gcode to optimize the print path
author: YTY
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2019-07-30

homepage: https://github.com/WHUTYTY/plugins.octoprint.org.git
source: https://github.com/WHUTYTY/plugins.octoprint.org.git
archive:https://raw.githubusercontent.com/WHUTYTY/plugins.octoprint.org/gh-pages/_plugins/Gcode-chocolate.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
follow_dependency_links: false
tags:
- a list
- of tags
- that apply
- to your plugin
- (take a look at the existing plugins for what makes sense here)

screenshots:
- url: url of a screenshot, /assets/img/plugins/Gcode/Gcode.png
  alt: alt-text of a screenshot
  caption: caption of a screenshot
- url: url of another screenshot, /assets/img/plugins/Gcode/Gcode.png
  alt: alt-text of another screenshot
  caption: caption of another screenshot
- ...

featuredimage: url of a featured image for your plugin, /assets/img/plugins/Gcode/Gcode.png

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
  - 1.3.11

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

---

Longer description of your plugin, configuration examples etc. This part will be visible on the page at
plugins.octoprint.org/plugin/<your plugin identifier>/
    
Use Markdown for formatting.
manually using this URL:https://raw.githubusercontent.com/WHUTYTY/plugins.octoprint.org/gh-pages/_plugins/Gcode-chocolate.zip
