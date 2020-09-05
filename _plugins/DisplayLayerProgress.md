---
layout: plugin

id: DisplayLayerProgress
title: DisplayLayerProgress 
description: Displays the Layer, Progress and other data on "Printer-Display", "NavBar", "BrowserTab-Title" and in the Browser as a simulated "Printer-Display"
author: Olli
license: AGPLv3

date: 2018-04-09

homepage: https://github.com/OllisGit/OctoPrint-DisplayLayerProgress
source: https://github.com/OllisGit/OctoPrint-DisplayLayerProgress
archive: https://github.com/OllisGit/OctoPrint-DisplayLayerProgress/releases/latest/download/master.zip

follow_dependency_links: false

tags:
- display
- lcd
- printer
- progress
- layer

compatibility:
  python: ">=2.7,<4"
  octoprint:
  - 1.3.10
  - 1.4.0
  
screenshots:
- url: https://github.com/OllisGit/OctoPrint-DisplayLayerProgress/raw/master/screenshots/browser-title-tab.png
  alt: Example of Browser Tab Title
  caption: Example of Browser Tab Title
- url: https://github.com/OllisGit/OctoPrint-DisplayLayerProgress/raw/master/screenshots/navbar.jpg
  alt: Example of NavBar Display
  caption: Example of NavBar Display
- url: https://github.com/OllisGit/OctoPrint-DisplayLayerProgress/raw/master/screenshots/example-printer-display.jpg
  alt: Example of Printer Display
  caption: Example of Printer Display
- url: https://github.com/OllisGit/OctoPrint-DisplayLayerProgress/raw/master/screenshots/printerDisplay_popup.jpg
  alt: Printer Display - PopUp
  caption: Printer Display - PopUp
- url: https://github.com/OllisGit/OctoPrint-DisplayLayerProgress/raw/master/screenshots/statebar.jpg
  alt: State Bar output
  caption: State Bar output
- url: https://github.com/OllisGit/OctoPrint-DisplayLayerProgress/raw/master/screenshots/plugin_settings.jpg
  alt: Plugin Settings
  caption: Plugin Settings


featuredimage: https://github.com/OllisGit/OctoPrint-DisplayLayerProgress/raw/master/screenshots/navbar.jpg

---

A OctoPrint-Plugin that sends the current Layer-Informations, the Progress and other data of a print via M117 command to the printer-display and also to the top navigation bar.
A new feature is the "Desktop Printer-Display", which shows all M117 messages in a Desktop PopUp.

It shows the **progress, estimatedEndTime, printTimeLeft, currentLayer, totalLayerCount, last/average layerDuration, currentHeight, totalHeight, feedrate and fanspeed**:

- Printer Display: ```50% L=60/120 H=23mm/47mm```  
- NavBar: Layer: ```60 / 120 Height: 23mm of 47mm```
- Browser TabTitle: ```12% end: 19:32```

*Output pattern is adjustable. Please visit the [homepage]({{ page.homepage | absolute_url }}) for more informations!*

#### Support my Efforts

This plugin, as well as my [other plugins](https://github.com/OllisGit/) were developed in my spare time.
If you like it, I would be thankful about a cup of coffee :) 

[![More coffee, more code](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=6SW5R6ZUKLB5E&source=url)

**ATTENTION:** 
- The layer information works only when the slicer adds "layer-indicator" to the g-code (CURA-Example as comments like ```;LAYER:10```). Then these indicators are parsed via a regular-expression.
- Currently supported slicers: CURA, Simplify3D, KISSlicer. You can add your own layer-expressions in Plugin-Settings.
If you want to use "slic3r", see [Enhancement #8](https://github.com/OllisGit/OctoPrint-DisplayLayerProgress/issues/8)
- Sometimes there is a "Post Processing script" that deletes all comments (e.g. see [Issue #33](https://github.com/OllisGit/OctoPrint-DisplayLayerProgress/issues/33))
- You need to upload your G-Code after installation of the plugin again (if you want to reuse already stored models in OctoPrint), because while uploading the G-Code is modfied
- The total height "calculation" can be done in two ways: 1)the max Z-Value in the G-Code, 2) max Z-Value with extrusion in this height
- The height/layer information is sometimes not matching with G-Code Viewer, because the viewer did a lot of "magic" (e.g. add extrusion diameter to height)


For implementation details please visit the [homepage]({{ page.homepage | absolute_url }}).

