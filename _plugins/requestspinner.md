---
layout: plugin

id: requestspinner
title: RequestSpinner
description: Shows a little spinner in the web frontend when background requests are active
author: Gina Häußge
license: AGPLv3

date: 2015-06-21

homepage: https://github.com/OctoPrint/OctoPrint-RequestSpinner
source: https://github.com/OctoPrint/OctoPrint-RequestSpinner
archive: https://github.com/OctoPrint/OctoPrint-RequestSpinner/archive/master.zip

follow_dependency_links: false

tags:
- ui
- ajax

screenshots:
- url: /assets/img/plugins/requestspinner/requestspinner.png
  alt: The request spinner in action
  caption: The request spinner in action

featuredimage: /assets/img/plugins/requestspinner/requestspinner.png

compatibility:
  python: ">=2.7,<4"
---

The Request Spinner Plugin puts a little spinner icon in the lower left corner of the OctoPrint web interface whenever
there are active background requests via AJAX in progress. That provides a bit of feedback about how long your actions
take to get processed by your server and gives you some more indication if stuff is actually happening or not.
