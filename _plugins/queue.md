---
layout: plugin

id: queue
title: OctoPrint-Queue
description: A simple queue setup designed for use by staff at a public library. 
authors: 
- Chris Hennes, Pioneer Library System
license: AGPLv3 

date: 2022-06-06

homepage: https://github.com/chennes/OctoPrint-Queue
source: https://github.com/chennes/OctoPrint-Queue
archive: https://github.com/chennes/OctoPrint-Queue/archive/master.zip

tags:
- ui 
- queue 

screenshots:
- url: /assets/img/plugins/queue/interface.png
  alt: Screenshot of the main user interface of the plugin.
  caption: The queue with a few items in it.
- url: /assets/img/plugins/queue/add.png
  alt: Screenshot of the Add to Queue screen.
  caption: The Add to Queue screen appears when you upload a file, or when you click the "Add" button.
- url: /assets/img/plugins/queue/settings.png
  alt: The settings screen.
  caption: The settings screen showing the default priorities.

featuredimage: /assets/img/plugins/queue/queue.png

compatibility:
  octoprint:
  - 1.3.0
  python: ">=3.0,<4"

---

## A simple print queue

Designed for use at a public library, this plugin allows staff to efficiently manage customer print 
jobs. Its simple interface and setup are easy to learn, and your organization can either implement its own
prioritization scheme or use the one provided with the plugin. It is primarily intended as a staff communication
mechanism, allowing staff to see which job they should start up next, as well as look up completed jobs
to provide information to customers.

# Purely local

This plugin does not use any outside services and has no requirements beyond having an OctoPrint installation.
It does not enforce any restrictions on the input fields, giving staff complete flexibility in how the tool
gets used.

Copyright 2019 [Pioneer Library System](http://pioneerlibrarysystem.org). Some rights reserved, see the [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) for details.
