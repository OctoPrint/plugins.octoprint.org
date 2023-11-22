---
layout: plugin

id: psucontrol_momentarygpio
title: OctoPrint-PSUControl-MomentaryGpio
description: A sub-plugin for PSUControl. Adds a momentary option to PSUControl power controls that sends a signal for a
  brief time rather than continuous. Useful for bistable relays.
authors:
- Justin Zak
license: AGPLv3

date: 2023-11-22

homepage: https://github.com/irotsoma/OctoPrint-PSUControl-MomentaryGpio
source: https://github.com/irotsoma/OctoPrint-PSUControl-MomentaryGpio
archive: https://github.com/irotsoma/OctoPrint-PSUControl-MomentaryGpio/archive/master.zip

tags:
- relay
- bistable
- power
- psu
- control
- psucontrol
- psucontrol subplugin
- gpio

screenshots:
- url: /assets/img/plugins/psucontrol_momentarygpio/momentarygpio_screenshot.png
  alt: plugin settings screenshot
  caption: Settings screen for plugin
- url: /assets/img/plugins/psucontrol_momentarygpio/psucontrol_screenshot.png
  alt: PSUControl settings plugin screenshot
  caption: Settings screen for PSUControl plugin

featuredimage: /assets/img/plugins/psucontrol_momentarygpio/momentarygpio_screenshot.png
compatibility:
  os:
  - linux
  python: ">=3,<4"

---

A sub-plugin for the PSUControl plugin that allows using bistable relays for power control. It implements
the same mechanisms as PSUControl, so it requires python periphery to be installed, only it pulls the GPIO
up/down only momentarily and then returns it to the default state.

### Instructions

- Set the PSUControl Switching Method to "Plugin" and select "PSUControl MomentaryGpio Plugin" from the dropdown

- Then in the PSUControl MomentaryGpio Plugin settings screen, set the appropriate GPIO Device, PIN, and pulse time in
milliseconds.

http://plugins.octoprint.org/plugin/psucontrol_momentarygpio/
