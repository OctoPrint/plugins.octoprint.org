---
layout: plugin

id: usb_keyboard
title: USB Keyboard
description: Use a USB Keyboard to control your printer and Octoprint!
authors:
- Barrett Ford
license: GPL-3.0 License

date: 2021-01-20

homepage: https://github.com/barrettford/Octoprint-Usb_keyboard
source: https://github.com/barrettford/Octoprint-Usb_keyboard
archive: https://github.com/barrettford/Octoprint-Usb_keyboard/archive/master.zip

tags:
- usb
- keyboard
- control
- printer
- configure
- gcode
- macros
- psu
- plugin

screenshots:
- url: /assets/img/plugins/usb_keyboard/example_qwerty.png
  alt: Example QWERTY Keyboard configuration
  caption: An example of how to represent a QWERTY keyboard
- url: /assets/img/plugins/usb_keyboard/example_10key_evdev_keyboard.png
  alt: Example 10-Key Keyboard configuration
  caption: An example of how to represent a 10-Key keyboard
- url: /assets/img/plugins/usb_keyboard/example_10key_evdev_commands.png
  alt: Example 10-Key Keyboard commands
  caption: You can set command macros for each key on your keyboard
- url: /assets/img/plugins/usb_keyboard/example_10key_evdev_variables.png
  alt: Example 10-Key Keyboard variables
  caption: You can set variables, with defaults, for use in your commands
- url: /assets/img/plugins/usb_keyboard/example_octoprint.png
  alt: Example Octoprint command
  caption: You can start/stop/pause/resume prints
- url: /assets/img/plugins/usb_keyboard/example_gcode.png
  alt: Example Printer commands with Gcode
  caption: You can define and trigger arbitrary gcode commands
- url: /assets/img/plugins/usb_keyboard/example_variables.png
  alt: Example Variable listening command with Gcode
  caption: You can modify defined variables on-the-fly and use them in your gcode
- url: /assets/img/plugins/usb_keyboard/example_psu_plugin.png
  alt: Example PSUControl Plugin command
  caption: You can use it to turn your PSU on and off


featuredimage: /assets/img/plugins/usb_keyboard/example_qwerty.png

compatibility:
  python: ">=3,<4"

---

#### Life

3D printer interfaces are a pain to navigate using that encoder wheel.
Octoprint's interface always seems to take forever to reload on a tablet.
Wouldn't it be nice if you just had some easy hardware buttons to do those simple things you do all the time?

#### Wait no more!

A fully configurable USB Keyboard plugin has arrived!

## Features
* Fully customizable keyboard key layouts with self-assigned keys/keycodes
* Several configurable command types including arbitrary gcode and variable manipulation
* Documentation found in-settings. Look for the \[i\] buttons!
* Keyboard troubleshooting and setup tools
* Keyboard Profiles and easy profile duplication






