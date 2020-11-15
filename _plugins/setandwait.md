---
layout: plugin
id: setandwait
title: Set And Wait
description: This OctoPrint plugin implements Set And Wait commands M109 & M190 into OctoPrint and sends their non-blocking counterparts to the controller.
archive: https://github.com/kantlivelong/OctoPrint-SetAndWait/archive/master.zip
homepage: https://github.com/kantlivelong/OctoPrint-SetAndWait
source: https://github.com/kantlivelong/OctoPrint-SetAndWait
author: Shawn Bruce
license: AGPLv3
date: 2020-06-02
tags:
- m109
- m190
- heating
- smoothieware
- cancel
- klipper
compatibility:
  os:
  - posix
  - windows
  python: ">=2.7,<4"
---

##### Benefits:
- Prints can be canceled during the heating phase without waiting for the temperature to be reached.
- Fixes an issue where Smoothieware only reports temperatures for the probe being heated which in turn causes gaps on the OctoPrint temperature graph for other probes.
- Works around odd behavior in Klipper where setting the temperature to a lower value will result in waiting for the heater to cool instead of simply continuting (S being treated as R). See [KevinOConnor/klipper#1108](https://github.com/KevinOConnor/klipper/issues/1108)

See <https://github.com/kantlivelong/OctoPrint-SetAndWait> for information.
