---
layout: plugin

id: prusaslicerthumbnails
title: PrusaSlicer Thumbnails
description: Extracts embedded thumbnails from PrusaSlicer gcode files.
author: jneilliii
license: AGPLv3

date: 2020-04-22

homepage: https://github.com/jneilliii/OctoPrint-PrusaSlicerThumbnails
source: https://github.com/jneilliii/OctoPrint-PrusaSlicerThumbnails
archive: https://github.com/jneilliii/OctoPrint-PrusaSlicerThumbnails/archive/master.zip

follow_dependency_links: false

tags:
- thumbnail
- preview
- PrusaSlicer

compatibility:
  python: ">=2.7,<4"

featuredimage: /assets/img/plugins/prusaslicerthumbnails/screenshot_thumbnail.png

---

# PrusaSlicer Thumbnails

This plugin will extract the embedded thumbnails from PrusaSlicer gcode files where the printer's profile ini file has the thumbnail option configured. This is default behavior for the Prusa Mini printer profile. 

The thumbnail image extracted will always be the last resolution provided in the thumbnail setting. So for example the Prusa Mini setting is `thumbnail=16x16,220x124` so the thumbnail that will be extracted will be 220x124 pixels as seen in the screenshots below. See the Configuration section below for additional details.

The preview thumbnail can be shown in OctoPrint from the files list by clicking the newly added image button.

![button](/assets/img/plugins/prusaslicerthumbnails/screenshot_button.png)

The thumbnail will open in a modal window.

![thumbnail](/assets/img/plugins/prusaslicerthumbnails/screenshot_thumbnail.png)

If enabled in settings the thumbnail can also be embedded as an inline thumbnail within the file list itself. If you use this option it's highly recommended to use Themify to make the file list taller and/or adjust the thumbnail's size.  The image selector for this in Themeify should be `div.row-fluid.inline_prusa_thumbnail > img` but I haven't yet tested personally.

![thumbnail](/assets/img/plugins/prusaslicerthumbnails/screenshot_inline_thumbnail.png)

## Configuration

Since PrusaSlicer only enables thumbnails by default for the Prusa Mini you may need to manually update your configuration files. Those can be found by selecting Show Configuration Folder from the Help menu of the application and then inside the printers sub-folder you'll find your printer profiles. 

Open your desired printer profile in your favorite text editor and find the `thumbnail=` section and add the resolution that you would like to include in your sliced files, and therefore visible by this plugin. For example `thumbnail=16x16,220x124` will be the equivalent of the Prusa Mini as described above.

**Warning**: the higher the resolution of the thumbnail you enter in this setting the larger your gcode file will be when sliced.

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

### Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip if you find this plugin helpful.

[![paypal](/assets/img/plugins/prusaslicerthumbnails/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>