---
layout: plugin

id: physicalbutton
title: Physical Button
description: Add physical buttons to OctoPrint
authors:
- LuxuSam
license: AGPLv3

date: 2021-08-01

homepage: https://github.com/LuxuSam/PhysicalButton/tree/master
source: https://github.com/LuxuSam/PhysicalButton/tree/master
archive: https://github.com/LuxuSam/PhysicalButton/archive/master.zip

tags:
- physical
- button
- buttons
- input
- gpio
- pins
- external
- send
- action
- actions
- gcode
- system

screenshots:
- url: /assets/img/plugins/physicalbutton/PhysicalButton_action.png
  alt: Image that shows an action activity of a button.
  caption: An exemplary action activity for a button.
- url: /assets/img/plugins/physicalbutton/PhysicalButton_gcode.png
  alt: Image that shows a gcode activity of a button.
  caption: An exemplary GCODE activity of a button.
- url: /assets/img/plugins/physicalbutton/PhysicalButton_system.png
  alt: Image that shows a system activity of a button.
  caption: An exemplary system activity of a button.
- url: /assets/img/plugins/physicalbutton/PhysicalButton_delete.png
  alt: Image that shows a modal to confirm the deletion of a configured button.
  caption: Before deleting a button you have to confirm the deletion.

featuredimage: /assets/img/plugins/physicalbutton/PhysicalButton_Logo.png


compatibility:

  #octoprint:
  #- 1.2.0
  os:
  - linux
  python: ">=3,<4"

---
The **PhysicalButton** plugin (hence the name) lets you add physical buttons to your Raspberry Pi.
The buttons are then able to send GCODE and actions to your printer.

----
### Configuring a new button
* **Button Name**
  * This is where you put the name of your button to differentiate them in the list of buttons.
* **GPIO**
  * This is the GPIO you connect your button to, the other cable has to be connected to a ground pin (Buttons are configured to use internal pulled-up resistors). You can only create one button per GPIO.
* **Mode**
  * Depending on your button setup or wiring you have to choose between the two modes.
  * Normally Open (NO)
    * Use this mode if your button is usually not pressed (open).
  * Normally Closed (NC)
    * Use this mode if your button is usually pressed (closed).
* **Hold Time**
  * This is where you set the hold time for your button, meaning how long the button has to be held until the reaction is triggered.
* **Choose activities for your button**
  * Action:
    * You can choose between the standard actions of OctoPrint (cancel, connect, disconnect, home (x, y and z are homed), pause, resume and start).
  * GCODE:
    * You can input any GCODE.
  * System:
    * You can input any system command for your Octoprint host.
  * These activities will be executed in order of your list. You can also rearrange them by inserting them at your desired position.

----
### ⚠️ Use at your own risk ⚠️
  I am not accountable for any damages made to your printer/raspberry pi when using this plugin (e.g. wrong wiring
  of buttons, GCODE or system commands that you send with the buttons to your printer, ...).

----
### Get Help / Feature request
If you encounter problems using the plugin or if you have an idea for a new feature please use the [issue tracker](https://github.com/LuxuSam/PhysicalButton/issues) and if applicable add the corresponding label.

----
### ❤️ Support me❤️
If you enjoy my plugin and want to support me and the development, you can do so by sending me a donation on

[![paypal](https://www.paypalobjects.com/webstatic/de_DE/i/de-pp-logo-100px.png)](https://www.paypal.com/paypalme/luxusam3d)&emsp;&emsp;[![ko-fi](https://uploads-ssl.webflow.com/5c14e387dab576fe667689cf/5c91bddac6c3aa6b3718fd86_kofisvglofo.svg)](https://ko-fi.com/C0C14BZCR)
