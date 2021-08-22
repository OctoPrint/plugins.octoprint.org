---
layout: plugin

id: printscheduler
title: Print Scheduler
description: Plugin that allows to schedule prints to run at a specified time.
authors:
- jneilliii
license: MIT

date: 2021-08-21

homepage: https://github.com/jneilliii/OctoPrint-PrintScheduler
source: https://github.com/jneilliii/OctoPrint-PrintScheduler
archive: https://github.com/jneilliii/OctoPrint-PrintScheduler/archive/master.zip

tags:
- scheduler
- cron
- schedule
- queue
- CR-30
- belt printers

featuredimage: /assets/img/plugins/printscheduler/screenshot_tab.png

compatibility:
  octoprint:
  - 1.6.1
  os:
  - linux
  - windows
  - macos
  - freebsd
  python: ">=3,<4"

---

# Print Scheduler

Plugin that allows for scheduling prints to happen. If a print is ongoing or the printer is not in an operational state, the plugin will try to print those again until it is possible to start the print.

**WARNING**: This plugin currently only has knowledge of your printer's state. If your printer is showing operational in OctoPrint, the next scheduled print job will run even if something is on the bed. Take caution when adding multiple prints to the scheduler for this reason.

## Screenshots

![Print Scheduler Tab](/assets/img/plugins/printscheduler/screenshot_tab.png)


![Print Scheduler Settings](/assets/img/plugins/printscheduler/screenshot_settings.png)

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

### Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip or become a Patron if you find this plugin helpful and want me to continue future development.

[![Patreon](/assets/img/plugins/printscheduler/patreon-with-text-new.png)](https://www.patreon.com/jneilliii) [![paypal](/assets/img/plugins/printscheduler/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>


