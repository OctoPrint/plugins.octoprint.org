---
layout: plugin

id: custom_gcode_events
title: OctoPrint-Custom_gcode_events
description: Enables the User to configure custom GCode hooks (both sent and received) that will fire a User-defined event to be picked up by other plugins.
authors:
- RoboMagus
license: AGPLv3

date: 2022-01-02

homepage: https://github.com/RoboMagus/OctoPrint-Custom_gcode_events
source: https://github.com/RoboMagus/OctoPrint-Custom_gcode_events
archive: https://github.com/RoboMagus/OctoPrint-Custom_gcode_events/archive/master.zip

tags:
- GCode hooks
- Event
- Notify
- Paused

compatibility:
  python: ">=3,<4"

---

This plugin enables you to configure G-Code hooks (sent or received) that will fire custom events which can then be picked up by another plugin, such as [OctoPrint-MQTT](https://github.com/OctoPrint/OctoPrint-MQTT).

My usecases are mostly to be notified through Home Assistant notifications when my printer requires some attention.
```GCode received --> Fire event --> OctoPrint-MQTT: Translate event to MQTT --> Home Assistant: Automation is triggered that notifies me.```