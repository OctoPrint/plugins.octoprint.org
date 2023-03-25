---
layout: plugin

id: octotuya
title: OctoTuya-SmartPlug
description: Controls Tuya-based SmartPlugs either directly from Octoprint Web interface or through GCODE commands
authors:
- andrelucca
#- second autor name
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2023-03-25

homepage: https://github.com/andrelucca/OctoTuya-SmartPlug
source: https://github.com/andrelucca/OctoTuya-SmartPlug
archive: https://github.com/andrelucca/OctoTuya-SmartPlug/archive/main.zip

# Set this if your plugin heavily interacts with any kind of cloud services.
#privacypolicy: your plugin's privacy policy URL

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- tuya
- smartoutlet
- smartplug
- poweroffprinter
- poweronprinter
- remotecontrol

screenshots:
- url: /assets/img/plugins/octotuya/top.png
  alt: Top Octoprint Bar with plugin enabled
  caption: Top Octoprint Bar with plugin enabled
- url: /assets/img/plugins/octotuya/settings.png
  alt: Main settings of the plugin
  caption: Main settings of the plugin
- url: /assets/img/plugins/octotuya/OctoTuyaDeviceEditor.png
  alt: Smart Device settings of the plugin
  caption: Smart Device settings of the plugin

featuredimage: /assets/img/plugins/octotuya/OctoTuyaDeviceEditor.png

# You only need the following if your plugin requires specific OctoPrint versions or
# specific operating systems to function - you can safely remove the whole
# "compatibility" block if this is not the case.

compatibility:
  python: '>=2.7,<4'

---

# OctoTuya-SmartPlug
With this plugin you'll be able to control [Tuya-based](https://en.tuya.com/) SmartPlugs either directly from Octoprint Web interface or through GCODE commands<br>

Work based on [OctoPrint-octotuya](https://github.com/ziirish/OctoPrint-octotuya). <br>
The original plugin by [ziirish](https://github.com/ziirish) was a must have to my 3D printing setup since my printer is connect to a Tuya smart outlet.<br>
But after going to the whole process of finding the required information to use the plugin I found out that it was not working properly and its been a couple of months since it was not updated, therefore forking the original repository and opening a Pull Request wasn't the best option.<br>
So I decide to look into its code and work the problems that I found, adding some changes to improve his work and a nice Wiki to guide users to the process of using it.<br>
This version of the plugin uses the tinytuya API to do the communications instead of the pytuya API. The tinytuya proved in my tests to be more reliable in terms of keeping comunication stable with the device and be more compatible as well.

<br>

## Disclaimer

Tuya is by far the most difficult IoT plataform that can be used to control devices by third-part software like this plugin, they require very specific information on the devices and change often their IoT Cloud Service.<br>
Many user have given up on using Tuya devices with OctoPrint because of its difficulty, some changed to other brands, other dug deeper and changed the device firmware or completely changed the device microcontroler, literally soldering a new one.<br>
If you, like me, only have Tuya devices and doesn't feel confortable on doing firmware flashes or resoldering, this plugin has a place on your OctoPrint instalation and its worth of your time configuring it. <br><br>
This plugin still needs improvements on the code itself, UI, performance and other elements, so you are more then welcome to open [PullRequests](https://github.com/andrelucca/OctoTuya-SmartPlug/pulls) with code updates/fixes or [Issues](https://github.com/andrelucca/OctoTuya-SmartPlug/issues) regarding what needs to be fixed. <br>
This is of course a side project of mine that unites two subjects that I like, so if you open a PR, Issue or a Discussion topic I'll answer as soon as I can, don't be angry if it takes more time than you think it should :). 

## How it was tested?

I tested all the plugin features using my Ender 3 V2 (Using original Marlin as Firmware that I configured and compiled) connected to the Octoprint v1.8.7. The Raspberry of my Octoprint is connected on the PSU of the printer, so if I power of the printer using the Tuya outlet it will also power-off the Raspberry (and will do it unsafely if I hadn't shutdown the Pi OS properly).

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/andrelucca/OctoTuya-SmartPlug/archive/main.zip

## Preparatory Work

All Tuya devices requires 2 infos in order to be controled by other software: `Device ID` and `Local Key`<br>
And this is were the greater difficulty takes place. I made a full guide on how obtain this info in this project [Wiki](https://github.com/andrelucca/OctoTuya-SmartPlug/wiki) so make sure you follow it and have this infos before installing an using this plugin.

## Configuration and Settings

All details on how to configure the plugin and how to change its settings according to your liking are in this project [Wiki](https://github.com/andrelucca/OctoTuya-SmartPlug/wiki)