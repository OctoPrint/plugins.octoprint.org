---
layout: plugin

id: procastinator
title: Procastinator
description: Puts printjobs on hold until a certain time
author: Juergen Pabel
license: AGPLv3

date: 2020-08-21

homepage: https://github.com/juergenpabel/OctoPrint-Procastinator
source: https://github.com/juergenpabel/OctoPrint-Procastinator
archive: https://github.com/juergenpabel/OctoPrint-Procastinator/archive/master.zip

tags:
- schedule
- scheduling
- delay
- pause
- wait
- procastinator

screenshots:
- url: /assets/img/plugins/procastinator/settings.png
  alt: Configuration settings of Procastinator
  caption: Configuration screenshot
- url: /assets/img/plugins/procastinator/dialog.png
  alt: Dialog for selecting time at which to continue the printjob
  caption: Selection screenshot
- url: /assets/img/plugins/procastinator/notice.png
  alt: Notification about putting a printjob on hold
  caption: Notification screenshot

featuredimage: /assets/img/plugins/procastinator/settings.png

compatibility:
  octoprint:
  - 1.4.2

  python: ">=2.7,<4"
      
---

Ever wanted to start a printjob sometime later? Instead of scheduliing a printjob by other means
(cron & curl via API), this plugin allows for a printjob to be started and immediately put on hold
until a given time (or immediately, if so desired). 

This might be useful if you want to start a printjob in the middle of the night (while sleeping)
or even just a little later on (without the risk of forgetting to actually start the printjob later on).

The plugin is configurable as to:
1. a time window during which a printjob is put on hold (like only in the evening)
2. 5 options as for times when to actually start the printjob

If a printjob is started during the configured time window then it is immediately put on hold and the
user is shown a dialog for selecting the time at which the job is to be continued (the first option is
always "NOW", just in case).
