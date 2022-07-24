---
layout: plugin

id: autoprint
title: OctoPrint-Autoprint
description: Tool to automatically start the printer and prints remotely
authors:
- Christian Hofbauer
license: AGPLv3

# TODO
date: 2022-07-21

homepage: https://github.com/chof747/octoprint-autoprint
source: https://github.com/chof747/octoprint-autoprint
archive: https://github.com/chof747/octoprint-autoprint/archive/master.zip

follow_dependency_links: false

# TODO
tags:
- power
- lights
- timer
- schedule
- gpio
- psu
- psucontrol

screenshots:
- url: /assets/img/plugins/autoprint/autoprint_settings.png
  alt: Settings screenshot, describing the plugin configuration options
  caption: Settings
- url: /assets/img/plugins/autoprint/autoprint_tab.png
  alt: Tab screenshot, describing the plugin controls
  caption: Settings
- url: /assets/img/plugins/autoprint/autoprint_schematic.png
  alt: Two relais are needed to be attached to two GPIO ports in order to turn on/off the printer via the plugin
  caption: Schematic of a GPIO setup

featuredimage: /assets/img/plugins/autoprint/featured_screenshot.png

compatibility:

  python: ">=3,<4" # Python 3 only
  
  os:
  - linux

---

# Autoprint Plugin

## Concept

The octoprint autoprint plugin has the following functionalities:

1. Enable the remote powering on/off of a printer and a light above the printer via two distinct
   GPIO pins (which are most likely connected to relais) - also exposing these GPIOs
2. Automatically disconnect and turn off the printer after a print is finished - with the option
   to wait for a proper cool down of the nozzle
3. Start the printer and begin printing a specific file either at a given time or at a time
   so that the print will be finished as specified 
4. Automatically turning off the printer after the scheduled print job has finished

To fully use the autoprint plugin you need to be able to control your printers power supply as well as the light illuminating the printer via GPIOs and e.g. attached relais that are switching the power (see also the example below). 

## Use

### Settings

The plugin can be configured with the following parameters (see also screenshot "Settings" below)

| Parameter                   | Type/Default    | Description                                           |
|-----------------------------|-----------------|-------------------------------------------------------|
| Printer Power               | GPIO Pin Number (BCM) | GPIO Pin triggering the power of the printer - this is usually connecte to a relay |
| Printer Light               | GPIO Pin Number (BCM) | GPIO Pin triggering the lights of the printer - should also be connected to a relay or a MOSFET turning on/off a led strip |
| Printer Startup Time        | Seconds               | Time delay the plugins waits after starting up the printer before it tries to connect to it
| Nozzle Cooldown Temperature | °C                    | After printing or when getting a shutdown command, the plugin waits until the nozzle has cold down below this threshold to avoid turning off the printer with a too hot hotend | 
| Autoprint Folder            | Folder Name           | Folder where prints are stored which are eligable for autoprinting |

### Operations

The plugin offers several options of useage:

1. **Manually turning on the power of the printer and lights:**

   - You can use the "Start up Printer" button on the top left to switch the printer and the lights on and off at   the same time. If the printer is on the button is showing the alternate text "Shut Down Printer"

   - As soon as the printer and/or the lights are on the icons right of the button switch to the color yellow

   - After the printer has been turned on and the startup time has passed (configuration), the plugin will try to connect octoprint to the printer

   - As soon as the printer is connected the printer icon turns green

2. **Manually turning off the printer and the lights:**

   When the printer is on (and connected) the button on the top left corner of the tavb shows "Shut Off Printer". In this state you can turn off the printer at any time which will trigger the following process:

   - Wait until the printer hotend has cooled down sufficiently (below the configurable _Nozzle Cooldown Temperatur_)

   - As soon as the nozzle is cool enough the printer will be disconnected from octoprint 
   
   - Lights and printer are shut down

During the cooldown process you can cancel the shutdown of the printer at any time by pressing the button on  the top left which is in this phased labelled as "Cancel Shut Down"

---
  
**Note:** The lights icon is also triggering the lights. When clicking on it you can toggle the state of the lights regardless of the state of the printer (e.g. for turning on the lights to check your printer while off or for turning them off while printing)

---

3. Autoprinting

The plugin allows to schedule a print for a later time with the following options:

- Select a file from a specific folder that has been defined in the settings
- Choose either the start or the end time
- Check wether the printer should shutdown after the print has finished

The autoprint controls are available on the tab of the plugin (see picture below) and are only available if the printer is neither printing, paused nor pausing a print.

A printed job can be cancelled any time before the print starts.

---

**Warning:** The plugin does not check any precondition for printing a scheduled job except the calculated time. Be therefore aware that the printbed and all other conditions must be given when scheduling a print job. There are no checks done by the plugin. The job is simply started regardless of the real conditions.

---

**Warning:** Be aware that running print jobs unattended is a security risk and should not be done in general.

---


## Next steps

1. Consider using all files for autoprinting