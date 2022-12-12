---
layout: plugin

id: SlicerSettingsParser
title: SlicerSettingsParser
description: Plugin to analyze gcode for slicer settings comments and add additional metadata of such settings.
authors:
- Larsjuhw
- T6
license: AGPLv3

date: 2018-12-22

homepage: https://github.com/larsjuhw/OctoPrint-SlicerSettingsParser
source: https://github.com/larsjuhw/OctoPrint-SlicerSettingsParser
archive: https://github.com/larsjuhw/OctoPrint-SlicerSettingsParser/archive/master.zip

tags:
- gcode
- analysis
- slicer settings

compatibility:
  python: ">=3,<4"

---

# SlicerSettingsParser

*This plugin is useless without another plugin to use the metadata. Those can be found [here](/by_tag/#tag-slicer-settings).*

### Compatible plugins
Check out [ExtraFileInfo](/plugins/ExtraFileInfo) for an example of what this plugin can do.

### Configuration
#### Scan limit

Scanning all files entirely can take a considerable amount of time when your gcode library is large. A Raspberry Pi 4B seems to parse at a rate of about 4 MB/s. Every file you upload will be scanned, and choosing a scan limit in the settings will drastically reduce the scan time.

#### Cura

Cura doesn't natively support injecting the slicer settings into the gcode, so you must add [this](https://gist.github.com/tjjfvi/75210b2ed20ed194d6eab48bf70c4f12) to your start/end gcode. Preferably add it to the start gcode, so that you can configure this plugin to stop parsing when it sees the first extrusion command. [Here](http://files.fieldofview.com/cura/Replacement_Patterns.html) are all the available gcode variables that Cura supports.

#### Python regexes
##### Cura

If you use the start/end gcode provided above, use this regex:
```regex
^;\s*(?P<key>\w+[\w\s]*) : (?P<val>.*)
```

##### Slic3r

```regex
^; (?P<key>[^,]*?) = (?P<val>.*)
```

##### Simplify3D

```regex
^;   (?P<key>.*?),(?P<val>.*)
```

##### Other

This plugin uses python regexes to parse the gcode.
Syntax can be easily found on the web.
There should be two named capturing groups, `key` and `val`.
Multiple regexes should be listed on seperate lines, ordered by precedence.
Any chars are allowed in the groups; `\n` will be replaced by newlines.

If you can not figure it out yourself, open an issue and I can take a look.
