---
layout: plugin

id: xMattersIntegration
title: xMatters Integration
description: Event notifications using xMatters
author: svv2014
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2019-03-04

homepage: https://github.com/svv2014/OctoPrint-xMatters-integration
source: https://github.com/svv2014/OctoPrint-xMatters-integration
archive: https://github.com/svv2014/OctoPrint-Xmatters-integration/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- xMatters
- events
- notifications
- monitoring

screenshots:
- url: /assets/img/plugins/xMattersIntegration/settings.png
  alt: plugin settings
  caption: plugin settings

featuredimage: /assets/img/plugins/xMattersIntegration/settings.png

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
  - 1.2.0

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

---

The plugin allows OctoPrint to send notifications on events using [xMatters](https://www.xmatters.com/).

## Setup

### xMatter integration setup

* Open your xMatters page
* go to page: Developer > Communication Plans
* Import zip file from [xMatters/OctoPrintIntegration.zip](https://github.com/svv2014/OctoPrint-xMatters-integration/tree/master/xMatters)
    * this will create communication plan for integration
* On communication plan press `Edit` and choose `Integration Builder`
* You should see one configured `Inbound integration`
    * Note if `Inbound integrations` configuration was not imported you may need to create once with `authentication method` equals to `API key`.
* Open this configuration and at the bottom you will find all needed credentials

### Configuration

* Take `API Key`, `Secret`, `Integration URL` from xMatters integration and set it in plugin configuration
    * Note: for `recipients` field use comma separated user id
* Choose events you interested in and enjoy.
