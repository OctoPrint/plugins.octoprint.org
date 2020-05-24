---
layout: plugin

id: Octoslack
title: Octoslack
description: An OctoPrint plugin for monitoring your printer and prints via Slack, Mattermost, Pushbullet, Pushover, Rocket.Chat, Discord, Riot/Matrix, or Microsoft Teams
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
- pushbullet
- pushover
- rocket chat
- matrix
- riot
- discord
- microsoft teams
- notification
- progress
- mobile
- monitor
- monitoring
- remote monitoring
- filament runout
- s3
- imgur 
- minio
- gcode
- camera
- webcam
- eta
- finish time
- print time
- snapshots
- status
- alert
- gcode

screenshots:
- url: /assets/img/plugins/Octoslack/Octoslack-PrintStarted.png
  alt: Slack/Mattermost - Print started
  caption: Slack/Mattermost - Print started
- url: /assets/img/plugins/Octoslack/Octoslack-PrintProgress.png
  alt: Slack/Mattermost - Print progress
  caption: Slack/Mattermost - Print progress
- url: /assets/img/plugins/Octoslack/Octoslack-PrintFinished.png
  alt: Slack/Mattermost - Print finished
  caption: Slack/Mattermost - Print finished
- url: /assets/img/plugins/Octoslack/Octoslack-Pushbullet-PrintStarted.png
  alt: Pushbullet - Print started
  caption: Pushbullet - Print started
- url: /assets/img/plugins/Octoslack/Octoslack-Pushover-PrintStarted.png
  alt: Pushover - Print started
  caption: Pushover - Print started
- url: /assets/img/plugins/Octoslack/Octoslack-RocketChat-PrintStarted.png
  alt: Rocket.Chat - Print started
  caption: Rocket.Chat - Print started
- url: /assets/img/plugins/Octoslack/Octoslack-Matrix-PrintStarted.png
  alt: Matrix/Riot.im - Print started
  caption: Matrix/Riot.im - Print started
- url: /assets/img/plugins/Octoslack/Octoslack-GcodeEventCommand.png
  alt: G-code event & System command
  caption: G-code event & System command

featuredimage: /assets/img/plugins/Octoslack/Octoslack-PrintProgress_SlackOnly.png

---


An OctoPrint plugin for monitoring your printer and prints via Slack, Mattermost, Pushbullet, Pushover, Rocket.Chat, or Riot/Matrix

# Features #
 - Support for Slack, Mattermost, Pushbullet, Pushover, Rocket.Chat, Discord, Matrix based platforms (e.g. Riot), & Microsoft Teams
 - Monitor both print status as well as printer connectivity status
 - Respond to Slack commands to check print status or cancel/pause/resume a print
     - Each command can be individually enabled/disbaled or flagged as restricted which limits the command(s) to specific users
     - Requires use of the Slack App Bot Token
 - Customizable messages
     - Slack and Mattermost support for a fallback message (e.g. mobile notification)
     - Pushover support for event specific sound and priority settings
 - Support for posting to one more channels as well as event level channel overrides
 - Support for inclusion of RasPi temperature, bed temperature, nozzle temperates, nozzle height, and device IP(s)
 - Support for local system command execution
 - Slack bot name/icon/emoji customizations
     - Requires use of the Slack App Bot Token
 - Optional inclusion of printer snapshot images with each message
     - Support for snapshot hosting via Amazon S3, Minio, Imgur (with album support), Slack attachments, Pushover, Pushbullet, Rocket.Chat, Discord, or Matrix
     - Slack attachments requires use of the Slack App Bot Token
 - Optional upload of rendered timelapse video to configured hosting service
     - Currently excludes Imgur, Pushover, Rocket.Chat, Discord, & Matrix
 - Support for additional snapshot images from IP cameras

# Supported Events #
 - Print started
 - Print failed
 - Print cancelling
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
 - Timelapse render finished (including Octolapse timelapses)
 - Timelapse render failed
 - File analysis started
 - File analysis finished
 - OctoPrint error
 - OctoPrint started
 - OctoPrint stopped
 - Printer connecting
 - Printer connected
 - Printer disconnecting
 - Printer disconnected
