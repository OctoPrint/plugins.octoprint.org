---
layout: plugin

id: thespaghettidetective
title: Access Anywhere - The Spaghetti Detective
description: The Spaghetti Detective is now Obico! Please install "Obico for OctoPrint" instead.
author: The Obico team
license: AGPLv3

# TODO
date: 2019-11-07

homepage: https://www.obico.io
source: https://github.com/TheSpaghettiDetective/OctoPrint-TheSpaghettiDetective
archive: https://github.com/TheSpaghettiDetective/OctoPrint-TheSpaghettiDetective/archive/master.zip

# TODO
# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

# TODO
tags:
- remote
- monitor
- webcam
- phone
- control
- port forwarding
- safe
- secure
- internet
- remote access
- remote app
- remote camera
- remote printing
- monitoring
- AI
- Machine Learning
- app
- mobile
- mobile app
- push notification
- cloud printing
- free
- plugin support


# TODO
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
  - 1.3.8

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

  python: ">=2.7,<4"

---

<p class="alert alert-warning">Access Anywhere - The Spaghetti Detective plugin has been
succeeded by <a href="/plugins/obico/">Obico for OctoPrint</a>.</p>

Obico is everything you loved about The Spaghetti Detective, but smarter and more open.

Please visit the Obico for OctoPrint [plugin page](/plugins/obico/) or [the Obico
website](https://obico.io) to learn more about Obico.

For existing The Spaghetti Detective users, please:

1. Uninstall The Spaghetti Detective plugin while keep its data in OctoPrint.
2. Then install [the Obico plugin](/plugins/obico/).
3. All your existing settings in The Spaghetti Detective will be automatically migrated.

For more info, go to [everything about migrating from The Spaghetti Detective to
Obico](https://www.obico.io/docs/user-guides/move-from-tsd-to-obico-in-octoprint/).


-- The Obico Team (Formally TSD Team)
