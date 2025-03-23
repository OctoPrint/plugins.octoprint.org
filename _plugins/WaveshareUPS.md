---
layout: plugin

id: WaveshareUPS
title: OctoPrint-WaveshareUPS
description: An OctoPrint plugin to support the Waveshare UPS HAT
authors:
- Michael Szubartowicz
license: MIT

# TODO
date: 2025-03-16

homepage: https://github.com/michaelszubartowicz/OctoPrint-WaveshareUPS
source: https://github.com/michaelszubartowicz/OctoPrint-WaveshareUPS
archive: https://github.com/michaelszubartowicz/OctoPrint-WaveshareUPS/archive/main.zip

follow_dependency_links: false

tags:
- UPS
- octopi
- Raspberry
- Pi
- battery

# TODO
# When registering a plugin on plugins.octoprint.org, all screenshots should be uploaded not linked from external sites.
screenshots:
- url: /assets/img/plugins/WavershareUPS/Screenshot_1.png
  alt: Screenshot of the plugin interface
  caption: Navbar icon including tooltip showing battery status
- url: /assets/img/plugins/WavershareUPS/Screenshot_2.png
  alt: Screenshot of the plugin interface
  caption: Navbar icon showing UPS is powered


featuredimage: /assets/img/plugins/WavershareUPS/featured.jpeg


compatibility:
  octoprint:
  - 1.4.0

  os:
  - linux
  - windows
  - macos
  - freebsd

  python: ">=3,<4"

# TODO
# If any of the below attributes apply to your project, uncomment the corresponding lines. This is MANDATORY!

attributes:
#  - cloud  # if your plugin requires access to a cloud to function
#  - commercial  # if your plugin has a commercial aspect to it
#  - free-tier  # if your plugin has a free tier

---

An OctoPrint plugin to support the Waveshare UPS HAT, providing real-time monitoring of battery status and power supply. The plugin displays the battery percentage, power supply status, and estimated remaining runtime. It also sends notifications when the battery is critically low.

### Configuration
1. Install the plugin via the OctoPrint plugin manager.
2. Connect the Waveshare UPS HAT to your Raspberry Pi.

### Features
- Real-time battery status monitoring
- Power supply status indication
- Estimated remaining runtime calculation
- Low battery notifications
