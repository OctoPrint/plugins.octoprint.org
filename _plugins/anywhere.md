---
layout: plugin

id: anywhere
title: OctoPrint Anywhere
description: Monitor and control your 3D printers from anywhere, on your phone.
author: Kenneth Jiang
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2017-06-26

homepage: https://github.com/kennethjiang/OctoPrint-Anywhere
source: https://github.com/kennethjiang/OctoPrint-Anywhere
archive: https://github.com/kennethjiang/OctoPrint-Anywhere/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- remote
- webcam
- job
- control
- monitor
- phone
- network

screenshots:
- url: /assets/img/plugins/anywhere/screenshot1.png
  alt: phone screenshot
  caption: Webcam feed, temperature feed, job progress
- url: /assets/img/plugins/anywhere/screenshot2.png
  alt: phone screenshot
  caption: Pause or cancel print job
- url: /assets/img/plugins/anywhere/screenshot3.png
  alt: multiple 3D printers
  caption: Multiple 3D printers

featuredimage: /assets/img/plugins/anywhere/screenshot1.png

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
  - 1.3.2

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

## Monitor and control your 3D printer from ANYWHERE

Built on nascent IoT platfrom [Anywhere](https://www.getanywhere.io), OctoPrint Anywhere extends
your control beyond the local network.

* Get webcam feed on your smart phone (Only when you are checking. There is no network traffic when the page is open in background).
* Get real-time feed on temperatures and print job.
* Pause or cancel print job.
* Display the IP address of your OctoPrint on your phone.
* Check status of all your 3D printers on the same page at a glance.
* Many more to come...
