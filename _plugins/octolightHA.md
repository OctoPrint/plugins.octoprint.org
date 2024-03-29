---
layout: plugin

id: octolightHA
title: OctoLight Home Assistant
description: Adds a button to the navbar, toggling a Home Assistant controlled light. Forked off of OctoLight by Žiga Kralj
authors:
- Mark Bloom
#- second autor name
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2023-07-04

homepage: https://github.com/mark-bloom/OctoLight_Home-Assistant
source: https://github.com/mark-bloom/OctoLight_Home-Assistant
archive: https://github.com/mark-bloom/OctoLight_Home-Assistant/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- raspberry pi
- home assistant
- lights

screenshots:
- url: /assets/img/plugins/octolightHA/screenshot.png 

featuredimage: /assets/img/plugins/octolightHA/screenshot.png

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
  - 0.0.1

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

  # Compatible Python version
  #
  # Plugins should aim for compatibility for Python 2 and 3 for now, in which case the value should be ">=2.7,<4".
  #
  # Plugins that only wish to support Python 3 should set it to ">=3,<4".
  #
  # If your plugin only supports Python 2 (worst case, not recommended for newly developed plugins since Python 2
  # is EOL), leave at ">=2.7,<3"

  python: ">=2.7,<4"

---

Adds a button to the navbar, toggling a Home Assistant controlled light. Forked off of OctoLight by Žiga Kralj


![screenshot](/assets/img/plugins/octolightHA/settings1.png)

