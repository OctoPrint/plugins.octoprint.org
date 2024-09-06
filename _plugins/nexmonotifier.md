---
layout: plugin

id: nexmonotifier
title: OctoPrint-Nexmonotifier
description:  Octoprint plugin for print completion notifications using Nexmo SMS gateway
author: Gert Kjerslev
license: AGPLv3

# TODO
date: 2018-10-02

homepage: https://github.com/gfk76/OctoPrint-Nexmonotifier
source: https://github.com/gfk76/OctoPrint-Nexmonotifier
archive: https://github.com/gfk76/OctoPrint-Nexmonotifier/archive/master.zip

# TODO
# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

# TODO
tags:
- notification
- SMS
- Text message

# TODO
screenshots:
- url: /assets/img/plugins/nexmonotifier/nexmonotifier.png
  alt: Settings dialog and SMS notification screenshot
  caption: Configure notification recipient, secret, api key and message.

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
  - 1.2.0

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

attributes:
- cloud

---

Receive SMS/Text notifications when OctoPrint jobs are complete.
