---
layout: plugin

id: mmu2filamentselect
title: OctoPrint-Mmu2filamentselect
description: Select the filament for Prusa MMU2 when printing in single mode.
authors: 
  - Thomas Köckerbauer
  - Florian Schütte
license: AGPLv3

date: 2019-10-04

homepage: https://github.com/tkoecker/OctoPrint-Mmu2filamentselect
source: https://github.com/tkoecker/OctoPrint-Mmu2filamentselect
archive: https://github.com/tkoecker/OctoPrint-Mmu2filamentselect/archive/master.zip

follow_dependency_links: false

tags:
- prusa
- mmu2
- gcode
- prusa mmu2
- filament
- notification

screenshots:
- url: /assets/img/plugins/mmu2filamentselect/dialog.png
  alt: Picture of the filament selection dialog.
  caption: Dialog which is shown when filament has to be selected.
- url: /assets/img/plugins/mmu2filamentselect/settings2.png
  alt: Picture of the settings dialog.
  caption: The dialog timeout can be set by the user.


featuredimage: /assets/img/plugins/mmu2filamentselect/octoprusa.png

compatibility:
  python: ">=2.7,<4"

---

![logo](/assets/img/plugins/mmu2filamentselect/octoprusa.png)

This plugin shows a dialog to select the filament when a print on a Prusa printer with MMU2 is started in single mode.

The dialog is shown, when the plugin detects a 'Tx' command in the gcode.

So you don't have to go to your printer and select the filament to be used. It can now be done from within Octoprint.

A timeout can be set in the settings (default 30 seconds), after which the dialog is closed. When this happens you have to select the filament on the printer as usual.
