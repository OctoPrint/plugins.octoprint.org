---
layout: plugin
id: pause_for_user_event
title: PauseForUser Event
description: Adds a new event 'paused_for_user' when the printer needs manual intervention
author: Thomas Arthofer
license: AGPLv3
homepage: https://github.com/zeroflow/OctoPrint-PauseForUserEvent
source: https://github.com/zeroflow/OctoPrint-PauseForUserEvent
archive: https://github.com/zeroflow/OctoPrint-PauseForUserEvent/archive/master.zip
tags: 
- paused for user
- Prusa MMU2
- notification
- event
compatibility:
  octoprint:
  - 1.3.11 
date: 2019-06-03

---

When `echo:busy: paused for user` is received on the serial port, this plugin then raises a `paused_for_user` event, which may then be used with other plugins like [OctoPrint-MQTT](https://github.com/OctoPrint/OctoPrint-MQTT) to alert the user, that the printer needs attention.
The primary use for this is the Prusa MMU2S, which when it fails to load/unload filament, will halt the printer and send this message on serial.

See the plugin's [README](https://github.com/zeroflow/OctoPrint-PauseForUserEvent) for details.
