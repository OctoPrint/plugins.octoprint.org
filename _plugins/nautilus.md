---
layout: plugin

id: nautilus
title: Nautilus - mobile shell for OctoPrint
description: OctoPrint simplified interface optimized for mobile devices
author: ovidiu
license: AGPLv3
date: 2016-07-04

homepage: https://github.com/MoonshineSG/OctoPrint-Mobile
source: https://github.com/MoonshineSG/OctoPrint-Mobile
archive: https://github.com/MoonshineSG/OctoPrint-Mobile/archive/master.zip
follow_dependency_links: false

tags:
- mobile
- iOS
- iphone
- ipad
- responsive

compatibility:
  # list of compatible versions, for example 1.2.0. If left empty no specific version requirement will be assumed
  octoprint:
  - 1.3.0 dev


screenshots:
- url: /assets/img/plugins/nautilus/img1.png
  alt: Information
- url: /assets/img/plugins/nautilus/img2.png
  alt: Printer
- url: /assets/img/plugins/nautilus/img3.png
  alt: Movement
- url: /assets/img/plugins/nautilus/img4.png
  alt: Offset
- url: /assets/img/plugins/nautilus/img5.png
  alt: Camera

featuredimage: /assets/img/plugins/marlin/img1.gif
  
---

OctoPrint simplified interface optimized for iOS devices. 

The iOS app is needed to force landscape, maintains the API key and handles the server connection. 

Bonus feature: shake to refresh.


The iOS app is available on [apple appstore](https://itunes.apple.com/us/app/id1125992543).

As long as octoprint is available over the internet, the UI changes to full screen webcam for pure monitoring. 

For notifications via [Prowl](https://www.prowlapp.com/), change settings by manually editing `config.yaml` under "plugins"

```
plugins:
  nautilus:
    prowl_key: [your_prowl_key]
```

`pyprowl` included from [https://github.com/babs/pyrowl/tree/master](https://github.com/babs/pyrowl/tree/master)

`settings.ini` under the plugin folder or it's corresponding data folder (`.octoprint/data/nautilus`) provides the gcode sequences for most of the functions provided. Make sure they are configured properly for your machine.

Some supplementary, non-core switch functions depend on a additional plugin which can be install separatly from [https://github.com/MoonshineSG/OctoPrint-Switch/archive/master.zip](https://github.com/MoonshineSG/OctoPrint-Switch/archive/master.zip). If the Switch plugin is not detected, the respective buttons are grey out and the printer is assumed to be powered on.

