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
- url: /assets/img/plugins/marlin/img1.png
  alt: Information
- url: /assets/img/plugins/marlin/img2.png
  alt: Printer
- url: /assets/img/plugins/marlin/img3.png
  alt: Movement
- url: /assets/img/plugins/marlin/img4.png
  alt: Offset
- url: /assets/img/plugins/marlin/img5.png
  alt: Camera

featuredimage: /assets/img/plugins/marlin/img1.gif
  
---

OctoPrint simplified interface optimized for mobile devices (only works on dev branch of OctoPrint)

The iOS app is needed to force landscape, load the API key and switch on/off the socket. 
Bonus feature: shake to refresh.

The iOS app is available on [apple appstore](https://itunes.apple.com/us/app/id1125992543).

When using the browser you can create a shortcut by using "Add to Home Screen" (it will be shown as "Nautilus")
Without the app constrains, the webapp has some alignment problems

As long as octoprint is available over the internet, the UI changes to full screen webcam for pure monitoring. 

For notifications via Prowl, change settings by manually editing `config.yaml` under "plugins"

```
plugins:
  nautilus:
    prowl_key: [your_prowl_key]
```

`pyprowl` included from [https://github.com/babs/pyrowl/tree/master](https://github.com/babs/pyrowl/tree/master)

`settings.ini` under the plugin folder or it's corresponding data folder (`.octoprint/data/nautilus`) provides the gcode sequences for most of the functions provided. Make sure they are configured properly for your machine.

