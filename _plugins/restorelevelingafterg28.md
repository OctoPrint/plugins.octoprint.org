---
layout: plugin

id: restorelevelingafterg28
title: Restore Leveling After G28
description: Automatically keeps bed leveling on after G28 (Auto Home).
author: Xennis
license: MIT

date: 2020-06-03

homepage: https://github.com/Xennis/OctoPrint-RestoreLevelingAfterG28
source: https://github.com/Xennis/OctoPrint-RestoreLevelingAfterG28
archive: https://github.com/Xennis/OctoPrint-RestoreLevelingAfterG28/archive/master.zip

tags:
- leveling
- bed leveling
- marlin

compatibility:
  octoprint:
  - 1.2.0
  os:
  - linux
  - windows
  - macos
  - freebsd
  python: ">=2.7,<4"

---

Marlin code `G28` disables bed leveling. The plugin restores the prior state:

* Before the `G28` command a `M420 V` is send to check if leveling is enabled or not.
* If leveling was enabled: After the `G28` command a `M420 S1` is send to enable leveling.

That same behaviour can be enabled in the Marlin firmware via `RESTORE_LEVELING_AFTER_G28`.

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

```
https://github.com/Xennis/OctoPrint-RestoreLevelingAfterG28/archive/master.zip
```

## Configuration

The plugin has no configuration and does not adjust the UI.
