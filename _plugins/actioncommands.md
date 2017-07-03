---
layout: plugin

id: actioncommands
title: Action Commands
description: Adds handling for user-definable action commands.
author: Ben Lye
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2017-06-30

homepage: https://github.com/benlye/OctoPrint-ActionCommandsPlugin
source: https://github.com/benlye/OctoPrint-ActionCommandsPlugin
archive: https://github.com/benlye/OctoPrint-ActionCommandsPlugin/archive/master.zip

tags:
- action
- actions
- commands
- action command

screenshots:
- url: /assets/img/plugins/actioncommands/settings.png
  alt: Action Commands Settings
  caption: Action Commands Settings

featuredimage: /assets/img/plugins/actioncommands/settings.png

---

Adds handling for custom action commands to OctoPrint. Action commands are sent from the RepRap machine in the form `//action:command`.

The plugin allows OctoPrint to execute a system command or send G-code to the printer in response to an action command.

## Usage
As of the latest Marlin bugfix-1.1.x version, the command `M118` can be used to echo output to serial, meaning that `M118 //action:dostuff` would cause this plugin to try to handle the `dostuff` command when `//action:dostuff` was echoed back on the serial console.

A future application of the plugin would be to add actions in the RepRap machine's firmware so that hosts could respond.  For example, when Marlin is killed because something is wrong it would echo `//action:poweroff` and the attached OctoPrint instance could use this action command to trigger the printer's power outlet to switch off.

## Action Command References
* [OctoPrint Documentation](http://docs.octoprint.org/en/master/features/action_commands.html)
* [RepRap Wiki](http://reprap.org/wiki/Gcode#Replies_from_the_RepRap_machine_to_the_host_computer)