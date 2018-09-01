---
layout: plugin

id: ProgressBasedOnTime
title: OctoPrint-ProgressBasedOnTime
description: Replace file based progression by time based progression
author: Celogeek
license: AGPLv3

date: 2018-09-01

homepage: https://github.com/celogeek/OctoPrint-ProgressBasedOnTime
source: https://github.com/celogeek/OctoPrint-ProgressBasedOnTime
archive: https://github.com/celogeek/OctoPrint-ProgressBasedOnTime/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
follow_dependency_links: false

tags:
- progress
- analysis
- estimation
- estimator
- print time
- time

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
  - 1.3.9

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

---

This plugin will change the way octoprint send back progress information to the plugins and apps.

Octoprint send progress information based on file progression.

This plugin will send progress information based on the time left to print.

It will apply change for all plugin and apps that display progression information. It keep sending file progress to the estimators.

I suggest to associate those plugins:
 * Print Time Genius (https://plugins.octoprint.org/plugins/PrintTimeGenius/)
 * DetailedProgress (https://plugins.octoprint.org/plugins/detailedprogress/).



