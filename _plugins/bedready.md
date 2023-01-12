---
layout: plugin

id: bedready
title: OctoPrint-BedReady
description: Plugin that uses the camera and opencv to determine if the bed matches a reference image indicating that the bed is clear and ready to start a print.
authors:
- jneilliii
license: AGPLv3

date: 2022-04-29

homepage: https://github.com/jneilliii/OctoPrint-BedReady
source: https://github.com/jneilliii/OctoPrint-BedReady
archive: https://github.com/jneilliii/OctoPrint-BedReady/archive/master.zip

tags:
- bed
- clear
- opencv
- collision avoidance
- object detection
- clear
- safety
- automation

featuredimage: /assets/img/plugins/bedready/screenshot_bed_not_ready.png

compatibility:
  octoprint:
  - 1.4.0
  os:
  - linux
  - windows
  - macos
  - freebsd
  python: ">=3.6,<4"

---

# Bed Ready

Plugin that uses the camera and opencv to determine if the bed matches a reference image indicating that the bed is clear and ready to start a print.

![Screenshot Bed Not Ready](/assets/img/plugins/bedready/screenshot_bed_not_ready.png)

For the plugin to work properly add `@BEDREADY` at the beginning of your slicer's start gcode. For best results add gcode to your slicer's end gcode to position the head out of the way for the next comparison.

**NOTE:** Lighting, camera view angle changes, and filament color that is similar to the bed can impact accuracy; adjust the Match Percentage setting below to compensate.

## Configuration

![Settings Screenshot](/assets/img/plugins/bedready/screenshot_settings.png)

Use the Test Snapshot button to compare the currently stored Reference Image with the bed.

![Test Results](/assets/img/plugins/bedready/screenshot_test_results.png)

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

### Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip or become a Patron if you find this plugin helpful and want me to continue future development.

[![Patreon](/assets/img/plugins/bedready/patreon-with-text-new.png)](https://www.patreon.com/jneilliii) [![paypal](/assets/img/plugins/bedready/paypal-with-text.png)](https://paypal.me/jneilliii) [![GitHub](/assets/img/plugins/bedready/github.png)](https://github.com/sponsors/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>
