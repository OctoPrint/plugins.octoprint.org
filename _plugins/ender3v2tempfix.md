---
layout: plugin

id: ender3v2tempfix
title: Ender-3 v2 Temperature Fix
description: Fixes the temperature reporting from the Creality Ender-3 v2 printer
author: Albert MN. @ SimplyPrint, b-morgan
license: MIT

# today's date in format YYYY-MM-DD, e.g.
date: 2020-09-07

homepage: https://github.com/SimplyPrint/OctoPrint-Ender3V2TempFix
source: https://github.com/SimplyPrint/OctoPrint-Ender3V2TempFix
archive: https://github.com/SimplyPrint/OctoPrint-Ender3V2TempFix/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- creality
- ender-3 v2
- temperature

compatibility:
  os:
  - linux
  - windows
  - macos
  - freebsd
  
  python: ">=2.7,<4"
      
---

Fixes the double temperature reporting from the Creality Ender-3 v2 printer described in [this OctoPrint forum topic](https://community.octoprint.org/t/octoprint-doesnt-show-a-temperature-graph-for-my-creality-printer/23901).

Some of the newer Creality firmware has an issue where, when reporting its temperature, it writes everything twice.
Example; _should report tool; 27.76, bed; 39.35
```
TT::27.7627.76  //0.000.00  BB::39.3539.35  //0.000.00  @@::00  BB@@::00
```

This plugin turns the input into the correct format, like this;
```
T:23.84 /0.00 B:24.05 /0.00 @:0 B@:0
```


**This fix is confirmed to work for the following printers:**
- Creality Ender-3 Pro v2
- Creality CR-6 SE
