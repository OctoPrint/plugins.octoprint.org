---
layout: plugin

id: translatemodel
title: OctoPrint-TranslateModel
description: A plugin to move models around without re-slicing.
authors:
- Will MacCormack
license: AGPLv3

date: 2021-03-01

homepage: https://github.com/Willmac16/OctoPrint-TranslateModel
source: https://github.com/Willmac16/OctoPrint-TranslateModel
archive: https://github.com/Willmac16/OctoPrint-TranslateModel/archive/main.zip

tags:
- gcode

screenshots:
- url: /assets/img/plugins/translatemodel/translateActionButton.png
  alt: Translate Model action button
  caption: select a file with the four arrow action button
- url: /assets/img/plugins/translatemodel/translateTab.png
  alt: Translate Model Tab
  caption: configure and run you file translation
- url: /assets/img/plugins/translatemodel/viewerGraphic.png
  alt: File Translate example
  caption: easily move gcode models all within OctoPrint

featuredimage: /assets/img/plugins/translatemodel/viewerGraphic.png

compatibility:

  octoprint:
  - 1.3.1

  python: ">=2.7,<4"

---

# OctoPrint-TranslateModel

Translate Model allows you to move models around in gcode files without reslicing.

## Features
* Select files via the translate button in the file pane
* Quick and easy model movement along the x and y axes
* Options to automatically print files after translation

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/Willmac16/OctoPrint-TranslateModel/archive/main.zip

* This plugin will compile its C++ code on install, but this should be pretty quick.

See the [GitHub page](https://github.com/Willmac16/OctoPrint-TranslateModel) for up-to-date information.
