---
layout: plugin

id: theater3d
title: Theater 3D
description: This is a tool to serve as a pan/tilt controller for checking on larger prints.
author: Princton Brennan
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2020-01-05

homepage: https://github.com/NerdboyQ/OctoPrint-Theater3d
source: https://github.com/NerdboyQ/OctoPrint-Theater3d.git
archive: https://github.com/NerdboyQ/OctoPrint-Theater3d/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- servo
- pan-tilt
- camera
- print recording
- large prints

screenshots:
- url: https://github.com/NerdboyQ/OctoPrint-Theater3d/blob/master/screenshot_plugin_00.png
  alt: Theater 3D Layout
  caption: This will be the new tab ui that will be added to control the pan/tilt system

featuredimage: url of a featured image for your plugin, /assets/img/...

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
  - 1.3.0

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
      
  python: ">=2.7,<3"
      
---

Longer description of your plugin, configuration examples etc. This part will be visible on the page at
plugins.octoprint.org/plugin/<your plugin identifier>/
    
Use Markdown for formatting.
