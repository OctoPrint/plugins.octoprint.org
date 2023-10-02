---
layout: plugin

id: prusammu
title: Prusa MMU
description: This plugin adds Prusa MMU support to OctoPrint. The active filament will be displayed in the navbar and you will be prompted to select which filament to use when slicing in "MMU Single" mode. Other settings are available to name each tool and set defaults. This plugin only works for Prusa printers with an MMU. Supports MMU firmware 1.X.X and 3.X.X.
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
- mmu2s
- mmu3
- multi

screenshots:
- url: /assets/img/plugins/prusammu/modal.png
  alt: Dialog that opens to select the filament to use.
  caption: Dialog that opens to select the filament to use.
- url: /assets/img/plugins/prusammu/nav.png
  alt: Navbar showing the MMU state.
  caption: Navbar showing the MMU state.
- url: /assets/img/plugins/prusammu/error.png
  alt: An error popup on MMU failure.
  caption: An error popup on MMU failure.
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

## Highlighted Featured
- Displays MMU state in the navbar (configurable)
- (Optional) Default to a filament if none are selected
- On single color prints, shows a modal to select the filament within Octoprint
- Displays an error popup when the MMU throws an error (Only when running 3.0.0+)
- Supports retrieving filament data from [Spool Manager](https://plugins.octoprint.org/plugins/SpoolManager/)
  and [Filament Manager](https://plugins.octoprint.org/plugins/filamentmanager/) if installed.

## GCode Interactions

This plugin does some minimal gcode manipulation. This is how it detects tool events and pause the
print to provide the dialog.

The command interactions are as follows:
- Before sent: (gcode_queuing_hook)
  - `Tx`: When the GCODE would send a `Tx` (tool change) it first triggers the modal and then does
    not send the `Tx` command. Instead, it sends a pause event to the printer. This results in Prusa
    not prompting for a tool change. If the timeout time is reached (`_timeout_prompt`) then the
    plugin resends the `Tx` command to allow Prusa to prompt the user.
  - `M109`: When the GCODE would send an `M109` (Wait for Hotend Temperature) and the user has
    selected a filament it sends both the `M109` and `T#` (like `T2`), otherwise it just sends the
    `M109`.
- After sent: (gcode_sent_hook)
  - When the plugin notices a `T#` command it sets the tool internally, so it can be used to
    display. This is to support multicolor printing. This trigger is also used to show unloading.

### MMU2 1.X.X

It listens to printer responses and does some substring matching. This is done to identify filament
events and printer notifications, so it can update the navbar: (gcode_received_hook)
  - `paused for user` - Used to show that the printer needs attention (either error or waiting for
    tool selection at printer).
  - `MMU not responding` -  Used to show that the printer needs attention because of an MMU failure.
  - `MMU - ENABLED` / `MMU starts responding` - Used to show printer is "OK".
  - `MMU can_load` / `Unloading finished` - Used to show the filament loading message.
  - `OO succeeded` - Used to show what filament is loaded.

### MMU2/3 3.X.X

The MMU 3.X.X firmware communicates continuously with the printer. The printer sends the MMU
requests, and the MMU sends back responses. The MMU's responses start with the request letter and
data, so it just listens for the Responses.

MMU 3.X.X responses come in this format:  
`MMU2:<(Request Letter)(Request Data) (Response Letter)(Response Data)`
  - `(Request Letter)` - A single letter code that represents a request sent from the printer to the MMU.
    - It only listens for `T` - Tool, `L` - Load, `U` - Unload, `X` - Reset, `K` - Cut, and `E` - Eject.
  - `(Request Data)` - Hexidecimal data that follows the Request Letter.
    - It's usually `0`, unless the request involves filament, in which case it is the filament number `[0-4]`.
  - `(Response Letter)` - A single letter code that represents a response from the MMU.
    - Possible responses are `P` - Processing, `E` - Error, `F` - Finished, `A` - Accepted,
      `R` - Rejected, and `B` - Button.
  - `(Response Data)` - Hexidecimal data that follows the Response Letter.
    - The amount of data varies depending on the Request Letter and Response Letter.
    - We only use Response Data to decode `P` - Progress messages, and `E` - Error messages

Several Regex strings are used to parse the MMU 3.X.X responses:
  - `MMU2:<[TLUXKE]` - Generic Regex used to catch the responses with the Request Letters that are important.
  - `MMU2:<([TLUXKE])(.*) ([PEFARB])(.*)\*` - Used to split the command into the four groups described above.

Additionally, it also listens for these lines:
  - `MMU2:Saving and parking` - Used to detect when the printer is waiting for user input after the
    MMU fails at auto-retrying after an Error.
  - `MMU2:Heater cooldown pending` - The same as above. Might be unnecessary, but included just in case.
  - `LCD status changed` - If the printer was paused, this indicates that the pause is probably over.

For all instances where command manipulation happens see `__init__.py` for `Gcode Hooks`. Also
look at function `_timeout_prompt` where it handles unpausing the printer after the timer and either
sending a `Tx` or `T#` if `useDefaultFilament` and `defaultFilament` settings are set.

More documentation is available [here](https://github.com/jukebox42/Octoprint-PrusaMMU#developer-zone).

## Known Bugs

1. In rare instances, the "waiting for user input" event can come in directly after a tool change is
   sent, resulting in the navbar never updating. This will not impact printing, but you will see
   "Awaiting user input" until the next tool change.
1. If the Prusa printer prompts the user for a "new version", the select filament modal may not
   display. You will still be able to select the filament directly on the printer.

## Useful Link
- [MMU2 Commands](https://cfl.prusa3d.com/display/PI3M3/MMU2+commands)
- [Debugging MMU2](https://revilor.github.io/MMU2-Marlin/debugging.html)
- [MMU2 LEDs Meaning](https://help.prusa3d.com/article/mmu2s-leds-meaning_2187#red-light)
- [Octoprint Plugin Docs](https://docs.octoprint.org/en/master/plugins/mixins.html)
