---
layout: plugin

id: ignorepausedforuser
title: IgnorePausedForUser
description: Plugin to ignore 'Paused for User' message from printer.
authors:
- Davide Mencarelli <d.mencarelli@outlook.com>
#- second autor name
license: GNU v3.0

# today's date in format YYYY-MM-DD, e.g.
date: 2021-02-19

homepage: https://github.com/DavideM84/OctoPrint-IgnorePausedForUser
source: https://github.com/DavideM84/OctoPrint-IgnorePausedForUser
archive: https://github.com/DavideM84/OctoPrint-IgnorePausedForUser/archive/main.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- paused for user
- pause
- ignore pause
- stuck print

screenshots:
- url: /assets/img/plugins/ignorepausedforuser/ignorepausedforuser2.jpg
  alt: ignorepausedforuser plugin
  caption: Plugin in action

featuredimage: /assets/img/plugins/ignorepausedforuser/ignorepausedforuser.jpg

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

# IgnorePausedForUser

Octoprint plugin to ignore 'Paused for User' message from printer.  

![screenshot](/assets/img/plugins/ignorepausedforuser/ignorepausedforuser.jpg)  

Occasionally when printing from Octoprint the printer stuck with the message "Paused for user".
This plugin when receives that message from the printer, sends an M108 to resume printing immediately.  
Obviously it should not be used if one or more filament changes are planned.
