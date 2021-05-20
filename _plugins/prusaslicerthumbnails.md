---
layout: plugin

id: prusaslicerthumbnails
title: Slicer Thumbnails
description: Extracts various slicer's embedded thumbnails from gcode files.
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

# Slicer Thumbnails

This plugin will extract embedded thumbnails from gcode files created from [PrusaSlicer](#PrusaSlicer), [SuperSlicer](#SuperSlicer), [Cura](#Cura), or [Simplify3D](#Simplify3D).

The preview thumbnail can be shown in OctoPrint from the files list by clicking the newly added image button.

![button](/assets/img/plugins/prusaslicerthumbnails/screenshot_button.png)

The thumbnail will open in a modal window.

![thumbnail](/assets/img/plugins/prusaslicerthumbnails/screenshot_thumbnail.png)

If enabled in settings the thumbnail can also be embedded as an inline thumbnail within the file list itself. If you use this option it's highly recommended to also set the option to set file list height or position inline image to the left.

![thumbnail](/assets/img/plugins/prusaslicerthumbnails/screenshot_inline_thumbnail.png)

## Configuration

### PrusaSlicer

Available via the UI since version 2.3, requires expert mode to be enabled in the upper right corner of the program to see the setting.

![PrusaSlicer](/assets/img/plugins/prusaslicerthumbnails/screenshot_prusaslicer.png)

**Warning**: the higher the resolution of the thumbnail you use in this setting the larger your gcode file will be when sliced.

### SuperSlicer

Available via the UI since version 2.2.53, requires expert mode to be enabled in the upper right corner of the program to see the setting.

![SuperSlicer](/assets/img/plugins/prusaslicerthumbnails/screenshot_superslicer.png)

**Warning**: the higher the resolution of the thumbnail you use in this setting the larger your gcode file will be when sliced.

### Cura

A post-processing script has been bundled since version 4.9. For older versions you can manually add the post-processing script as described [here](https://gist.github.com/jneilliii/4034c84d1ec219c68c8877d0e794ec4e).

![Cura](screenshot_cura.png)

### Simplify3D

Available as a post-processing script for [windows](https://github.com/boweeble/s3d-thumbnail-generator) or [linux](https://github.com/NotExpectedYet/s3d-thumbnail-generator) thanks to [@boweeble](https://github.com/boweeble/) and [@NotExpectedYet](https://github.com/NotExpectedYet/).

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

### Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip or become a Patron if you find this plugin helpful and want me to continue future development.

[![Patreon](/assets/img/plugins/prusaslicerthumbnails/patreon-with-text-new.png)](https://www.patreon.com/jneilliii) [![paypal](/assets/img/plugins/prusaslicerthumbnails/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>
