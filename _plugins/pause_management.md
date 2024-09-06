---
layout: plugin

id: pause_management
title: Pause Management
description: Plugin allowing to ignore upcoming pauses in gcode or add additional pauses while printing.
author: jneilliii
license: AGPLv3

date: 2024-01-22

homepage: https://github.com/jneilliii/OctoPrint-PauseManagement
source: https://github.com/jneilliii/OctoPrint-PauseManagement
archive: https://github.com/jneilliii/OctoPrint-PauseManagement/archive/master.zip

tags:
- M600
- pause
- gcode
- ignore
- skip

compatibility:
  python: ">=3,<4"

featuredimage: /assets/img/plugins/pause_management/screenshot_sidebar.png

---

# Pause Management

Plugin allowing to ignore upcoming pauses in gcode or add additional pauses while printing.

## Operation

![sidebar screenshot](/assets/img/plugins/pause_management/screenshot_sidebar.png)

Use the toggle button in the sidebar to ignore pre-existing configurable pause command, see Settings below.

Use the + button to inject a configurable pause command at provided height or layer number, see Settings section below.


## Settings

![screenshot settings](/assets/img/plugins/pause_management/screenshot_settings.png)

- `Pause Command to Ignore`: Configure this setting to match the pause command used by your slicer. This is what will be ignored when the toggle button in the sidebar is enabled.
- `Pause Command to Inject`: Configure this setting as the pause command that you want to send at given pause positions in the sidebar.
- `Layer Indicator`: Configure this setting to match the custom command added to your slicer to let the plugin know what height or layer number the print is at. This is used to match against the pause positions added in the sidebar. See the Slicer Setup section below for more details.

## Slicer Setup

In order for the injection of pause commands to work a configurable layer indicator needs to be added to your slicer's before layer change gcode script.


### PrusaSlicer

For PrusaSlicer that setting can be found in Printer Settings > Custom G-code. You have a couple of options to use based on how you want to enter pause positions in the sidebar.

- **Height**: `@PAUSE_POSITION [layer_z]`
- **Layer Number**: `@PAUSE_POSITION [layer_num]`

![prusa screenshot](/assets/img/plugins/pause_management/screenshot_prusa.png)

### Cura

Thanks to [@CortezSMz](https://github.com/CortezSMz) for this information, setup in Cura will require the Search and Replace post-processing script with the following settings.

- Search: `\;LAYER\:(\d+)`
- Replace: `;LAYER:\1\n@PAUSE_POSITION \1`
- Use Regular Expressions: _must_ be checked.

![prusa screenshot](/assets/img/plugins/pause_management/screenshot_cura.png)

---

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

### Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip or become a Patron if you find this plugin helpful and want me to continue future development.

[![Patreon](/assets/img/plugins/pause_management/patreon-with-text-new.png)](https://www.patreon.com/jneilliii) [![paypal](/assets/img/plugins/pause_management/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>
