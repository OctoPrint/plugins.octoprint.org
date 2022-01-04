---
layout: plugin

id: ublmeshedit
title: OctoPrint-UBLMeshEdit
description: A plugin that provides a method for manually editing and saving/loading UBL meshes.
authors:
- Taylor Talkington
license: AGPLv3

date: 2021-02-24

homepage: https://github.com/The-EG/OctoPrint-UBLMeshEdit
source: https://github.com/The-EG/OctoPrint-UBLMeshEdit
archive: https://github.com/The-EG/OctoPrint-UBLMeshEdit/archive/main.zip


tags:
- bed leveling
- ubl
- mesh

screenshots:
- url: /assets/img/plugins/ublmeshedit/screenshot.png
  alt: UBL Mesh Editor
  caption: UBL Mesh Editor

featuredimage: /assets/img/plugins/ublmeshedit/screenshot.png

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
  - 1.3.7

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
  # Plugins should aim for compatibility for Python 2 and 3 for now, in which case the value should be ">=2.7,<4".
  #
  # Plugins that only wish to support Python 3 should set it to ">=3,<4".
  #
  # If your plugin only supports Python 2 (worst case, not recommended for newly developed plugins since Python 2
  # is EOL), leave at ">=2.7,<3" - be aware that your plugin will not be allowed to register on the
  # plugin repository if it only support Python 2.

  python: ">=2.7,<4"

---

# OctoPrint-UBLMeshEdit

![screenshot](/assets/img/plugins/ublmeshedit/screenshot.png)

UBL Mesh Editor can be used to view, edit and manage Marlin Unified Bed Leveling (UBL) meshes. 

See the plugin repository for the most up to date information and features: https://github.com/The-EG/OctoPrint-UBLMeshEdit

*Note: this is only intended for UBL. This plugin will attempt to show and provide basic functionality for ABL meshes, but some features will be disabled and others may not function as expected.*

For issues and feature requests, [check the issues on GitHub](https://github.com/The-EG/OctoPrint-UBLMeshEdit/issues) and create one if needed.

