---
layout: plugin

id: prusammu
title: Prusa MMU
description: This plugin adds Prusa MMU2 support to OctoPrint. The active filament will be displayed in the navbar and you will be prompted to select which filament to use when slicing in "MMU2S Single" mode. Other settings are available to name each tool and set defaults. This plugin only works for a Prusa printer with an MMU2.
authors:
- jukebox42
license: AGPLv3

date: 2022-08-01

homepage: https://github.com/jukebox42/Octoprint-PrusaMMU
source: https://github.com/jukebox42/Octoprint-PrusaMMU
archive: https://github.com/jukebox42/Octoprint-PrusaMMU/releases/latest/download/Octoprint-PrusaMmu.zip

follow_dependency_links: false

tags:
- prusa
- mmu
- mmu2

screenshots:
- url: /assets/img/plugins/prusammu/modal.png
  alt: Dialog that opens to select the filament to use.
  caption: Dialog that opens to select the filament to use.
- url: /assets/img/plugins/prusammu/nav.png
  alt: Navbar showing the MMU state.
  caption: Navbar showing the MMU state.
- url: /assets/img/plugins/prusammu/settings.png
  alt: Settings configuration options.
  caption: Settings configuration options.

featuredimage: /assets/img/plugins/prusammu/nav.png

compatibility:
  python: ">=3,<4"
  octoprint:
  - 1.8.0
  - 1.8.1

---

This plugin adds Prusa MMU2 support to OctoPrint. The active filament will be
displayed in the navbar and you will be prompted to select which filament to use when slicing in
"MMU2S Single" mode. Other settings are available to name each tool and set defaults. This plugin
only works for a Prusa printer with an MMU2.

## Configuration

- Set a timeout to auto-select an extruder
- Enable/disable extruders, name them and give them a color
- Show/hide navbar item (and simplify the display)

## Known Bugs

1. In rare instances, the "waiting for user input" event can come in directly after a tool change is
   sent, resulting in the navbar never updating. This will not impact printing but you will see
   "Awaiting user input" until the next tool change.
1. If the Prusa printer prompts the user for a "new version", the select filament modal may not
   display. You will still be able to select the filament directly on the printer.
1. If settings are saved mid-print the navbar will forget the state of the MMU. This does not impact
   printing but is rather annoying. It'll remember the next time the tool changes.

## Implementation Notes

This plugin does some minimal gcode manipulation. This is how it detects tool events.

The command interactions are as follows:
- Before sent: (gcode_queuing_hook)
  - `Tx`: When the GCODE would send a `Tx` (tool change) it first triggers the modal and then does
    not send the Tx command. Instead it sends a pause event to the printer. This results in Prusa
    not prompting for a tool change. If the timeout time is reached (`_timeout_prompt`) then the
    plugin resends the `Tx` command to allow Prusa to prompt the user.
  - `M109`: When the GCODE would send an `M109` (Wait for Hotend Temperature) and the user
    has selected a filament we send both the `M109` and `T#` (like `T2`), otherwise we just send the
    `M109`.
- After sent: (gcode_sent_hook)
  - When the plugin notices a `T#` command we set the tool internally so it can be used to
    display. This is to support multi-color printing. This trigger is also used to show unloading.

We listen to printer responses and do some substring matching. This is done to identify filament
events and printer notifications so we can update the navbar: (gcode_received_hook)
  - `paused for user` - Used to show that the printer needs attention (eithe error or waiting for
    tool selection at printer).
  - `MMU not responding` -  Used to show that the printer needs attention because of an MMU failure.
  - `MMU - ENABLED` / `MMU starts responding` - Used to show printer is "OK".
  - `MMU can_load` - Used to show the filament loading message.
  - `OO succeeded` - Used to show what filament is loaded.

For all instances of where command manipulation happens see `__init__.py` for `Gcode Hooks`. Also
look at function `_timeout_prompt` where we handle unpausing the printer after the timer and either
sending a `Tx` or `T#` if `useDefaultFilament` and `defaultFilament` settings are set.

## Useful Link
- [MMU2 Commands](https://cfl.prusa3d.com/display/PI3M3/MMU2+commands)
- [Debugging MMU2](https://revilor.github.io/MMU2-Marlin/debugging.html)
- [MMU2 LEDs Meaning](https://help.prusa3d.com/article/mmu2s-leds-meaning_2187#red-light)
- [Octoprint Plugin Docs](https://docs.octoprint.org/en/master/plugins/mixins.html)
