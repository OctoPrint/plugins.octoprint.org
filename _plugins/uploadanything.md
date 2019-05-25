---
layout: plugin

id: uploadanything
title: Upload Anything
description: Allows custom file types to be uploaded via the web interface
author: Roberto Lo Giacco
license: Apache License 2.0

# today's date in format YYYY-MM-DD, e.g.
date: 2019-05-25

homepage: https://github.com/rlogiacco/UploadAnything
source: https://github.com/rlogiacco/UploadAnything
archive: https://github.com/rlogiacco/UploadAnything/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- file upload
- upload

screenshots:
- url: /assets/img/uploadanything/settings.png
  alt: Plugin settings
  caption: Customize allowed file extensions

featuredimage: /assets/img/uploadanything/settings.png

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

---

If you want to keep your files organized storing project files and models along the sliced GCODE as I do then this plugin will allow you to overcome the default constraint allowing to upload only GCODE files via the file embedded file upload mechanism.

By default this plugin adds the following file extensions:

* STL
* OBJ
* 3MF
* JPG
* GIF
* PNG

You can add or remove from the above list at your liking via the dedicated plugin settings.