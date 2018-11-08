---
layout: plugin

id: TerminalCommands
title: OctoPrint-TerminalCommands
description: Lets you add custom G-code command buttons to OctoPrint's Terminal view tab
author: ieatacid
license: AGPLv3

date: 2017-12-31

homepage: https://github.com/ieatacid/OctoPrint-TerminalCommands
source: https://github.com/ieatacid/OctoPrint-TerminalCommands
archive: https://github.com/ieatacid/OctoPrint-TerminalCommands/archive/master.zip

tags:
- terminal
- command
- commands
- gcode
- ui

screenshots:
- url: /assets/img/plugins/TerminalCommands/terminal_tab.png
  alt: Terminal tab with command buttons
- url: /assets/img/plugins/TerminalCommands/terminal_commands_settings.png
  alt: Terminal Commands settings

featuredimage: /assets/img/plugins/TerminalCommands/terminal_tab.png

compatibility:

  octoprint:
  - 1.2.0

  os:
  - linux
  - windows
  - macos
  - freebsd

---

Buttons are inserted between the terminal command input and the terminal filters. Currenty only supports G-code commands that you can send through the terminal.

Multiple commands can be bound to one button by separating them with a semicolon (;) e.g. `M114; M503` (spaces before or after the semicolon are fine)
