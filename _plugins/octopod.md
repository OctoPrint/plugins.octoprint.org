---
layout: plugin

id: octopod
title: OctoPrint-OctoPod
description: OctoPrint plugin for OctoPod
author: Gaston Dombiak
license: Apache-2.0

# TODO
date: 2019-05-26

homepage: https://github.com/gdombiak/OctoPrint-OctoPod
source: https://github.com/gdombiak/OctoPrint-OctoPod
archive: https://github.com/gdombiak/OctoPrint-OctoPod/archive/master.zip

# TODO
# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

# TODO
tags:
- octopod
- bed temperature
- print finished
- iOS
- notifications

# TODO
screenshots:
- url: /assets/img/plugins/octopod/settings.png
  alt: Configure Notifications
  caption: Configure Notifications
- url: /assets/img/plugins/octopod/print_finished.jpg
  alt: Print Finished
  caption: Print Finished
- url: /assets/img/plugins/octopod/bed_cooled.jpg
  alt: Bed Cooled Down
  caption: Bed Cooled Down

# TODO
featuredimage: /assets/img/plugins/octopod/print_finished.jpg

---

This plugin sends immediate push notifications to your iOS devices when:
* your print has finished. Notifications include a snapshot of your camera. If you
have multiple cameras then you can include a snapshot of any of them. Even if the
cameras are not connected to OctoPrint you can still make use of them
* bed has cooled down enough so you can remove your print
* bed has warmed up to target temperature for a specified period so you can start
printing knowing that bed's material won't expand anymore

If you are using the free and open source [OctoPod](https://itunes.apple.com/us/app/octopod-for-octoprint/id1412557625?mt=8)
to control your printer from any iOS device then this plugin is a great addition. If you
never heard of [OctoPod](https://itunes.apple.com/us/app/octopod-for-octoprint/id1412557625?mt=8)
before then you are in for a treat. Here are some of its features: multiple printers support,
multiple cameras support including full screen with zoom in/out, control your printer using
Siri or from your Apple Watch, temperature charts including temp variance. You can cancel any object
being printed since it has support for [Cancel object plugin](https://plugins.octoprint.org/plugins/cancelobject/).
But that is not the only supported plugin, here are other supported plugins: [TPLink](https://plugins.octoprint.org/plugins/tplinksmartplug/),
[PSU Control](https://github.com/kantlivelong/OctoPrint-PSUControl), [Domoticz](https://plugins.octoprint.org/plugins/domoticz/),
[Belkin Wemo](https://plugins.octoprint.org/plugins/wemoswitch/), [Tasmota](https://plugins.octoprint.org/plugins/tasmota/) and
[Custom Control ](https://plugins.octoprint.org/plugins/customControl/). And now with this new
OctoPrint plugin we added real time notifications for some very useful features.

## Installation

Installation is super easy. There is no need to change your router configuration, do
port forwarding or open holes in your firewall. Just follow these steps and you will
be up and running in no time.

1. Download and install this plugin as you would do with any other OctoPrint plugin
1. Download [OctoPod](https://itunes.apple.com/us/app/octopod-for-octoprint/id1412557625?mt=8) from the App Store
1. Start [OctoPod](https://itunes.apple.com/us/app/octopod-for-octoprint/id1412557625?mt=8) so
it can receive notifications. This step is required for testing the plugin
1. Go to OctoPrint settings and configure this plugin
  * If needed, update _Snapshot URL_ to point to the camera that will provide an image when your print is finished
  * Click on _Send test notification_ to confirm setup is operational
  * Configure _Bed Notifications_ to receive cooled down or warm up bed events
  * Save settings and enjoy
