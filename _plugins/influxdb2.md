---
layout: plugin

id: influxdb2
title: InfluxDB2
description: Push Metrics to InfluxDB 2.0+
authors:
  - MoltenBytes
license: MIT

# today's date in format YYYY-MM-DD, e.g.
date: 2023-03-04

homepage: https://gitlab.com/moltenbytes32/octoprint-influxdb2
source: https://gitlab.com/moltenbytes32/octoprint-influxdb2
archive: https://gitlab.com/moltenbytes32/octoprint-influxdb2/-/archive/master/octoprint-influxdb2-master.zip

# Set this if your plugin heavily interacts with any kind of cloud services.
#privacypolicy: your plugin's privacy policy URL

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- events
- data
- log

screenshots:
- url: /assets/img/plugins/influxdb2/thumbnail.jpg
  alt: InfluxDB 2
  caption: Log Data from Octoprint into InfluxDB 2.0+
- url: /assets/img/plugins/influxdb2/settings.png
  alt: The configuration options
  caption: Settings Page
- url: /assets/img/plugins/influxdb2/influx.png
  alt: A graph of print temperatures in InfluxDB
  caption: InfluxDB

featuredimage: /assets/img/plugins/influxdb2/thumbnail.jpg

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

#  octoprint:
#  - 1.3.0

  # List of compatible operating systems
  #
  # Possible values:
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

#  os:
#  - linux
#  - windows
#  - macos
#  - freebsd

  # Compatible Python version
  #
  # Plugins should aim for compatibility for Python 2 and 3 for now, in which case the value should be ">=2.7,<4".
  #
  # Plugins that only wish to support Python 3 should set it to ">=3,<4".
  #
  # If your plugin only supports Python 2 it will no longer be accepted on the plugin repository.
  #
  # Uncomment the appropriate setting

  python: ">=3,<4" # Python 3 only

---

Pushes temperatures and status to an [InfluxDB](https://www.influxdata.com) instance. Similar to `Octoprint-InfluxDB`, however this version is compatible with v2.0+.

## Features:
- Authorization via auth token (only requires write access to one bucket)
- Configurable Temperature and Status measurement names
- Optional machine name tag
- Non-polling, Destructured Logging
  + The implementation registers itself as a native printer callback, and logs every data point from the printer as they are received (using the timestamps from Octoprint where available)
  + The fields this plugin fetches aren't hard-coded. Instead, the event objects are decomposed recursively into fields. If Octoprint (or another plugin) adds additional temperature or state values, they will also get logged in this plugin.
- Can configure and test InfluxDB connection entirely from Octoprint UI

For configuration details, see the homepage. 
