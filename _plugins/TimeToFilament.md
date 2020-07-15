---
layout: plugin

id: TimeToFilament
title: OctoPrint-TimeToFilament
description: Display time until next filament change
author: eyal0
license: AGPLv3

date: 2020-07-15

homepage: https://github.com/eyal0/OctoPrint-TimeToFilament
source: https://github.com/eyal0/OctoPrint-TimeToFilament
archive: https://github.com/eyal0/OctoPrint-TimeToFilament/archive/master.zip

tags:
- filament
- time
- remaining
- change

screenshots:
- url: /assets/img/plugins/TimeToFilament/screenshot.png
  alt: Screenshot of TimeToFilament showing the time until next filament change and the time until the next layer.
  caption: Added to the display.

# TODO
featuredimage: /assets/img/plugins/TimeToFilament/screenshot.png

---

TimeToFilament can show you the time until the next filament change in
your print.  It can also show the time until your next layer will
start.  In fact, it's extensible and can show you whatever you want if
you configure it through the settings!

How it works:

TimeToFilament scans through your gcode looking for a line that you
specify.  Then it parses the text on that line and sends it to your
browser along with how many seconds until the printer will reach that
line.  Your browser will use that to create some text to display right
below the total time to print.

If you know [how to write a regular
expression](https://regexone.com/), you can make your own.  If you
need this and have trouble with it, [file a request](https://github.com/eyal0/OctoPrint-TimeToFilament/issues/new).

http://plugins.octoprint.org/plugin/TimeToFilament/
