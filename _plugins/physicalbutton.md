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
- file
- gcode
- system
- output

screenshots:
- url: /assets/img/plugins/physicalbutton/PhysicalButton_output.png
  alt: Image that shows an output activity of a button.
  caption: An exemplary output activity for a button.
- url: /assets/img/plugins/physicalbutton/PhysicalButton_action.png
  alt: Image that shows an action activity of a button.
  caption: An exemplary action activity for a button.
- url: /assets/img/plugins/physicalbutton/PhysicalButton_gcode.png
  alt: Image that shows a gcode activity of a button.
  caption: An exemplary GCODE activity of a button.
- url: /assets/img/plugins/physicalbutton/PhysicalButton_system.png
  alt: Image that shows a system activity of a button.
  caption: An exemplary system activity of a button.
- url: /assets/img/plugins/physicalbutton/PhysicalButton_file.png
  alt: Image that shows a file activity of a button.
  caption: An exemplary file activity of a button.
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
The buttons are then able to send GCODE, actions and system commands to your printer.

----

### Configuration - Overview
To add a new button you have to click on the ➕. This adds a new button to the end of your list.

From there you should enter a button name, the used GPIO and the mode (NO or NC) of the button.
In addition you have to specify for how long a button has to be held in order to trigger.

The last step is to add activities to your button which are executed in order of the activities list.
You can edit, move or remove activities in the right pane.

----
### Configuration - Detail
* **Button Name**
  * This is where you put the name of your button to differentiate it in the list of buttons.
* **GPIO**
  * This is the GPIO you connect your button to. The other cable has to be connected to a ground pin (Buttons are configured to use internal pulled-up resistors). You can only create one button per GPIO.
* **Mode**
  * Depending on your button setup or wiring you have to choose between the following two modes:
    * Normally Open (NO)
      * Use this mode if your button is usually not pressed (open).
    * Normally Closed (NC)
      * Use this mode if your button is usually pressed (closed).
* **Hold Time**
  * This is where you set the hold time for your button, meaning how long the button has to be held until the reaction is triggered.
* **Choose activities for your button**
  * Action:
    * You can choose between different actions:  
    connect, disconnect, home (x, y and z are homed), pause, resume, start, start latest, cancel, toggle pause-resume, toggle start-cancel, toggle start latest-cancel
  * File:
    * You can specify the path to a file which will be selected.
    * To start the execution of a file, add 'start action' behind the 'file activity'.
    * There are three ways to specify a file:
      * Absolute path to a file:  
        `/home/pi/Some/Folder/Test.gcode`
      * Relative path to a file inside the uploads folder:  
        `Some/Folder/Test.gcode`
      * Path to a file on the SD-card of the printer:  
        `@sd:Some/Folder/Test.gcode`
  * GCODE:
    * You can input any GCODE commands.
  * System:
    * You can input any system command for your Octoprint host.  
    Note that system commands will be run under the same user that owns your OctoPrint service (usually 'pi' for OctoPi) with the same rights and permissions, so you may need to use sudo facilities for certain tasks. Please refer to your OctoPrint host's documentation for details.
  * Output:
    * Generate output on the given GPIO pin for a given amount of time.
    * By setting the time to 0, the output will continue until you toggle it again.
    * The async option lets the output run while also continuing with the next activities.
    * The initial value sets the level of the GPIO pin for startup and settings save.
  * These activities will be executed in order of your list. You can also rearrange them by inserting them at your desired position.

----
### ⚠️ Use at your own risk ⚠️
  I am not accountable for any damages made to your printer/raspberry pi when using this plugin (e.g. wrong wiring
  of buttons, GCODE or system commands that you send with the buttons to your printer, ...).

----
### Get Help / Feature request
If you encounter problems using the plugin or if you have an idea for a new feature please use the [issue tracker](https://github.com/LuxuSam/PhysicalButton/issues) and the corresponding issue template.

----
### ❤️ Support me❤️
If you enjoy my plugin and want to support me and the development, you can do so by sending me a donation on

[![paypal](https://www.paypalobjects.com/webstatic/de_DE/i/de-pp-logo-100px.png)](https://www.paypal.com/paypalme/luxusam3d)&emsp;&emsp;[![ko-fi](https://uploads-ssl.webflow.com/5c14e387dab576fe667689cf/5c91bddac6c3aa6b3718fd86_kofisvglofo.svg)](https://ko-fi.com/C0C14BZCR)
