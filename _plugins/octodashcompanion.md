---
layout: plugin

id: octodashcompanion
title: OctoDash Companion
description: This plugin allows for configuring OctoDash settings and upload custom theme files from within the OctoPrint interface.
authors:
- jneilliii
license: MIT

date: 2021-05-03

homepage: https://github.com/jneilliii/OctoPrint-OctoDashCompanion
source: https://github.com/jneilliii/OctoPrint-OctoDashCompanion
archive: https://github.com/jneilliii/OctoPrint-OctoDashCompanion/archive/master.zip

tags:
- OctoDash

screenshots:
- url: /assets/img/plugins/octodashcompanion/screenshot_settings.png
  alt: OctoDash Companion
  caption: OctoDash Companion Settings

featuredimage: /assets/img/plugins/octodashcompanion/screenshot_settings.png

compatibility:
  octoprint:
  - 1.4.0
  os:
  - linux
  - windows
  - macos
  - freebsd
  python: ">=3.3,<4"

---

# OctoDash Companion

This plugin allows for configuring OctoDash settings and upload custom theme files from within the OctoPrint interface. It assumes that you have both OctoDash and OctoPrint running on the same physical machine.

## Configuration

![settings](/assets/img/plugins/octodashcompanion/screenshot_settings.png)

Once installed you can use the OctoDash Companion settings to configure the Printer Name and [Custom Actions](https://github.com/UnchartedBull/OctoDash/wiki/Custom-Actions). Other settings will be added as deemed necessary.

To upload a new [Custom Theme](https://github.com/UnchartedBull/OctoDash/wiki/Custom-Styles) file, just upload the `custom-styles.css` file to OctoPrint as if it were a gcode file.

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

### Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip or become a Patron if you find this plugin helpful and want me to continue future development.

[![Patreon](/assets/img/plugins/active_filters_extended/patreon-with-text-new.png)](https://www.patreon.com/jneilliii) [![paypal](/assets/img/plugins/active_filters_extended/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>
