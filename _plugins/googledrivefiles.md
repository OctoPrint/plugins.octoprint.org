---
layout: plugin

id: googledrivefiles
title: Google Drive Files
description: Adds Google Drive file access from within OctoPrint's file manager.
authors:
- jneilliii
license: AGPLv3

date: 2022-01-22

homepage: https://github.com/jneilliii/OctoPrint-GoogleDriveFiles
source: https://github.com/jneilliii/OctoPrint-GoogleDriveFiles
archive: https://github.com/jneilliii/OctoPrint-GoogleDriveFiles/archive/master.zip

tags:
- google
- cloud
- sync

featuredimage: /assets/img/plugins/googledrivefiles/screenshot_filelist.png

compatibility:
  octoprint:
  - 1.2.0
  os:
  - linux
  - windows
  - macos
  - freebsd
  python: ">=3,<4"

attributes:
- cloud

---

# Google Drive Files

This plugin will sync a configured folder in your Google Drive locally to your OctoPrint instance.

![screenshot](/assets/img/plugins/googledrivefiles/screenshot_filelist.png)

## Configuration

Once the [Prerequisites](https://github.com/jneilliii/OctoPrint-GoogleDriveFiles#create-a-google-oauth-app) are met and you have downloaded your client_secrets.json file follow the steps [here](https://github.com/jneilliii/OctoPrint-GoogleDriveFiles#configuration) to authorize the plugin to your newly created OAuth app.

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

### Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip or become a Patron if you find this plugin helpful and want me to continue future development.

[![Patreon](/assets/img/plugins/googledrivefiles/patreon-with-text-new.png)](https://www.patreon.com/jneilliii) [![paypal](/assets/img/plugins/googledrivefiles/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>
