---
layout: plugin

id: display-eta
title: OctoPrint-Display-ETA
description: Show finish time (ETA time) for current print.
author: Pablo Ventura
license: AGPLv3

# TODO
date: today's date in format YYYY-MM-DD, e.g. 2015-04-21

homepage: https://github.com/pablogventura/Octoprint-ETA
source: https://github.com/pablogventura/Octoprint-ETA
archive: https://github.com/pablogventura/Octoprint-ETA/archive/master.zip

# TODO
# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

# TODO
tags:
- time
- eta
- finish time

# TODO
screenshots:
- url: /assets/img/plugins/octoprint_eta/screenshot.png
  alt: alt-text of a screenshot
  caption: ETA time for current print.


# TODO
featuredimage: /assets/img/plugins/octoprint_eta/screenshot.png

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
  - 1.3.6

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

---

Display estimated time of finish for current print (Estimated Time of Arrival). Day of finish is displayed only when current print not finish today.

![alt text](/assets/img/plugins/octoprint_eta/screenshot.png)

## Setup


You must have the time zone configured on the host, otherwise you will see the time in UTC.
In Debian the following commands are made "sudo dpkg-reconfigure tzdata", then follow the wizard.
