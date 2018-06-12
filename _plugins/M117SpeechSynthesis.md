---
layout: plugin
    
id: M117SpeechSynthesis
title: OctoPrint-M117SpeechSynthesis
description: Plugin to speak aloud M117 gcode messages via the web ui.
author: jneilliii
license: AGPLv3
    
date: 2018-01-18
    
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

featuredimage: /assets/img/plugins/M117SpeechSynthesis/settings.png

---

# M117 Speech Synthesis

This plugin utilizes ``_plugin_manager.send_plugin_message`` and ``onDataUpdaterPluginMessage`` to communicate between server and client.

**Note: this plugin does NOT work with files on the SD card. Requires modern day browsers that support Speech Synthesis, check compatibility table [here](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesisUtterance#Browser_compatibility).**

## Screenshots

![screenshot](/assets/img/plugins/M117SpeechSynthesis/settings.png)

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

### Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip if you find this plugin helpful.

[![paypal](/assets/img/plugins/M117SpeechSynthesis/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>
