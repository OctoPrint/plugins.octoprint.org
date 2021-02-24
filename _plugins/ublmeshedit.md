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

featuredimage: /assets/img/plugins/ublmeshedit/screenshot.png.

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

In its current state, this plugin is intended to be used to make minor tweaks to a mesh that is already valid and setup. This could be to correct a point that wasn't probed properly for some reason or to fine tune the mesh when using `PROBE_MANUALLY`. It won't help with the initial creation of a mesh, except in the case of starting with a zero mesh and manually editing points.

*Note: this is only intended for UBL, and not any other ABL or MBL setup. It assumes a square mesh and will not function properly with other shapes.*

## Usage

With the printer connected and idle, switch to the 'UBL Mesh Editor' tab and click 'Get Mesh'. The current mesh will be shown.

Click a point to edit the value. The current value will be shown next to 'Z Value.' That value can be changed by clicking up/down or by entering a value. To save the value, click 'Save Value.'

UBL Mesh Editor can also save and load saved meshes. Select the mesh slot next to 'Mesh Save Slot' and click either 'Save' or 'Load.'

*Note: the plugin does not currently verify the save mesh slot is valid.*

For issues, [check the issues on GitHub](https://github.com/The-EG/OctoPrint-UBLMeshEdit/issues) and create one if needed.

