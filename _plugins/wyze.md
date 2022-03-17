---
layout: plugin

id: wyze
title: OctoPrint-Wyze
description: Control Wyze devices through OctoPrint
authors:
- Eric Shapiro
license: AGPLv3

date: 2022-03-16

homepage: https://github.com/eshapiro42/OctoPrint-Wyze
source: https://github.com/eshapiro42/OctoPrint-Wyze
archive: https://github.com/eshapiro42/OctoPrint-Wyze/archive/main.zip

follow_dependency_links: false

tags:
- wyze
- control
- events
- scheduling
- lights

# When registering a plugin on plugins.octoprint.org, all screenshots should be uploaded not linked from external sites.
screenshots:
- url: /assets/img/plugins/wyze/OctoPrint-Wyze.png
  alt: OctoPrint-Wyze Screenshot
  caption: OctoPrint-Wyze Screenshot


featuredimage: /assets/img/plugins/wyze/OctoPrint-Wyze.png

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

  python: ">=3.8,<4"

---

OctoPrint-Wyze lets you control and automate Wyze home devices through OctoPrint. You can register plugs, lights and cameras to turn on or off whenever specific events occur. For example, you can set a light to turn on whenever the web client is opened, or a print or timelapse is started, then off when a print has finished.

NOTE: Only Python 3.8 and up will work! This is not ideal since OctoPrint does not officially support anything higher than Python 3.7 at the moment, so you will need to be comfortable updating OctoPrint's Python environment. This is a hard requirement because the wyze_sdk module that this plugin relies on will only work with Python 3.8 and up.
