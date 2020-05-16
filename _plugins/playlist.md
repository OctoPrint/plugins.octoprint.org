---
layout: plugin

id: playlist
title: Playlist
description: Create's a playlist of gcode files to automatically print back to back.
author: jneilliii
license: AGPLv3

date: 2020-05-16

homepage: https://github.com/jneilliii/OctoPrint-Playlist
source: https://github.com/jneilliii/OctoPrint-Playlist
archive: https://github.com/jneilliii/OctoPrint-Playlist/archive/master.zip

follow_dependency_links: false

tags:
- print queue
- playlist
- consecutive

compatibility:
  python: ">=2.7,<4"

featuredimage: /assets/img/plugins/playlist/screenshot_tab.png

---

# OctoPrint-Playlist

This plugin will allow you to create a playlist of gcode files that will automatically play one after another with a configured set of gcode commands in between. There are options for configuring "black out" windows where the printing does not occur, and a start time for when to automatically start the playlist.

To add files to the playlist, press the newly created "Add to Playlist" button in OctoPrint's file list.

![button](/assets/img/plugins/playlist/screenshot_button.png)

Once clicked the file will be added to the Playlist tab where you can manage the files in the playlist and set options for auto starting at a certain time and auto-repeating the playlist once all files have been printed.

![tab](/assets/img/plugins/playlist/screenshot_tab.png)

Additional plugin settings can be found in OctoPrint's settings interface where you can set the gcode commands to run between each file in the playlist. You can configure the gcode to use for removing the beginning and end of the file. This is helpful for removing start/end gcode scripts configured in your slicer that are not necessary during sequential playback. The last group of options are for configuring the "black out" window for automatically pausing and resuming playback. 

![button](/assets/img/plugins/playlist/screenshot_settings.png)

## Tips

A couple of helpful gcode commands to use in between the files are listed below, but I highly recommend you know what your specific firmware is capable of and what [gcode commands](https://reprap.org/wiki/G-cod) are compatible. Each user's use case may be different; you may want to clear a sand art printer to erase the previous design or for 3D printing you may want to use the gantry to push the part off the front/back/side of the bed, etc.

* [M104 S80](https://reprap.org/wiki/G-code#M104:_Set_Extruder_Temperature) ; Set nozzle temperature without waiting to prerevent oozing on printed parts.
* [M109 S80](https://reprap.org/wiki/G-code#M109:_Set_Extruder_Temperature_and_Wait) ; Set nozzle temperature and wait for temperature to be reached before performing next commands.
* [M190 S30](https://reprap.org/wiki/G-code#M190:_Wait_for_bed_temperature_to_reach_target_temp) ; Set and wait for bed temperature to reach 30 degrees, allowing the bed to cool down and letting the part release.
* [G90](https://reprap.org/wiki/G-code#G90:_Set_to_Absolute_Positioning)/[G91](https://reprap.org/wiki/G-code#G91:_Set_to_Relative_Positioning) ; switch between relative and absolute nozzle positioning, G90 is highly recommended before moving the nozzle to specific coordinates like the next example.
* [G0 X0 Y200](https://reprap.org/wiki/G-code#G0_.26_G1:_Move) ; Move the nozzle out of the way, follow up with additional G0 commands to move the gantry to the back center of the bed and then move forward to push the released part off the front of the bed.
* [G4 S600](https://reprap.org/wiki/G-code#G4:_Dwell) ; Wait for 600 seconds.

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

### Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip if you find this plugin helpful.

![PayPal](/assets/img/plugins/playlist/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>
