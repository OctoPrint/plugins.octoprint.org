---
layout: plugin

id: powerfailure
title: OctoPrint-PowerFailure
description: This plugin attempts to recover a print after a power failure or printer disconnect.
authors:
- Pablo Ventura
- Paul Paukstelis
license: AGPLv3

date: 2023-01-23

homepage: https://github.com/pablogventura/OctoPrint-PowerFailure
source: https://github.com/pablogventura/OctoPrint-PowerFailure
archive: https://github.com/pablogventura/OctoPrint-PowerFailure/archive/master.zip

tags:
- power
- disconnect
- recovery

#featuredimage: url of a featured image for your plugin, /assets/img/...

# You only need the following if your plugin requires specific OctoPrint versions or
# specific operating systems to function - you can safely remove the whole
# "compatibility" block if this is not the case.

compatibility:

  octoprint:
  - 1.3.0
  os:
  - linux
  - windows
  - macos
  - freebsd

  python: ">=3,<4" # Python 3 only
---
OctoPrint-PowerFailure attempts to recover a print after a power failure or printer disconnect. It is intended as a last resort and does not replace the use of proper power backup and appropriate communication setups. Recovered parts are certain to show small defects, but this may be acceptable in some cases. **RESULTS WILL VARY AND NO GUARANTEES ARE MADE**
