---
layout: plugin
    
id: M117NavBar
title: OctoPrint-M117NavBar
description: Plugin to send M117 gcode messages to the top navbar of OctoPrint.
author: jneilliii
license: AGPLv3
    
# today's date in format YYYY-MM-DD, e.g.
date: 2016-10-27
    
homepage: https://github.com/jneilliii/OctoPrint-M117NavBar
source: https://github.com/jneilliii/OctoPrint-M117NavBar
archive: https://github.com/jneilliii/OctoPrint-M117NavBar/archive/master.zip
    
# set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
follow_dependency_links: false
    
tags:
- M117
- gcode

screenshots: 
- url: /assets/img/plugins/M117NavBar/screenshot.png
  alt: Screenshot
  caption: Screenshot of the M117NavBar messages

featuredimage: /assets/img/plugins/M117NavBar/screenshot.png

---
    
This plugin utilizes the ``_plugin_manager.send_plugin_message`` and ``onDataUpdaterPluginMessage`` to communicate between server and client. It will display M117 gcode content in the header.
