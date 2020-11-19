---
layout: plugin

id: marlingcodedocumentation
title: MarlinGcodeDocumentation
description: Provides documentation for Marlin & RepRap GCode commands in the Terminal tab
author: Costas Basdekis
license: AGPLv3

date: 2020-09-27

homepage: https://github.com/costas-basdekis/MarlinGcodeDocumentation
source: https://github.com/costas-basdekis/MarlinGcodeDocumentation
archive: https://github.com/costas-basdekis/MarlinGcodeDocumentation/archive/master.zip

tags:
- terminal
- gcode
- marlin
- reprap
- documentation

screenshots:
- url: /assets/img/plugins/marlingcodedocumentation/screenshot-example-command.png
  alt: Example of a command
  caption: Example of a command
- url: /assets/img/plugins/marlingcodedocumentation/screenshot-example-multiline-commands.png
  alt: Example of multiple commands in different lines
  caption: Example of multiple commands in different lines
- url: /assets/img/plugins/marlingcodedocumentation/screenshot-example-search.png
  alt: Example of search
  caption: Example of search
- url: /assets/img/plugins/marlingcodedocumentation/screenshot-example-favourites.png
  alt: Example of favourites
  caption: Example of favourites
- url: /assets/img/plugins/marlingcodedocumentation/screenshot-example-sent.png
  alt: Example of help for sent commands
  caption: Example of help for sent commands

featuredimage: /assets/img/plugins/marlingcodedocumentation/screenshot-example-command.png

compatibility:
  python: ">=2.7,<4"

---

It displays GCode documentation for Marlin & RepRap in the terminal command line.

Type a command and you will get explanation for the command and the parameters.

Type '?' and some terms and you'll be shown commands that reference those terms.

Features:
* Commands from [Marlin](https://marlinfw.org/meta/gcode/) & [RepRap](https://reprap.org/wiki/G-code#G-commands) official documentations
* Support for search by prepending `?`
* Add and manage favourite commands
* Support for [Multiline Terminal plugin](https://plugins.octoprint.org/plugins/multilineterminal/)
* If you use [Terminal Messaging](https://github.com/jeffeb3/OctoPrint-TerminalMessaging), it allows you to explain sent commands
