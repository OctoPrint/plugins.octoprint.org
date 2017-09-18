---
layout: plugin

id: ZERO
title: OctoPrint-ZERO
description: Configures compiling and install FirmWare for any 3D printer 30 in Sec.
author: Giorgio Kolozof
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2017-09-2

homepage: https://github.com/gkolozof/
source: https://github.com/gkolozof/OctoPrint-ZERO.git
archive: https://github.com/gkolozof/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
follow_dependency_links: false

tags:
- 0.2.1

screenshots:
- url: /assets/img/plugins/ZERO/OctoPrint-ZERO.png
  alt: After configuring compill and install the FirmWare
  caption: Configures compiling and install FirmWare for any 3D printer in 30 Sec.

featuredimage: /assets/img/ZERO.png

# You only need the following if your plugin requires specific OctoPrint versions or
# specific operating systems to function - you can safely remove the whole
# "compatibility" block if this is not the case.

compatibility:

  octoprint:
  - 1.2.4


  os:
  - Linux
  - MacOs

---

Configures compiling and install FirmWare for any 3D printer in 30 Sec.
plugins.octoprint.org/plugin/ZERO/

GIT: https://github.com/gkolozof/OctoPrint-ZERO/archive/master.zip
Project: OctoPrint ZERO
Compatibility: Linux/Mac OS
Plugin: OctoPrint
Manual installation: python2.7 -m pip install https://github.com/gkolozof/OctoPrint-ZERO/archive/master.zip
                or   python -m pip install https://github.com/gkolozof/OctoPrint-ZERO/archive/master.zip
                     apt install avrdude #for Linux
                     brew install  vrdude $for Mac

REQUIREMENTS for Linux: avrdude  (Type from shell: apt install avrdude)
REQUIREMENTS for Mac: avrdudea (Type from shell: brew install)

Manual restart server for Linux:
 /etc/init.d/octoprint restart

Installation approx. time 3 Min.
Firmware Configuration, compilation and installtion approx. time 30 Sec.!!!

For HELP: gkolozof@gmail.com

Good Work!!!

