---
layout: plugin
    
id: M117SpeechSynthesis
title: OctoPrint-M117SpeechSynthesis
description: Plugin to speak aloud M117 gcode messages via the web ui.
author: jneilliii
license: AGPLv3
    
date: 2018-01-17
    
homepage: https://github.com/jneilliii/OctoPrint-M117SpeechSynthesis
source: https://github.com/jneilliii/OctoPrint-M117SpeechSynthesis
archive: https://github.com/jneilliii/OctoPrint-M117SpeechSynthesis/archive/master.zip
    
follow_dependency_links: false
    
tags:
- M117
- gcode
- speech
- voice
- accessibility

screenshots: 
- url: /assets/img/plugins/M117SpeechSynthesis/settings.png
  alt: Settings
  caption: Screenshot of the M117 Speech Synthesis Settings

featuredimage: /assets/img/plugins/M117SpeechSynthesis/settings.png

---
    
This plugin utilizes the ``_plugin_manager.send_plugin_message`` and ``onDataUpdaterPluginMessage`` to communicate between server and client.

**Note: this plugin does NOT work with files on the SD card. Requires modern day browsers that support Speech Synthesis, check compatibility table [here](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesisUtterance#Browser_compatibility).**
