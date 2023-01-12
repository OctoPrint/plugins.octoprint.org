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

  python: ">=3.7,<4"

---

![rainbow effect](/assets/img/plugins/ws281x_led_status/rainbow.gif)

A highly configurable yet easy to use plugin for attaching WS2811, WS2812 and SK6812 or LEDs to your Raspberry Pi for a printer status update!

With lots of options effects and integrations to choose from, you can customise the plugin to do things _exactly_ as you want them.

Most prominent features include:

- Printer status effects
- Tracking heating, printing and cooling progress
- Intercepting M150 commands & controlling with @ commands
- Easy controls for turning lights on and off from the navbar
- Theme-friendly torch button to temporarily light up your printer
- Timers to turn the LEDs off at certain times of day or after a print is done.
- Custom Triggers - add your own events, @ commands or gcode matching to trigger effects
- Powerful integration with OctoApp for Android
- ...and more!

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
