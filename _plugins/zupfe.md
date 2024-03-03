---
layout: plugin

id: zupfe
title: OctoPrint-Zupfe
description: A plugin for octoprint that allows you to see in real time print jobs in Zupfe
authors:
- Glenn Hall
license: AGPLv3

date: 2024-03-03

homepage: https://github.com/glennerichall/OctoPrint-Zupfe
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

---
## Setup
Install the plugin then in the Wizard or in the Settings, click "Complete Your Setup Now". Log into your ZupFe account. That's it!
