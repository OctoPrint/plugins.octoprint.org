---
layout: plugin

id: detector2
title: OctoPrint-Detector2
description: Detects errors directly in your browser and sends email with detected error
authors:
- Mikulas Heinz
license: AGPLv3

# TODO
date: 2022-04-15

homepage: https://github.com/mikulash/OctoPrint-Detector2
source: https://github.com/mikulash/OctoPrint-Detector2
archive: https://github.com/mikulash/OctoPrint-Detector2/archive/master.zip

# TODO
# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

# TODO
tags:
- ai
- alerts
- automation
- defect detection
- email
- failure
- monitoring
- notifications
- local

# TODO
screenshots:
- url: /assets/img/plugins/detector2/mailPreview.png
  alt: received email
  caption: Email sent from plugin
- url: /assets/img/plugins/detector2/OctoprintPreview.png
  alt: octoprint integration
  caption: as tab in octoprint
- url: /assets/img/plugins/detector2/settingsPreview.png
  alt: filling out the settings
  caption: Settings page
- url: /assets/img/plugins/detector2/outlookPreview.png
  alt: outlook smtp settings
  caption: outlook smtp settings

# TODO
featuredimage: /assets/img/plugins/detector2/errorPreview.png

# TODO
# You only need the following if your plugin requires specific OctoPrint versions or
# specific operating systems to function - you can safely remove the whole
# "compatibility" block if this is not the case.

compatibility:

  # List of compatible versions
  #
  # A single version number will be interpretated as a minimum version requirement,
  # e.g. "1.3.1" will show the plugin as compatible to OctoPrint versions 1.3.1 and up.
  # More sophisticated version requirements can be modelled too by using PEP440
  # compatible version specifiers.
  #
  # You can also remove the whole "octoprint" block. Removing it will default to all
  # OctoPrint versions being supported.

  octoprint:
  - 1.4.0

  # List of compatible operating systems
  #
  # Valid values:
  #
  # - windows
  # - linux
  # - macos
  # - freebsd
  #
  # There are also two OS groups defined that get expanded on usage:
  #
  # - posix: linux, macos and freebsd
  # - nix: linux and freebsd
  #
  # You can also remove the whole "os" block. Removing it will default to all
  # operating systems being supported.

  os:
  - linux
  - windows
  - macos
  - freebsd

  # Compatible Python version
  #
  # It is recommended to only support Python 3 for new plugins, in which case this should be ">=3,<4"
  #
  # Plugins that wish to support both Python 2 and 3 should set it to ">=2.7,<4".
  #
  # Plugins that only support Python 2 will not be accepted into the plugin repository.

  python: ">=3,<4"

---
Octoprint-Detector2 is a detection plugin that runs in locally your browser and emails you if it detects some spaghetti, stringing or blobs on your print. All you need is an email account and a PC.
It is completely free without any monthly subscriptions or one time fees unlike some similar plugins. If it detects an error it sounds the alarm and sends you an email with the latest image snapshot of the print.
##### Used services:
Tensorflow.js for prediction, https://www.smtpjs.com/ to send mail via javascript and Outlook to serve as an SMTP server.

## setup
Install via the [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html) or manually using this URL:

    https://github.com/mikulash/Octoprint-detector2/archive/master.zip

## Configuration

1. To enable email sending it needs to use an SMTP connection. Free and easy to set up is via Outlook. For now, this plugin uses exclusively Outlook so at this moment there is no need for extra set-up. Just creating an email will do it.
<img src="/assets/img/plugins/detector2/outlookPreview.png">
2. In the settings of this plugin enter the username and password for created Outlook account.
<img src="/assets/img/plugins/detector2/settingsPreview.png">
3. This plugin uses snapshots sent by the Timelapse plugin, which is preinstalled with Octoprint. Go to the Timelapse tab and choose snapshot interval. The minimal recommended interval is 10 seconds to let the plugin have enough time to detect errors from an image.
After finishing printing, the timelapse is created, and its deletion is not implemented. I suggest for now deleting these timelapse manually or using another plugin to delete them automatically.
4. Once you start printing you should see the last sent image and result that this detector gets as well with confidence of the result. But if you would
<img src="/assets/img/plugins/detector2/OctoprintPreview.png">
5. If the confidence of the error is greater than 75 %, it starts the alarm and emails you the detected error. Email is sent exactly once to prevent spamming. You can change the confidence threshold in settings.
<img src="/assets/img/plugins/detector2/mailPreview.png">
6. That’s it. You just need to leave the octoprint tab running in the browser and let it work.

## Q&A
#### Email sending stopped working.
To prevent spamming, Outlook has a daily limit for services like this. Open the Outlook account and you should have received a prompt to verify this account. After verification, you should be able to start receiving emails again.

## Supporting the development
It would be greatly appreciated if you would send me your time lapses. Especially the ones with errors not detected. It would help me to improve the model and add new types of errors to detect.
It is super easy. Just upload the generated time-lapse to [Swiss transfer](https://www.swisstransfer.com/en) and send me the generated link to <octoprint.detector2@gmail.com>. Thanks in advance!

## problems or feedback?
If you are having any trouble or have an idea to implement, let me know! This plugin is part of my bachelor thesis so any feedback would be much appreciated. Reach me at the discussion in this plugin [GitHub repository](https://github.com/mikulash/Octoprint-detector2/discussions) or send me your thoughts about this plugin to <octoprint.detector2@gmail.com>.
