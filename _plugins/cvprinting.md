---
layout: plugin

id: cvprinting
title: OctoPrint-CVPrinting
description: Computer vision for detecting issue during 3d printing with automatic notification to Discord and Telegram and pausing the print. This plugin has minimal HW requirements. Check plugin page for more information.
authors:
- Viliam Chudacik
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2025-04-21

homepage: https://github.com/Spini11/OctoPrint-Cvprinting
source: https://github.com/Spini11/OctoPrint-Cvprinting
archive: https://github.com/Spini11/OctoPrint-Cvprinting/archive/refs/heads/master.zip

# Set this if your plugin heavily interacts with any kind of cloud services.
#privacypolicy: your plugin's privacy policy URL

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- defect detections
- ai
- computer vision
- discord
- telegram
- notifications
- local
- monitoring

screenshots:
- url: /assets/img/plugins/cvprinting/sidebar.png
  alt: "Sidebar with current status and settings"
  caption: "Sidebar box allows to see current detection confidence and change notification and pause settings"
- url: /assets/img/plugins/cvprinting/discordNotification.png
  alt: "Discord notification showing snapshot of spaghetty error, togehter with confidence value and information that print has been paused"
  caption: "Example of discord notification after print pause has been triggered"

featuredimage: /assets/img/plugins/cvprinting/discordNotification.png

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
  - 1.10.3

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

  # Compatible Python version
  #
  # Plugins should aim for compatibility for Python 2 and 3 for now, in which case the value should be ">=2.7,<4".
  #
  # Plugins that only wish to support Python 3 should set it to ">=3,<4".
  #
  # If your plugin only supports Python 2 it will no longer be accepted on the plugin repository.
  #
  # Uncomment the appropriate setting

  #python: ">=2.7,<3" # Python 2 & 3
  python: ">=3,<4" # Python 3 only

# TODO
# If any of the below attributes apply to your project, uncomment the corresponding lines. This is MANDATORY!
    
attributes:
  - cloud  # if your plugin requires access to a cloud to function
#  - commercial  # if your plugin has a commercial aspect to it
#  - free-tier  # if your plugin has a free tier

---

Computer vision for detecting issue during 3d printing with automatic notification to Discord and Telegram and pausing the print. This plugin has minimal HW requirements. Recommended hardware is Raspberry pi 5, older version are not supported.
