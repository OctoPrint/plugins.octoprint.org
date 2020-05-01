---
layout: plugin

id: commandsplitter
title: CommandSplitter
description: Splits multiple commands on one line in GCODE files into multiple lines
author: Gina Häußge
license: AGPLv3

date: 2015-06-21

homepage: https://github.com/OctoPrint/OctoPrint-CommandSplitter
source: https://github.com/OctoPrint/OctoPrint-CommandSplitter
archive: https://github.com/OctoPrint/OctoPrint-CommandSplitter/archive/master.zip

follow_dependency_links: false

tags:
- gcode
- preprocessing

compatibility:
  python: ">=2.7,<4"

---

This is a small GCODE preprocessor that makes sure that uploaded GCODE file contain only one command per line.

GCODE allows putting multiple commands on one line, separated by a <code>:</code> (colon). Since it is currently a bit
unclear how firmware should process such lines with regards to included line numbers or checksums, in order to
avoid any confusion this plugin can be used to make sure that all such multi-command-lines in uploaded GCODE files
are split into multiple lines first.

## Example

If an uploaded GCODE file contains these lines:

    G28 X0 Y0 : G28 Z0 ; home all axes
    ; this is a comment with a colon : in the middle
    M117 Hello there \:)

this plugin will turn them into these lines:

    G28 X0 Y0
    G28 Z0; home all axes
    ; this is a comment with a colon in the middle
    M117 Hello there \:)

Note that it will touch neither colons in comments nor escaped ones. Be careful though, it is currently not completely
clear if all firmwares support escaping the colon as shown above. Better not use any : within your commands if possible.
