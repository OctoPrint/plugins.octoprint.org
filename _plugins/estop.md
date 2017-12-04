---
layout: plugin

id: estop
title: Emergency STOP! button
description: Adds an emergency stop button to the sidebar.
author: ntoff
license: AGPLv3

date: 2017-12-02

homepage: https://github.com/ntoff/OctoPrint-Estop
source: https://github.com/ntoff/OctoPrint-Estop
archive: https://github.com/ntoff/OctoPrint-Estop/archive/master.zip

follow_dependency_links: false

tags:
- emergency stop
- M112


screenshots:
- url: /assets/img/plugins/estop/enabled.PNG
  alt: enabled
  caption: Enabled (logged in and operational)
- url: /assets/img/plugins/estop/disabled.PNG
  alt: disabled
  caption: Disabled (logged out or non operational)


featuredimage: /assets/img/plugins/estop/enabled.PNG

compatibility:
  octoprint:
  - 1.2.0

  
  os:
  - linux
  - windows
  - macos
---

Adds a nice big emergency stop button that (by default) sends M112 to the printer in the case of an emergency. If your printer uses a different E-Stop command, there's a settings page entry to allow changing the command sent.

Please do be aware that this button is no substitute for human interaction in the case of a real emergency. How your printer responds to M112 depends entirely on its firmware.