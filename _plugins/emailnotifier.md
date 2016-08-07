---
layout: plugin
    
id: emailnotifier
title: Email Notifier
description: Recieve email notifications when OctoPrint jobs are complete.
author: Jim DeVona
license: AGPLv3
    
# today's date in format YYYY-MM-DD, e.g.
date: 2015-09-23
    
homepage: https://github.com/anoved/OctoPrint-EmailNotifier
source: https://github.com/anoved/OctoPrint-EmailNotifier
archive: https://github.com/anoved/OctoPrint-EmailNotifier/archive/master.zip
    
# set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
follow_dependency_links: false
    
tags:
- notification

screenshots: 
- url: /assets/img/plugins/emailnotifier/emailnotifier.png
  alt: Settings dialog and email notification screenshot
  caption: Configure notification recipient, outgoing SMTP account, and message format in the settings dialog.

featuredimage: /assets/img/plugins/emailnotifier/emailnotifier.png

compatibility:
  # list of compatible versions, for example 1.2.0. If left empty no specific version requirement will be assumed
  octoprint:
  - 1.2.4

---
    
Receive email notifications when OctoPrint jobs are complete.
