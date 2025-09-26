---
layout: plugin

id: btt_touch_support
title: BTT TFT TouchScreen Firmware Support
description: Support for the BTT TFT touchscreen firmware
authors:
- Jounathaen
license: AGPLv3

date: 2024-11-24

homepage: https://github.com/jounathaen/octoprint_btt_touch_support
source: https://github.com/jounathaen/octoprint_btt_touch_support
archive: https://github.com/jounathaen/octoprint_btt_touch_support/archive/master.zip

#privacypolicy: your plugin's privacy policy URL

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
follow_dependency_links: false

tags:
- display
- touchscreen
- action commands


featuredimage: /assets/img/plugins/btt_touch_support/btt_touchscreen.jpg

compatibility:
  python: ">=2.7,<4"

---

# OctoPrint-BTT TFT Touchscreen Firmware support

This plugin adds support for the remote printing features of the [BigTreeTech TFT
Touchscreen Firmware's](https://github.com/bigtreetech/BIGTREETECH-TouchScreenFirmware)
_Touch Mode_ for [OctoPrint](https://github.com/OctoPrint/OctoPrint).

This plugin does *not* interact with the firmware's _Marlin Mode_ - a normal serial connection between the TFT and the printer is sufficient.

Features:

- Automatically switch to printing mode on the TFT upon print start.
- Update the progress indicator on the TFT during print.
- Update the remaining time on the TFT during print.
- Update the Layer progress on the TFT (requires [DisplayLayerProgress](/plugins/DisplayLayerProgress))
- React to the TFT's _Pause_, _Resume_ and _Cancel_ buttons on in OctoPrint.

This is a fork of the [M73Progress plugin](https://github.com/cesarvandevelde/OctoPrint-M73Progress), created by [Cesar Vandevelde](/by_author/#cesar-vandevelde)!

{:refdef: style="text-align: center;"}
![BTT TFT Touchscreen during an OctoPrint
print](/assets/img/plugins/btt_touch_support/btt_touchscreen.jpg){: width="50%" }
{: refdef}

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/jounathaen/octoprint_btt_touch_support/archive/master.zip

## Configuration

You can fine-tune the plugin's behavior in the `BTT TFT Touchscreen` tab in the OctoPrint settings (don't forget to **restart** OctoPrint to apply changes):

* **Use time estimate**: By default, the plugin uses OctoPrint's built-in progress
  estimate, which is based on the progress inside a G-code file. In some cases,
  a better progress estimate can be calculated from the time elapsed and the
  time remaining: `P = elapsed / (elapsed + remaining)`. This option is
  particularly useful for
  [PrintTimeGenius](https://github.com/eyal0/OctoPrint-PrintTimeGenius) users.
* **Serial Port Number**: The number of the serial port the TFT is connected to. If it is set to `0` (default), all serial ports will be used, which could lead to issues if other plugins also utilize action commands.

  (Typically, your printer has two serial ports `1` and `2`, of which one is the connected to your OctoPrint host and the other one to the TFT)
