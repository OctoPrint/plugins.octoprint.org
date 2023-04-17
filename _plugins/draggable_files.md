---
layout: plugin

id: draggable_files
title: Draggable Files
description: Plugin that allows for the dragging of files in the File Manager
authors:
  - Sander Ronde
license: MIT

date: 2021-05-18

homepage: https://github.com/SanderRonde/Octoprint-Draggable-Files
source: https://github.com/SanderRonde/Octoprint-Draggable-Files
archive: https://github.com/SanderRonde/Octoprint-Draggable-Files/archive/main.zip

#follow_dependency_links: false

tags:
  - file
  - filemanager
  - file_manager
  - dragging

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

# Octoprint Draggable Files

Plugin that allows for the dragging of files in the File Manager. Additionally, it adds the ability to resize the file manager.

## Example:

![Dragging files or folders](/assets/img/plugins/draggable_files/dragging.gif)

![Resizing the file manager](/assets/img/plugins/draggable_files/resizing.gif)
