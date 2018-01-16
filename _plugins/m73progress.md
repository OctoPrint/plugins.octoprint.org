---
layout: plugin

id: m73progress
title: M73 Progress
description: A plugin to update the built-in progress bar on your printer's LCD.
author: Cesar Vandevelde
license: AGPLv3

date: 2018-01-07

homepage: https://github.com/cesarvandevelde/OctoPrint-M73Progress
source: https://github.com/cesarvandevelde/OctoPrint-M73Progress
archive: https://github.com/cesarvandevelde/OctoPrint-M73Progress/archive/master.zip

follow_dependency_links: false

tags:
- progress
- lcd
- display

# TODO
screenshots:
- url: /assets/img/plugins/m73progress/m73progress.jpg
  alt: Working LCD progress bar while printing from OctoPrint!
  caption: Working LCD progress bar while printing from OctoPrint!

featuredimage: /assets/img/plugins/m73progress/m73progress.jpg

---

Most 3D printers offer a progress bar or percentage indicator on
their display. However, by default, this percentage is only updated when
printing from SD card. When printing directly through OctoPrint, the progress bar
remains empty. This small plugin remedies the situation by injecting
`M73 (set build percentage)` commands into the print stream.

**Note:** Not all printers support this feature. In order for this to work, your
firmware needs to understand the `M73` command. See below for instructions for
[Marlin](https://github.com/MarlinFirmware/Marlin).

## Marlin Firmware

You will need a recent version of Marlin, **1.1.7** or later. The `M73` feature is
not enabled by default. You can enable it by uncommenting line 576 in
`Configuration_adv.h`:

```C
// Add an 'M73' G-code to set the current percentage
#define LCD_SET_PROGRESS_MANUALLY
```
