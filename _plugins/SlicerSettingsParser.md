---
layout: plugin

id: SlicerSettingsParser
title: OctoPrint-SlicerSettingsParser
description: Plugin to analyze gcode for slicer settings comments and add additional metadata of such settings.
author: T6
license: AGPLv3

date: 2018-12-22

homepage: https://github.com/tjjfvi/OctoPrint-SlicerSettingsParser
source: https://github.com/tjjfvi/OctoPrint-SlicerSettingsParser
archive: https://github.com/tjjfvi/OctoPrint-SlicerSettingsParser/archive/master.zip

tags:
- gcode
- analysis
- slicer settings

---

**NOTE: Only supports Slic3r and Simplify3D currently; suggest more in issues; contributions welcome!**

*Note: this plugin has not been test with versions under 1.3.10; they may not work!*

*This plugin is useless without another plugin to use the metadata. Those can be found [here](/by_tag/#tag-slicer-settings).*

## Configuration

### Python regexes (Advanced)

This plugin uses python regexes to parse the gcode.
Syntax can be easily found on the web.
There should be two named capturing groups, `key` and `val`.
Multiple regexes should be listed on seperate lines, ordered by precedence.
Any chars are allowed in the groups; `\n` will be replaced by newlines.

See the [wiki](https://github.com/tjjfvi/OctoPrint-SlicerSettingsParser/wiki/Python-regexes) for examples.
