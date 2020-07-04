---
layout: plugin

id: swapxy
title: SwapXY
description: Swap the X and Y axes used by the jog controls
author: Andy Castille <andy.castille@wolframmf.com>
license: GPLv3
date: 2020-07-02

homepage: https://gitlab.com/wolframmfg/octoprint-swapxy
source: https://gitlab.com/wolframmfg/octoprint-swapxy/-/tree/main
archive: https://gitlab.com/wolframmfg/octoprint-swapxy/-/archive/main/octoprint-swapxy-main.zip

tags:
- controls
- ui

screenshots:
- url: /assets/img/plugins/swapxy/swapxy_settings.png
  alt: Screenshot of the SwapXY section of the OctoPrint settings dialog, showing options to also reverse the X and/or Y axis movement
  caption: Configuration

featuredimage: /assets/img/plugins/swapxy/swapxy_controls.png

compatibility:
  python: ">=2.7,<4"

---

## Setup

As long as the plugin is enabled, the jog buttons for X and Y will
drive the other axis instead.

To drive one or both of these axes in the opposite direction (negative/positive), enable the reverse option for that axis.

## Config

These options can also be changed from the web UI settings window.

Default config:

```yaml
plugins:
    swapxy:
        reverse:
            X: false
            Y: false
```

---

Developed by [Wolfram Manufacturing](https://wolframmfg.com/)
