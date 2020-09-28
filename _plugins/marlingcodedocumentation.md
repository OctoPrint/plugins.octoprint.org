---
layout: plugin

id: marlingcodedocumentation
title: MarlinGcodeDocumentation
description: Provides documentation for Marlin GCode commands in the Terminal tab
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

screenshots:
- url: /assets/img/plugins/marlingcodedocumentation/screenshot-example-command.png
  alt: Example of a command
  caption: Example of a command
- url: /assets/img/plugins/marlingcodedocumentation/screenshot-example-multiple-commands.png
  alt: Example of matching multiple commands
  caption: Example of matching multiple commands
- url: /assets/img/plugins/marlingcodedocumentation/screenshot-example-multiline-commands.png
  alt: Example of multiple commands in different lines
  caption: Example of multiple commands in different lines
- url: /assets/img/plugins/marlingcodedocumentation/screenshot-example-search.png
  alt: Example of search
  caption: Example of search

featuredimage: /assets/img/plugins/marlingcodedocumentation/screenshot-example-command.png

compatibility:
  python: ">=2.7,<4"

---

It displays GCode documentation for Marlin in the terminal command line.

Type a command and you will get explanation for the command and the parameters.

Type '?' and some terms and you'll be shown commands that reference those terms.
