---
layout: plugin

id: excluderegion
title: OctoPrint-ExcludeRegionPlugin
description: Adds the ability to prevent printing within rectangular or circular regions of the currently active gcode file
author: Brad Fisher
license: AGPLv3

date: 2018-07-05

homepage: https://github.com/bradcfisher/OctoPrint-ExcludeRegionPlugin
source: https://github.com/bradcfisher/OctoPrint-ExcludeRegionPlugin
archive: https://github.com/bradcfisher/OctoPrint-ExcludeRegionPlugin/archive/master.zip

follow_dependency_links: false

tags:
- gcode
- exclude
- region
- ui

screenshots:
- url: /assets/img/plugins/excluderegion/excluderegion-gcode-viewer.png
  alt: OctoPrint gcode viewer with Exclude Region plugin installed
  caption: OctoPrint gcode viewer with Exclude Region plugin installed

featuredimage: /assets/img/plugins/excluderegion/excluderegion-gcode-viewer.png

compatibility:
  octoprint:
  - 1.3.8

---

Imagine running a long running, multi-part print job only to have one of the parts fail half-way
through.  If you allow the job to continue, that big mess of spaghetti-like extrusions within the
failed area are likely to get stuck to other pieces and lead to additional failures or blemishes
on the other parts (not to mention wasted filament) as the print goes on.

The intent of this plugin is to provide a means to salvage multi-part prints where one (or more)
of the parts has broken loose from the build plate or has otherwise become a worthless piece of
failure.  Instead of cancelling an entire job when only a portion is messed up, use this plugin
to instruct OctoPrint to ignore any gcode commands executed within the area around the failure.

You can dynamically define rectangular or circular exclusion regions for the currently selected
gcode file through OctoPrint's integrated gcode viewer, and those regions may be added or modified
before, during, or even after printing.

## Some things to note about this plugin

* It can only affect printing of files managed by OctoPrint, and can NOT exclude regions of files
  being printed from your printer's SD card.
* Use the exclude feature at your own risk.  It is recommended to only use it when a portion of
  your print has already failed.
* When defining regions, try to fully enclose all portions of the failed part that would otherwise
  still print.  You will get unpredictable results if you only exclude a portion of a part, and any
  overhangs on higher layers that extend outside an excluded region will have nothing to support
  them.
* This plugin makes several assumptions when filtering the gcode, some of which may not be correct
  for your printer's firmware.  It was developed with Marlin in mind, so should work reasonably well
  with firmware that replicates Marlin's behavior.
* The plugin only supports a single hotend at this time.  It is not recommended to attempt to use
  it on a gcode file with instructions for multiple hotends.
* Users of TouchUI will not be able to create or modify exclude regions.  Any defined regions will
  be displayed, but they cannot currently be manipulated on a touch device.

## Get Help

If you experience issues with this plugin please use the issue tracker at the plugin's Homepage
linked on the right.
