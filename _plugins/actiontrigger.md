---
layout: plugin
id: actiontrigger
title: Action Trigger Plugin
description: Plugin for OctoPrint that handles serial commands sent out by the printer.
homepage: https://github.com/Booli/OctoPrint-ActionTriggerPlugin
source: https://github.com/Booli/OctoPrint-ActionTriggerPlugin
author: Pim Rutgers
license: AGPLv3
archive: https://github.com/Booli/OctoPrint-ActionTriggerPlugin/archive/master.zip
date: 2015-04-17
tags:
- printing
---
compatibility:
  python: ">=2.7,<4"

> Its gun do some serial trigger handling yo

Plugin for OctoPrint that handles serial commands send out by the printer. These action triggers should be manually added to your firmware if you want to use this add-on.  Basic handler code is:

    // action:somevariable

Plugin reacts to two different situations, door open/close and filament detection.

    action:door_open
    action:door_closed

``action:door_open`` will pause the print and home the X-axis. Pop-up dialog will notify the user, they can decide to accept the pop-up and use the controls. Closing the door will trigger ``action:door_closed`` resume the print and close the dialog

    action:filament

This trigger will pause the print and home the X and Y axis, giving the user the opportunity to change out the filament. The print needs to be resumed manually through the UI.
