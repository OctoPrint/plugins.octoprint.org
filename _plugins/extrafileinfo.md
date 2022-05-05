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

This plugin adds slicer settings to the additional data tab of each file, which is shown by pressing the downwards arrow button. Uses [Octoprint-SlicerSettingsParser-Python3](https://github.com/Rob4226/OctoPrint-SlicerSettingsParser-Python3) to get the data.

![fileinfo](/assets/img/plugins/extrafileinfo/file.png)

The plugin's settings allows you to configure which slicer settings to show and what their units should be.

## Configuration

| **Setting**      	| **Description**                                                 	|
|------------------	|-----------------------------------------------------------------	|
| Key              	| The "key" of your slicer setting in SlicerSettingsParser        	|
| Label (optional) 	| A label that replaces the key in the file info view             	|
| Unit (optional)  	| The unit suffix that is appended after the value of the setting 	|

---


The Key, Label and Unit fields in the plugin's settings are directly injected into the view, without any sanitization. Therefore, the use of HTML tags (such as label=`<strong>Material` and unit=`</strong>`) is allowed.