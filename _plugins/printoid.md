---
layout: plugin

id: printoid
title: OctoPrint-Printoid
description: Notifications plugin for Printoid (Android app for OctoPrint)
author: Anthony Stéphan
license: Apache-2.0

date: 2020-04-30

homepage: https://github.com/anthonyst91/OctoPrint-Printoid
source: https://github.com/anthonyst91/OctoPrint-Printoid
archive: https://github.com/anthonyst91/OctoPrint-Printoid/archive/master.zip

tags:
- printoid
- bed temperature
- print finished
- Android
- notifications

compatibility:
  python: ">=2.7,<4"

screenshots:
- url: /assets/img/plugins/printoid/notif_progress_10.png
  alt: Notification on print progress
  caption: Notification on print progress
- url: /assets/img/plugins/printoid/notif_print_completed.png
  alt: Notification on print completed
  caption: Notification on print completed
- url: /assets/img/plugins/printoid/notif_temperature_alert.png
  alt: Notification on temperature alert
  caption: Notification on temperature alert

attributes:
- cloud
- commercial
- free-tier

---

This is the official plugin made for the [Printoid for OctoPrint](https://play.google.com/store/apps/details?id=fr.yochi76.printoid.phones.premium&utm_source=github&utm_medium=plugin) application.

It aims to send you push notifications to your device(s) on specific events on your OctoPrint server.
This plugin has been inspired by the great plugin made by the developer of [OctoPod](https://itunes.apple.com/us/app/octopod-for-octoprint/id1412557625?mt=8) for iOS.
He plugin (the original one) can be found [here](https://github.com/gdombiak/OctoPrint-OctoPod).
If you like the Printoid Plugin, then please support the developer of the OctoPod plugin, because he did an amazing work!

The Printoid Plugin communicates with Firebase Cloud Messaging server over a Google Cloud Function, located at the following URL:

	https://us-central1-firebase-printoid.cloudfunctions.net/printoidPluginGateway

## Prerequisites

Printoid v15.01 (at least) should be available and installed on your phone

## What CAN this plugin do for you?

This plugin sends immediate push notifications to your Android devices running
[Printoid for OctoPrint](https://play.google.com/store/apps/details?id=fr.yochi76.printoid.phones.premium&utm_source=github&utm_medium=plugin) when:

- The state of your printer is changing (to PRINTING, to PAUSED, to ERROR, and back to OPERATIONAL, for example)
- The print job reached a certain progress (every 10%, every 25% or at 50% only)
- Your print is now complete (progress = 100%)
- Your print reached specified layers (requires plugin [DisplayLayerProgress plugin](https://plugins.octoprint.org/plugins/DisplayLayerProgress/) to be installed too)
- Your heated bed reached a specific temperature (useful to know when you can easily remove your prints from the bed, or when you can get smooth first layer)
- Your extruder cooled down below a specific temperature (useful to be informed when you can safely turn off your printer)
- Your printer has been paused because it requires a user action (out of filament, or manual multi color printing or M600 detection)
- [Palette 2 / Pro](https://www.mosaicmfg.com/products/palette-2) encountered a problem while printing
- [MMU](https://shop.prusa3d.com/en/upgrades/183-original-prusa-i3-mk25smk3s-multi-material-2s-upgrade-kit-mmu2s.html#) requires user assistance (it requires Prusa firmware)
- Firmware errors (get security alerts like thermal runaway, probing failed, min temp error, max temp error...)

This plugin does not need your phone to be connected to the same network as your OctoPrint server to send the notifications.
You will be able to receive the notifications even if you are out of your home and/or connected to the cellular network (3G/4G/5G) for example.

This plugin does not need your network to be opened to the Internet. You do not need to do port forwarding, and you do not need to setup a VPN ;)

Printoid does not need to be opened on your device to receive the notifications from the plugin. The app can be killed and your phone can be sleeping, you will receive the notifications whatever happens!

## What CAN'T this plugin do for you?

This plugin is not a plugin to control your 3D printer remotely. Please be nice, don't yell at me because this was what you expected...
May be this will be possible in the future, but for the moment it would require me too much work.

This plugin only sends push to your device in order to show you notifications on your device for specific events.
This way it will not update the information contained in the app (at least for the moment).

## Setup

Install the plugin via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/anthonyst91/OctoPrint-Printoid/archive/master.zip

## Configuration

Once the plugin has been installed:

1. Open the _Settings_ panel of OctoPrint
2. Navigate to the _Plugins_ section and select _Printoid Notifications_
3. Open the Printoid application on your phone, and connect it to your OctoPrint server
4. Wait few seconds for the app to be fully refreshed
5. From the OctoPrint interface, click on the _Send test notification_ button
6. Check on your phone, you should receive your first notification!
7. The Printoid app is now paired with the Printoid plugin, you will receive notifications!
