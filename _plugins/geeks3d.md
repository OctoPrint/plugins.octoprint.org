---

layout: plugin

id: geeks3d
title: OctoPrint-3DGeeks
description: Companion plugin for 3D Geeks (Android & iOS App)
author: Toby from 3D Geeks
license: Apache-2.0

date: 2020-06-22

homepage: https://www.3dgeeks.app
source: https://github.com/2BWorks/OctoPrint-3DGeeks
archive: https://github.com/2BWorks/OctoPrint-3DGeeks/archive/master.zip


##

tags:

- 3dgeeks
- push
- print finished
- print started
- Android
- notifications

compatibility:
python: ">=2.7,<4"

featuredimage: /assets/img/plugins/geeks3d/featured.png

screenshots:
- url: /assets/img/plugins/geeks3d/octoprint_settings.png
  alt: OctoPrint Settings Screen
  caption: OctoPrint Settings Screen

- url: /assets/img/plugins/geeks3d/app_setup.png
  alt: App Setup
  caption: App Setup

- url: /assets/img/plugins/geeks3d/app_notification.png
  alt: Print Progress Notification
  caption: Print progress Notification

---

# 3D Geeks

{% include youtube.html vid="E-0v3v7pcBc" preview="'/assets/img/plugins/geeks3d/video.png'" %}




This plugin is created as a companion plugin to the [3D Geeks](https://www.3dgeeks.app) app.

It allows you to connect your OctoPrint instance with the 3D Geeks app for quick one-click configuration. Which removes the needs to manually type in IP addresses en port numbers, which is super error-prone.

The plugin also allows you to receive push notifications with a status update from your OctoPrint instance. It currently supports the following events:

- Print started
- Print finished
- Print failed
- Print progress
- Printer connected
- Printer disconnected
- Octoprint startup
- Octoprint shutdown



## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/2BWorks/OctoPrint-3DGeeks/archive/master.zip


## Usage
### Instance configuration
After installation restart OctoPrint, and go to the Settings tab. You should see a new tab named 3D Geeks, go ahead and click that tab. You should be presented with a QR Code.

On your Android powered device open the 3D Geeks app, go to:
```
Settings > OctoPrint settings
```
Press the `+`-Icon in the bottom-right hand corner.

Press the scan icon, scan the QR code you're being presented. If everything goes well all the nesecary fields will be filled in automatically for you. You can now press Test connection for a quick test of the connection to your OctoPrint instance.

NOTE: Be sure you're Android device is connected to the same network as your OctoPrint instance, as they communicate through the local network. When the test succeeds you can press Create. Your OctoPrint instance is now saved and can receive files from 3D Geeks.

NOTE: You can create as much OctoPrint instances as you desire. When uploading a file, the app will ask you which instance to upload to.

### Push notifications
Enable remote notifications from within the app. And press the `Send test notification`-button from the 3D Geeks OctoPrint settings. If everything is filled in correctly you should receive a test notification on your phone.

Select the push notification categories which you would like to receive.

Don't forget to save your OctoPrint instance on the app.

### Disclaimer

Sending push notifications happens via a proxy in the form of an AWS Lambda Function. Which on it's turn triggers an Firebase Message.
If you don't want your OctoPrint instance to send requests to AWS, don't install this plugin.
The called url is:
```
https://qx8eve27wk.execute-api.eu-west-2.amazonaws.com/prod/octoprint_push
```
