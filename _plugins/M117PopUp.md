---
layout: plugin

id: M117PopUp
title: OctoPrint-M117PopUp
description: Plugin to send M117 gcode messages to the web interface.
author: jneilliii
license: AGPLv3

date: 2016-10-27

homepage: https://github.com/jneilliii/OctoPrint-M117PopUp
source: https://github.com/jneilliii/OctoPrint-M117PopUp
archive: https://github.com/jneilliii/OctoPrint-M117PopUp/archive/master.zip

follow_dependency_links: false

tags:
- M117
- gcode

compatibility:
  python: ">=2.7,<4"

featuredimage: /assets/img/plugins/M117PopUp/screenshot_1.png

---

# M117PopUp

This plugin utilizes ``_plugin_manager.send_plugin_message`` and ``onDataUpdaterPluginMessage`` to communicate between server and client. It utilizes OctoPrint's built in alerting system to pop up the messages being sent via M117 gcode command.

## Screenshots

![screenshot](/assets/img/plugins/M117PopUp/screenshot_1.png)

![settings](/assets/img/plugins/M117PopUp/settings.png)

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

### Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip or become a Patron if you find this plugin helpful and want me to continue future development.

[![Patreon](/assets/img/plugins/M117PopUp/patreon-with-text-new.png)](https://www.patreon.com/jneilliii) [![paypal](/assets/img/plugins/M117PopUp/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>
