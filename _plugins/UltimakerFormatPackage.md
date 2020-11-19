---
layout: plugin

id: UltimakerFormatPackage
title: Cura Thumbnails
description: This plugin adds support for Ultimaker Format Package (.ufp) files.
author: jneilliii
license: AGPLv3

date: 2019-11-16

homepage: https://github.com/jneilliii/OctoPrint-UltimakerFormatPackage
source: https://github.com/jneilliii/OctoPrint-UltimakerFormatPackage
archive: https://github.com/jneilliii/OctoPrint-UltimakerFormatPackage/archive/master.zip

follow_dependency_links: false

tags:
- Ultimaker Format Package
- ufp
- Cura

compatibility:
  python: ">=2.7,<4"

featuredimage: /assets/img/plugins/UltimakerFormatPackage/screenshot_thumbnail.png

---

# Cura Thumbnails

(formerly Ultimaker Format Package)

This plugin adds support for Ultimaker Format Package (.ufp) files. Ultimaker Format Package files are based on Open Packaging Conventions (OPC) and contain compressed gcode and a preview thumbnail. This format will automatically be used by the [OctoPrint Connection](https://github.com/fieldOfView/Cura-OctoPrintPlugin) plugin in Cura (install via Marketplace) if this plugin is installed.

The preview thumbnail can be shown in OctoPrint from the files list by clicking the newly added image button.

![button](/assets/img/plugins/UltimakerFormatPackage/screenshot_button.png)

The thumbnail will open in a modal window.

![thumbnail](/assets/img/plugins/UltimakerFormatPackage/screenshot_thumbnail.png)

If enabled in settings the thumbnail can also be embedded as an inline thumbnail within the file list itself. If you use this option it's highly recommended to use Themify to make the file list taller and/or adjust the thumbnail's size.  The image selector for this in Themeify should be `div.row-fluid.inline_thumbnail > img` but I haven't yet tested personally.

![thumbnail](/assets/img/plugins/UltimakerFormatPackage/screenshot_inline_thumbnail.png)

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

### Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip or become a Patron if you find this plugin helpful and want me to continue future development.

[![Patreon](/assets/img/plugins/UltimakerFormatPackage/patreon-with-text-new.png)](https://www.patreon.com/jneilliii) [![paypal](/assets/img/plugins/UltimakerFormatPackage/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>
