---
layout: plugin

id: ws281x_led_status
title: WS281x LED Status
description: Add some WS281x type RGB LEDs to your printer for a quick status update!
author: Charlie Powell
license: AGPLv3

date: 2020-07-28

homepage: https://github.com/cp2004/OctoPrint-WS281x_LED_Status
source: https://github.com/cp2004/OctoPrint-WS281x_LED_Status
archive: https://github.com/cp2004/OctoPrint-WS281x_LED_Status/releases/latest/download/release.zip

follow_dependency_links: false

tags:
- rgb led
- led
- status
- progress
- neopixel
- ws281x
- ws2811
- ws2812
- sk6812

screenshots:
- url: /assets/img/plugins/ws281x_led_status/ws281x_settings.png
  alt: settings-overview-screenshot
  caption: Settings Overview Screenshot
- url: /assets/img/plugins/ws281x_led_status/ws281x_wizard.png
  alt: setup-wizard-screenshot
  caption: Setup Wizard Screenshot

featuredimage: /assets/img/plugins/ws281x_led_status/ws281x_settings.png

compatibility:

  octoprint:
  - 1.4.0

  os:
  - linux

  python: ">=2.7,<4"

---

![rainbow effect](/assets/img/plugins/ws281x_led_status/rainbow.gif)

A highly configurable plugin for supporting WS2811, WS2812 and SK6812 LEDs attached to your Raspberry Pi.

With lots of effects to choose from, you can customise the plugin to do things *exactly* as you want them, to display the status from your 3D printer from a simple strip of LEDs

Features include:
* Reacting to printing events
* Tracking heating & printing progress
* Intercepting M150 commands
* Quick on/off button from the navbar
* 'Torch' button
* A timer to turn the LEDs on or off at certain times
* Easy to use but highly configurable settings interface, you can turn pretty much anything on or off.
* LED Strip test
* Power calculator
* ... and more!

For the most up-to-date feature list, please checkout the [plugin's homepage]({{ page.homepage }}) as well as the [documentation](https://cp2004.gitbook.io/ws281x-led-status/) for more information.

![rainbow effect](/assets/img/plugins/ws281x_led_status/color_wipe.gif)

## Setup

Setting up the plugin couldn't be easier! There are 3 main steps, with the heavy lifting done for you via a configuration wizard:

* Wiring your LEDs
* Configuring SPI
* Configuring plugin settings

Like the sound of it? Follow the detailed [setup guide](https://cp2004.gitbook.io/ws281x-led-status/guides/setup-guide-1) in the documentation.

### Getting help

Please read the [Get Help Guide](https://cp2004.gitbook.io/ws281x-led-status/guides/get-help-guide) as well as the [rest of the documentation](https://cp2004.gitbook.io/ws281x-led-status/), to see if your question has been answered there. Still got questions? Get in touch:

* On the [OctoPrint Discord](https://discord.octoprint.org)
* On the [Community Forums](https://community.octoprint.org)
* Open an issue with the [question template]({{ page.homepage }}/issues/new?assignees=&labels=question&template=question.md&title=)


### Reporting problems
Whilst I don't like bugs, I want to hear about them! Let me know by [opening an issue on Github]({{ page.homepage }}/issues/new?assignees=&template=bug_report.md&title=%5BBug%5D)

Before you report a bug, please read the [Get Help Guide](https://cp2004.gitbook.io/ws281x-led-status/guides/get-help-guide) as well, there is a section on reporting bugs.


# Support my work!
I created this plugin in my spare time, so if you have enjoyed using it then please [support it's development!](https://github.com/sponsors/cp2004)
