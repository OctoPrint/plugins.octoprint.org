---
layout: plugin

id: nautilus
title: Nautilus - mobile shell for OctoPrint
description: OctoPrint simplified interface optimized for iOS devices
author: ovidiu
license: AGPLv3
date: 2016-10-27

homepage: https://github.com/MoonshineSG/OctoPrint-Mobile/wiki
source: https://github.com/MoonshineSG/OctoPrint-Mobile
archive: https://github.com/MoonshineSG/OctoPrint-Mobile/archive/master.zip
follow_dependency_links: false

tags:
- iOS
- iphone
- ipad

compatibility:
  # list of compatible versions, for example 1.2.0. If left empty no specific version requirement will be assumed
  octoprint:
  - 1.3.0


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

featuredimage: /assets/img/plugins/nautilus/img1.gif
  
---

OctoPrint simplified interface optimized for iOS devices. 

The iOS app will force landscape, maintain the API key and handle the server connection.

Bonus feature: shake to refresh.


The iOS app is available on [apple appstore](https://itunes.apple.com/us/app/id1125992543).

As long as OctoPrint is available over the internet, the UI changes to full screen webcam for pure monitoring. 


The plugin configuration file `settings.ini` (residing under the plugin data folder - `.octoprint/data/nautilus`) provides the gcode sequences for most of the functions provided. Make sure they are configured properly for your machine. [Read more](https://github.com/MoonshineSG/OctoPrint-Mobile/wiki/settings.ini)

Some supplementary, non-core switch functions depend on a additional plugin which can be install separatly from [https://github.com/MoonshineSG/OctoPrint-Switch/archive/master.zip](https://github.com/MoonshineSG/OctoPrint-Switch/archive/master.zip). If the Switch plugin is not detected, the respective buttons are not shown and the printer is assumed to be powered on.

[Read more...](https://github.com/MoonshineSG/OctoPrint-Mobile/wiki)
