---
layout: plugin

id: terminalresponse
title: Terminal Response
description: Monitors terminal for a regular expression and allows you to respond with your own commands.
author: Xiao Jin
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2020-05-07

homepage: https://github.com/xia0/OctoPrint-TerminalResponse
source: https://github.com/xia0/OctoPrint-TerminalResponse
archive: https://github.com/xia0/OctoPrint-TerminalResponse/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- regex
- regular
- expressions
- gcode
- command
- commands
- terminal
- monitor
- send

screenshots:
- url: https://github.com/xia0/OctoPrint-TerminalResponse/raw/master/screenshots/01.png
  alt: Plugin settings
  caption: Plugin settings

featuredimage: /assets/img/plugins/terminalresponse/01.png

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

  python: ">=2.7,<4"

---

This plugin will monitor the terminal for regular expressions that you define. You can use parentheses to extract values from matches. You can then define commands to run in response to your regex matches and substitute the matches values to your liking.
