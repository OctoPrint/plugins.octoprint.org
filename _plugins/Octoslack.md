---
layout: plugin

id: Octoslack
title: Octoslack
description: An OctoPrint plugin for monitoring your printer and prints via Slack or Mattermost
author: Chris Fraschetti
license: MIT

# today's date in format YYYY-MM-DD, e.g.
date: 2017-05-20

homepage: https://github.com/fraschetti/Octoslack
source: https://github.com/fraschetti/Octoslack
archive: https://github.com/fraschetti/Octoslack/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- slack
- mattermost
- notification
- progress
- mobile
- monitor
- monitoring
- remote monitoring
- filament runout
- s3
- imgur 
- gcode
- camera
- webcam
- eta
- finish time
- print time
- snapshots
- status

screenshots:
- url: /assets/img/plugins/Octoprint/Octoslack-PrintStarted.png
  alt: Print started
  caption: Print started
- url: /assets/img/plugins/Octoprint/Octoslack-PrintProgress.png
  alt: Print progress
  caption: Print progress
- url: /assets/img/plugins/Octoprint/Octoslack-PrintFinished.png
  alt: Print finished
  caption: Print finished

featuredimage: /assets/img/plugins/Octoprint/Octoslack-PrintProgress_SlackOnly.png

---


An OctoPrint plugin for monitoring your printer and prints via Slack or Mattermost

# Features #
 - Support for both Slack and Mattermost
 - Monitor both print status as well as printer connectivity status
 - Slack+Mattermost WebHooks and Slack API Token
 - Respond to Slack commands to check print status or cancel/pause/resume a print
     - Requires use of the Slack API Token
 - Customizable messages
 - Support for posting to one more channels as well as event level channel overrides
 - Support for inclusion of RasPi temperature, bed temperature, nozzle temperates, and nozzle height
 - Custom bot name/icon/emoji
 - Optional inclusion of printer snapshot images with each message
     - Support for snapshot hosting via Amazon S3, Minio, Imgur (with album support), or Slack attachments
     - Slack attachments requires use of the Slack API Token
 - Optional upload of rendered timelapse video to configured hosting service
     - Excluding Imgur which does not support video uploads
 - Support for additional snapshot images from IP cameras

# Supported Events #
 - Print started
 - Print failed
 - Print cancelled
 - Print paused
 - Print resumed
 - Print finished
 - Print progress (% complete)
 - Print progress (time interval)
 - Print progress (Z height change)
 - G-code sent to the printer
 - G-code received from the printer (including filament runout messages)
 - Timelapse render started
 - Timelapse render finished
 - Timelapse render failed
 - OctoPrint error
 - OctoPrint started
 - OctoPrint stopped
 - Printer connecting
 - Printer connected
 - Printer disconnecting
 - Printer disconnected

