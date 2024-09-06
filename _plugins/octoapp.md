---
layout: plugin

id: octoapp
title: OctoApp
description: The Companion Plugin for OctoApp
authors:
- Christian Würthner
#- second autor name
license: AGPL v3

# today's date in format YYYY-MM-DD, e.g.
date: 2021-12-01

homepage: https://play.google.com/store/apps/details?id=de.crysxd.octoapp&hl=en&gl=US
source: https://github.com/crysxd/OctoApp-Plugin
archive: https://github.com/crysxd/OctoApp-Plugin/archive/refs/heads/release.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- android
- app
- notifications
- push
- print finished
- control
- phone
- octoapp
- monitor
- obico
- octoeverywhere
- ngrok
- monitoring
- remote app

screenshots:
- url: /assets/img/plugins/octoapp/carousel.webp
  alt: Get OctoApp on Google Play
  caption: Get OctoApp on Google Play
- url: /assets/img/plugins/octoapp/screenshot.png
  alt: Automatic setup
  caption: OctoApp will connect automatically!
# - url: url of another screenshot, /assets/img/...
#   alt: alt-text of another screenshot
#   caption: caption of another screenshot
# - ...

featuredimage: /assets/img/plugins/octoapp/carousel.webp

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
  - 1.7.0

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

  #python: ">=2.7,<3" # Python 2 & 3
  python: ">=3,<4" # Python 3 only

attributes:
- cloud
- commercial
- free-tier

---

A plugin providing extra functionality to OctoApp:

- Remote push notification for events like print completion or filament change with end-to-end encryption
- Remote push notifications for your print progress with end-to-end encryption
- More coming in the future!

Get OctoApp on Google Play!

[![Google Play](/assets/img/plugins/octoapp/play-badge.png)](https://play.google.com/store/apps/details?id=de.crysxd.octoapp&hl=en&gl=US)  [![App Store](/assets/img/plugins/octoapp/app-store-badge.png)](https://apps.apple.com/us/app/octoapp-for-octoprint/id1658133862)

This plugin requires OctoApp 1.11 or newer!
