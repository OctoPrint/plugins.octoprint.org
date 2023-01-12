---
layout: plugin

id: CreatbotUtil
title: Creatbot Util
description: Various utility functions to make OctoPrint work better with Creatbot printers.
author: Kestin Goforth
license: AGPLv3

date: 2022-06-14

homepage: https://github.com/kForth/OctoPrint-CreatbotUtil
source: https://github.com/kForth/OctoPrint-CreatbotUtil
archive: https://github.com/kForth/OctoPrint-CreatbotUtil/archive/main.zip

follow_dependency_links: false

tags:
- creabot
- printer
- control
- command
- serial
- start
- stop
- temperature
- heated
- chamber
- build
- volume

# featuredimage: null

screenshots:
- url: /assets/img/plugins/CreatbotUtil/settings.png
  alt: Settings Page Screenshot

compatibility:
  python: ">=2.7,<4"

---

# Creatbot Util

This plugin add various utility functions to make OctoPrint work better with Creatbot printers.

## Features

- Send "Start/Stop Serial Print" commands whenever a print is started, cancelled, or finished (M6006 & M6007).

- Replace the Marlin 'Set Chamber Temperature' command (M141) with the Creatbot command (M6013).

## Screenshot

![Settings Page Screenshot](/assets/img/plugins/CreatbotUtil/settings.png)

## Notes

This plugin should work for most/all Creatbot 3D Printers but has only been tested with a Creatbot F430.

Your Creatbot firmware may need to be upgraded to at least v5.6, the original v5.5 firmware that shipped with my Creatbot F430 did not support the Heated Chamber (M6013) command.
