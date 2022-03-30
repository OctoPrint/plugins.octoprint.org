---
layout: plugin

id: pwmbuzzer
title: OctoPrint-PWMBuzzer
description: Uses PWM via GPIO to sound tones whenever an M300 command is encountered
authors:
- Matt Bielich
license: AGPLv3

date: 2022-03-29

homepage: https://github.com/stealthmonkey99/OctoPrint-PWMBuzzer
source: https://github.com/stealthmonkey99/OctoPrint-PWMBuzzer
archive: https://github.com/stealthmonkey99/OctoPrint-PWMBuzzer/archive/master.zip

tags:
- gpio
- pwm
- buzzer
- beep
- m300
- music
- gcode

screenshots:
- url: /assets/img/plugins/pwmbuzzer/config.png
  alt: Configuration settings panel
  caption: Configuration of Hardware and Software buzzers for handling M300 commands
- url: /assets/img/plugins/pwmbuzzer/events.png
  alt: Events settings panel
  caption: Link system and printer events to M300 tunes that play when they are triggered
- url: /assets/img/plugins/pwmbuzzer/composer.png
  alt: Composer settings panel
  caption: Use the tools in the Composer tab to easily generate your own M300 tunes

featuredimage: /assets/img/plugins/pwmbuzzer/composer.png

compatibility:

  os:
  - linux

  python: ">=3,<4"

---

# OctoPrint-PWMBuzzer

If your 3D printer doesn't have a speaker or natively support M300 commands for making beeps, this plugin is for you!

You can use a simple (and cheap) passive buzzer, attach it to your Raspberry Pi's GPIO pins, and route M300 commands through it using Pulse-Width Modulation (PWM).  Simply connect your passive buzzer to a ground pin and the (+) side to a triggering GPIO pin, like GPIO16 (BCM).  You can find more details online in various tutorials ([example](https://github.com/stealthmonkey99/OctoPrint-PWMBuzzer)).

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/stealthmonkey99/OctoPrint-PWMBuzzer/archive/master.zip

## Configuration

Once you have connected your passive buzzer to your Raspberry Pi and installed the plugin, launch the plugin settings dialog in your OctoPrint client to configure it.

![Configuration Panel](/assets/img/plugins/pwmbuzzer/config.png)

From here you can enable the passive buzzer and indicate which GPIO pin the (+) side is connected to.  You may want to play around with the Duty Cycle setting to see what works best for your buzzer.  These buzzers won't sound _great_ but they'll get the job done!

Optionally, you might also choose to enable a software buzzer that simulates M300 commands in your web browser while you're actively connected to OctoPrint.  This has not been tested in all browsers yet, but you're welcome to try it out.

Once you have chosen your buzzer configuration settings you can test them out (hardware and/or software) using the "Play Default Tone" button.  You can also set a default frequency and duration to be played any time an M300 command is encountered without parameters.

Don't forget to save your settings before you continue!

## Events

Here's where the magic happens... not only can your printer now handle M300 commands, but you can set up your OctoPrint instance to play music when certain events occur!

![Events Panel](/assets/img/plugins/pwmbuzzer/events.png)

Next to each event you'll see a drop-down for selecting a preset or any .gcode files found in your local storage (not SD card) that contain M300 commands.  Select whatever tune you'd like, then click "Try it" to play it.  Keep in mind that you'll need to have saved your settings on the Configurations settings panel before trying to play these M300 commands.

> NOTE: if you upload or save new .gcode files, you'll need to restart OctoPrint before they'll show up in the Events settings panel.

## Composer

Feeling creative?  Use the Composer settings panel to generate your own tunes for playback!

![Composer Panel](/assets/img/plugins/pwmbuzzer/composer.png)

Just press-and-hold any of the piano keys to hear them.  When you release the key, it will save your "note" as generated Gcode.  There are also some tools below the generated Gcode that you might find helpful:

- Hit a wrong note?  Use the "Undo" button to quickly remove the last note you pressed.
- Need a rest between notes?  "Insert Pause" will drop one at the end of your composition.
- Use "Reverse" to play your composition backwards... you can always hit "Reverse" again to put it back.
- Make your tune more rigid and robotic using the "Snap Durations" button.  This will try to normalize the durations of your notes.
- "Clear" simply empties out your composition so you can start on another one.
- "Send Gcode to Printer" is an easy way to play back your composition.
- Once you have finalized your masterpiece you can use the drop-down options to:
  - "Save Gcode File" in your local storage (SD card storage not supported) under the "M300 Compositions" folder
  - "Download Gcode" so you have a copy on your computer
  - "Copy Gcode to Clipboard" if you want to paste it into an email, etc.

## Support & Contributing

This is my first OctoPrint plugin and it's still a bit experimental.  Please feel free to open issues if you encounter any bugs.  I'm also happy to take contributions if you'd like to open a pull request to make any changes.

I hope you find this useful and fun!  If you like my plugin or want to support my random coding projects you can always
[![Buy me a coffee](/assets/img/plugins/pwmbuzzer/bmc-button-sm.png)](https://www.buymeacoffee.com/mbielich)

Enjoy!
