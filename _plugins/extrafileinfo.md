---
layout: plugin

id: extrafileinfo
title: ExtraFileInfo
description: Adds a file's slicer settings to its additional data column.
authors:
- Larsjuhw
license: AGPLv3

date: 2022-05-05

homepage: https://github.com/larsjuhw/OctoPrint-Extrafileinfo
source: https://github.com/larsjuhw/OctoPrint-Extrafileinfo
archive: https://github.com/larsjuhw/OctoPrint-Extrafileinfo/archive/master.zip

follow_dependency_links: false

tags:
- slicer settings
- slicersettingsparser
- info

featuredimage: /assets/img/plugins/extrafileinfo/file.png

compatibility:
  python: ">=3,<4"

---

# ExtraFileInfo

This plugin adds slicer settings to the additional data tab of each file, which is shown by pressing the downwards arrow button. Uses [Octoprint-SlicerSettingsParser-Python3](https://github.com/Rob4226/OctoPrint-SlicerSettingsParser-Python3) (which should install automatically) to get the slicer data from the gcode.

![fileinfo](/assets/img/plugins/extrafileinfo/file.png)

The plugin's settings allows you to configure which slicer settings to show and what their units should be.

## Configuration
### SlicerSettingsParser
SlicerSettingsParser searches through your gcode files to find commented lines that contain the slicer settings. Some slicers automatically add these lines to your gcode files, but not all do it by default. The parser finds the "key = value" sets of these settings by matching each line with a regex. The default regex supports Slic3r and Simplify3D (and the Cura configuration below).

After installing, you need to configure SlicerSettingsParser to parse your gcode files and find the commented settings in them. Press the "Analyze all files" button to scan your old files. Note that my Raspberry Pi 4B 2GB can only handle around 4 MB/s, so this can take a while depending on your files and setup.

**If you use Cura, you need to add [this](https://gist.github.com/tjjfvi/75210b2ed20ed194d6eab48bf70c4f12) to your start or end gcode.** More gcode variables that Cura supports can be found [on this page](http://files.fieldofview.com/cura/Replacement_Patterns.html). If you want to add these manually, make sure that you keep using the `; key = {variable}` style.

### ExtraFileInfo

| **Setting**      	| **Description**                                                 	|
|------------------	|-----------------------------------------------------------------	|
| Key              	| The "key" of your slicer setting in SlicerSettingsParser        	|
| Label (optional) 	| A label that replaces the key in the file info view             	|
| Unit (optional)  	| The unit suffix that is appended after the value of the setting 	|

---


The Key, Label and Unit fields in the plugin's settings are directly injected into the view, without any sanitization. Therefore, the use of HTML tags (such as label=`<strong>Material</strong>`) is allowed.


## Example

The gcode file that I upload contains the following lines:

```
; layer_height = 0.2
; adaptive_layer_height_enabled = False
; adhesion_type = skirt
```
The default settings of SlicerSettingsParser support this format. To display these values in the file info, I configure this plugin as such, while leaving the other settings empty:

![example1](/assets/img/plugins/extrafileinfo/example1.png)

This gives the following result in the files menu:

![example2](/assets/img/plugins/extrafileinfo/example2.png)

## Known Issues

* SlicerSettingsParser does not parse newly uploaded files when Cura Thumbnails/UltimakerFormatPackage is installed, [as described here](https://github.com/tjjfvi/OctoPrint-SlicerSettingsParser/issues/7). Use [Slicer Thumbnails](https://plugins.octoprint.org/plugins/prusaslicerthumbnails/#cura) instead to solve this.