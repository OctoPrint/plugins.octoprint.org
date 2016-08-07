---
layout: plugin
    
id: M117PopUp
title: OctoPrint-M117PopUp
description: Plugin to send M117 gcode messages to the web interface.
author: jneilliii
license: AGPLv3
    
# today's date in format YYYY-MM-DD, e.g.
date: 2016-08-06
    
homepage: https://github.com/jneilliii/OctoPrint-M117PopUp
source: https://github.com/jneilliii/OctoPrint-M117PopUp
archive: https://github.com/jneilliii/OctoPrint-M117PopUp
    
# set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
follow_dependency_links: false
    
tags:
- M117
- gcode

screenshots: 
- url: /assets/img/plugins/M117PopUp/screenshot_1.png
  alt: Screenshot
  caption: Screenshot of the M117PopUp messages

featuredimage: /assets/img/plugins/M117PopUp/screenshot_1.png

compatibility:
  # list of compatible versions, for example 1.2.0. If left empty no specific version requirement will be assumed
  octoprint:
  - 1.2.0

  # list of compatible operating systems, valid values are linux, windows, macos, leaving empty defaults to all
  os:
  - linux
---
    
This plugin utilizes the _plugin_manager.send_plugin_message and onDataUpdaterPluginMessage to communicate between server and client. It utilizes OctoPrint's built in alerting system to pop up the messages being sent via M117 gcode command.