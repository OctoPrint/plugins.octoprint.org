---
layout: plugin

id: mystromswitch
title: OctoPrint-MyStromSwitch
description: Plugin to integrate myStrom Switch into your OctoPrint installation
author: David Zingg
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2019-11-27

homepage: https://github.com/da4id/OctoPrint-MyStromSwitch
source: https://github.com/da4id/OctoPrint-MyStromSwitch
archive: https://github.com/da4id/OctoPrint-MyStromSwitch/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- MyStrom
- Switch
- Relay

screenshots:
- url: /assets/img/plugins/mystromswitch/sidebar_on_button.png
  alt: Sidebar
  caption: Sidebar Module when Switch is on with Toggle Button
- url: /assets/img/plugins/mystromswitch/fullscreen.png
  alt: Main screen
  caption: Main Screen with the plugin on the bottom left
- url: /assets/img/plugins/mystromswitch/settings_page.png
  alt: Settins Page
  caption: Settings Page of the Plugin
- url: /assets/img/plugins/mystromswitch/sidebar_off.png
  alt: Sidebar Relais off
  caption: Sidebar Module when Switch is off and toggle Button disabled
- url: /assets/img/plugins/mystromswitch/sidebar_on.png
  alt: Sidebar Relais on
  caption: Sidebar Module when Switch is on and toggle Button disabled
- url: /assets/img/plugins/mystromswitch/sidebar_off_button.png
  alt: Sidebar Relais off with Toggle Button
  caption: Sidebar Module when Switch is off with Toggle Button



featuredimage: /assets/img/plugins/mystromswitch/sidebar_on_button.png

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

Plugin to integrate [myStrom Switch](https://mystrom.ch/de/wifi-switch/) into your OctoPrint installation