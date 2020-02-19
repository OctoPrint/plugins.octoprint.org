---
layout: plugin

id: webcamSB
title: OctoPrint-Webcamsb
description: Sidebar webcam viewer
author: Luis Magar Brunner
license: AGPLv3

# TODO
date: 2019-09-04

homepage: https://github.com/quanticchaos/OctoPrint-Webcamsb
source: https://github.com/quanticchaos/OctoPrint-Webcamsb
archive: https://github.com/quanticchaos/OctoPrint-Webcamsb/archive/master.zip

# TODO
# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

# TODO
tags:
- webcam
- sidebar
- stream

# TODO
screenshots:
- url: /assets/img/plugins/webcamSB/screen1.png
  alt: Screenshot settings
  caption: Screenshot of settings


# TODO
featuredimage: /assets/img/plugins/webcamSB/featured.png

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

---

This plugin adds a webcam stream viewer to the sidebar of Octoprint so you can keep an eye on your print at any moment.
You can click on the viewer to maximize the view.
You can flip the image in the configuration (even if left blank to use the default stream).
You can configure up to four streams (IP cam recommended when using multiple streams).
