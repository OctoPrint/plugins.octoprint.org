---
layout: plugin

id: SlicerSettingsParser
title: OctoPrint-SlicerSettingsParser
description: Plugin to analyse gcode for slicer settings comments and add additional metadata of such settings.
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

 # featuredimage: url of a featured image for your plugin, /assets/img/...

compatibility:

  # Untested on previous versions

  octoprint:
  - 1.3.10

  # Doesn't work on Windows
  # Unsure about MacOS

  os:
  - nix

---

*This plugin is useless without another plugin to use the metadata. Those can be found [here](/by_tag/#tag-slicer-settings).*

## Configuration

### Sed command (Advanced)

This plugin uses `sed` to parse the gcode. Sed command syntax can be easily found on the web [(help)](http://lmgtfy.com/?q=sed+command+syntax).
The output should be of the format:
```
key=value
key2=value
key lalalalala=value=haha
with_newlines=abc\ndef
```
will be parsed as (JSON):
```json
{
 "key": "value",
 "key2": "value",
 "key lalalalala": "value=haha",
 "with_newlines": "abc\ndef"
}
```
