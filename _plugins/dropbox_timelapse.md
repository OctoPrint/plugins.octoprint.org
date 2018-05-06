---
layout: plugin

id: dropbox_timelapse
title: OctoPrint-Dropbox-Timelapse
description: Automatically upload rendered timelapses to Dropbox. Can also delete after upload to save space on the Raspberry Pi SD Card.
author: Justin Slay
license: AGPLv3

date: 2018-05-06

homepage: https://github.com/jslay88/OctoPrint-Dropbox-Timelapse
source: https://github.com/jslay88/OctoPrint-Dropbox-Timelapse
archive: https://github.com/jslay88/OctoPrint-Dropbox-Timelapse/archive/master.zip

tags:
- timelapse
- dropbox

---

## Configuration

You must provide an API Token to be able to upload rendered timelapses to Dropbox.
To do this, [create a Dropbox App](https://www.dropbox.com/developers/apps/create)
select `Dropbox API` -> `App Folder` -> Provide Folder Name.
Once the app is created, scroll down to the `OAuth 2` section, and click `Generate Token`. Paste the token into the
settings pane.
