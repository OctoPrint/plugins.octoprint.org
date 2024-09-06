---
layout: plugin

id: octoprint_complicated
title: OctoPrint-Complicated
description: Display Print Progress on your Apple Watch using the Complicated iOS App
author: Mike Lyons
license: AGPLv3

# TODO
date: 2019-04-23

homepage: https://github.com/frenchie4111/complicated-octoprint
source: https://github.com/frenchie4111/complicated-octoprint
archive: https://github.com/frenchie4111/complicated-octoprint/archive/master.zip

# TODO
tags:
- apple watch
- ios
- progress

# TODO
screenshots:
- url: /assets/img/plugins/octoprint_complicated/settings.png
  alt: Complicated Settings
  caption: Complicated Settings Menu
- url: /assets/img/plugins/octoprint_complicated/demo.png
  alt: Watch Demo
  caption: Print Progress on your Apple Watch

featuredimage: /assets/img/plugins/octoprint_complicated/demo.png

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

attributes:
- cloud

---

# OctoPrint Complicated Integration

This plugin allows you to show your 3d print progress on your Apple Watch by integrating with
the Complicated iOS/Apple Watch app.

## What is Complicated?

Complicated is a simple app that lets you update your Apple Watch face complications with WebHooks. You can also use IFTTT and Zapier to update the WebHooks.

![Demo Apple Watch](/assets/img/plugins/octoprint_complicated/demo.png)

https://mikelyons.org/complicated?utm_source=octoprint-complicated

[![Complicated Download App](/assets/img/plugins/octoprint_complicated/app_store.png)](https://itunes.apple.com/us/app/complicated/id1444561091?ls=1&mt=8)
