---
layout: plugin

id: BetterHeaterTimeout
title: OctoPrint-BetterHeaterTimeout
description: Turns off heaters after specified time being on and unused
author: T6
license: AGPLv3

date: 2019-01-02

homepage: https://github.com/tjjfvi/OctoPrint-BetterHeaterTimeout
source: https://github.com/tjjfvi/OctoPrint-BetterHeaterTimeout
archive: https://github.com/tjjfvi/OctoPrint-BetterHeaterTimeout/archive/master.zip

tags:
- temperature
- heater
- timeout
- heater timeout
- custom event

screenshots:
- url: /assets/img/plugins/BetterHeaterTimeout/timedout.png
  alt: Image showing heater timeout
- url: /assets/img/plugins/BetterHeaterTimeout/settings.png
  alt: Screenshot of settings

featuredimage: /assets/img/plugins/BetterHeaterTimeout/timedout.png

---

*Note: this plugin has not been tested with versions under 1.3.10; they may not work!*

### Advantages:
 - Supports configuring timeout length
 - Supports before/after gcode
 - Supports notification via Web UI
 - Fires a custom event _*_ when the heaters timeout, so one can be notified or otherwise hook on the event.

_*May not be (officially) supported; see [#2965](https://github.com/foosel/OctoPrint/issues/2965) for more info._

### Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/tjjfvi/OctoPrint-BetterHeaterTimeout/archive/master.zip

If you want to trigger on the custom event, use the event name `HeaterTimeout`.
The payload values are `heater`, `time_elapsed`, and `timeout`.


### Configuration

The checkbox enables/disables the timeout, and the number input changes the timeout length.

#### After target temp changes vs after heating starts

If set to the former, changing the target temp will reset the timeout.

#### Before/after GCODE

GCODE commands to run before/after the heaters are disabled.
You can use the placeholders `$heater`, `$time_elapsed`. and `$timeout`.
I think the names are pretty self-explanatory.

**Examples:**
```
M117 $heater timed out ; display that on the screen
```
```
M300 S100 P200 ; chirp
```
