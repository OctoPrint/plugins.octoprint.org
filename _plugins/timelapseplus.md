---
layout: plugin

id: timelapseplus
title: Timelapse+
description: Timelapse+ is a powerful yet lightweight plugin to capture, enhance and render your print timelapses.
author: Christoph Muche
license: CC BY-ND
date: 2023-04-24

homepage: https://github.com/cmuche/octoprint-timelapseplus
source: https://github.com/cmuche/octoprint-timelapseplus
archive: https://github.com/cmuche/octoprint-timelapseplus/archive/master.zip

tags:
- timelapseplus
- timelapse
- snapshot
- ffmpeg
- render

screenshots:
- url: /assets/img/plugins/timelapseplus/files.png
  alt: File Manager
  caption: File Manager
- url: /assets/img/plugins/timelapseplus/current-print.png
  alt: Current Print Job
  caption: Current Print Job

featuredimage: /assets/img/plugins/timelapseplus/logo.png

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
  - 1.8.0

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
  # If your plugin only supports Python 2 it will no longer be accepted on the plugin repository.
  #
  # Uncomment the appropriate setting

  python: ">=3.7,<4"

---

{% include youtube.html vid="fV8yoPwcXAU" preview="https://github.com/cmuche/octoprint-timelapseplus/raw/master/assets/timelapseplus.gif" %}

## Features
- Trigger snapshots via __commands__ in your GCODE (e.g. on layer change)
  - __@-Commands__ like ``@SNAPSHOT``
  - __Action Commands__ like ``//action:SNAPSHOT`` (on Marlin via ``M118``)
- Regular __time-based__ snapshot mode
- User-friendly and tidy user interface
  - __View, watch and download__ your rendered videos
  - __Preview__ your __render settings__ and check the estimated video length before starting a render job
- Customizable __image enhancements for post-processing__
  - __Brightness__ and __contrast__
  - __Auto-Optimization__ by histogram equalization
  - __Blur__ parts of the video for privacy when sharing
  - Resizing
- __Frame interpolation__ for __smoother timelapses__!
  - __Generate frames__ between your captured frames
  - Based on __motion calculation__ algorithms
  - Or just __blend frames__ together to generate sub-frames
- __Combine/Blend multiple frames__ to reduce the number of total frames
- Colorful Fade-In and Fade-Out effects
- Manage and set up your enhancement- and render presets via the settings page
- Snapshots are stored in __Frame Collections__, so you can re-render them at any time with different settings and presets
- __Preview__ the __snapshot capturing__ live while printing
- Timelapse+ __doesn't modify your GCODE__ and __doesn't affect your printer's movements__!