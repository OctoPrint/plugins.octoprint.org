---
layout: plugin

id: RewriteM600
title: Rewrite M600 - For M600 Unsupported
description:  Implement M600 for pinters that can't support M600 by default (TFT with out marlin mode support, like Artilelry X1 and Genius)
author: Gustavo Cevallos
license: MIT

# today's date in format YYYY-MM-DD, e.g.
date: 2020-06-23

homepage: https://github.com/wgcv/RewriteM600
source: https://github.com/wgcv/RewriteM600
archive: https://github.com/wgcv/RewriteM600t/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- filament
- simplified
- trigger
- color change
- hook
- M600

screenshots:
- url: /assets/img/plugins/RewriteM600/M600-in-action.png
  alt: Askin to change the filament
  caption: Ask to change filament - M600

featuredimage: /assets/img/plugins/RewriteM600/M600-in-action.png

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
# This plugin implement M600 with out Marlin support.

Implement M600 for pinters that can't support M600 by default (TFT with out Marlin Mode support, like Artilelry X1 and Genius). You can use M600, is going to stop wait until you change and press resume. If you have a TFT 28 (Like the Artillery) i would recomend you to check [Rawr TFT Firmware](https://github.com/wgcv/RAWR-TFT-Firmware-Artillery3D) to implement M600 direct in the TFT and do not need Octoprint.
