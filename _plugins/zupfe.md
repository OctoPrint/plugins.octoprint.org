---
layout: plugin

id: zupfe
title: OctoPrint-Zupfe
description: A plugin for octoprint that allows you to see in real time print jobs in ZupFe, the interactive online gcode viewer. View gcode content and interact with the 3d model to find the exact command of any extrusion.
authors:
- Glenn Hall
license: AGPLv3

date: 2024-03-03

homepage: https://zupfe.velor.ca
source: https://github.com/glennerichall/OctoPrint-Zupfe
archive: https://github.com/glennerichall/OctoPrint-Zupfe/archive/master.zip

tags:
- access
- live stream
- gcode
- remote app

screenshots:
- url: /assets/img/plugins/zupfe/img_3.png
- url: /assets/img/plugins/zupfe/img_5.png
- url: /assets/img/plugins/zupfe/img_4.png

featuredimage: /assets/img/plugins/zupfe/img_3.png

compatibility:

  octoprint:
  - 1.9.0

  # Compatible Python version
  #
  # It is recommended to only support Python 3 for new plugins, in which case this should be ">=3,<4"
  # 
  # Plugins that wish to support both Python 2 and 3 should set it to ">=2.7,<4".
  #
  # Plugins that only support Python 2 will not be accepted into the plugin repository.

  python: ">=3,<4"

attributes:
- cloud

---
### Features
This plugin permits remote access of your OctoPrint instances through [ZupFe](https://zupfe.velor.ca).
 - Follow in real time the printing progress on a premium GCode viewer
 - See your printer's camera stream and printer temperatures
 - Upload or load printer files into ZupFe
 - Start/pause printing jobs
 - All of this directly in your browser on the internet

### Setup
Install the plugin then in the Wizard or in the Settings, click "Complete Your Setup Now". Log into your ZupFe account. That's it!

### Questions, Comments, Or Feedback?
Contact us at [zupfe@velor.ca](mailto:zupfe@velor.ca).
See our [Terms](https://zupfe.velor.ca/terms.html) and [Privacy](https://zupfe.velor.ca/privacy.html)
