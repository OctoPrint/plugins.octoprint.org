---
layout: plugin

id: nexus_ai
title: Octoprint Nexus AI
description: Nexus AI was oriniall developed for Sentry Pro to detect print failure. Fiberpunk  make it free and accessible to as many 3D printer users as possible. 
author: Fiberpunk team
#- first author name
#- second autor name
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2022-09-29

homepage: https://fiber-punk.com/pages/nexusai
source: https://github.com/fiberpunk1/OctoPrint-Nexus-AI
archive: https://github.com/fiberpunk1/OctoPrint-Nexus-AI/archive/master.zip
privacypolicy: https://fiber-punk.com/pages/privacy-policy

# Set this if your plugin heavily interacts with any kind of cloud services.
#privacypolicy: your plugin's privacy policy URL

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- monitoring
- free
- email


featuredimage: /assets/img/plugins/nexus_ai/featured.png

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

  os:
  - linux
  - windows
  - macos
  - freebsd

  # Compatible Python version
  #
  # Plugins should aim for compatibility for Python 2 and 3 for now, in which case the value should be ">=2.7,<4".
  #
  # Plugins that only wish to support Python 3 should set it to ">=3,<4".
  #
  # If your plugin only supports Python 2 it will no longer be accepted on the plugin repository.
  #
  # Uncomment the appropriate setting

  #python: ">=2.7,<3" # Python 2 & 3
  python: ">=3.6,<4" # Python 3 only

attributes:
- cloud
- commercial
- free-tier

---
<br />

<p class="lead"> <a href="https://fiber-punk.com/pages/nexusai">Nexus AI</a>, The easiest and free way to implement print failure detection</p>

<br />

## what is Nexus AI?

Nexus AI is a server program that can detect 3D printing failures by recognizing patterns in pictures uploaded by clients. 
Key features: 
- Free,All features are free recognizing print issues
- Easy to deploy.  Simply install. Just install a program on your old computer.
- Safer than using a cloud service
- Low hardware requirement, it can run on machines without needing the latest high-power CPU, nor it requires GPU to function. 
- Optimized. It can utilize Intel’s Openvino for machine vision model acceleration to boost performance. 

**Free to use!**

Step by step turitol, please refer this doc: [Nexus AI Turitol](https://docs.google.com/presentation/d/17tiNloVBMYsRRr2qnuSZILDhk4pYkyATVpw55qvDMcA/edit?usp=sharing)

## Easy deploy and install

**1. Start service**

When the red status label turn to green, means service started.
![img](/assets/img/plugins/nexus_ai/Octoscreen-3.jpg)

**2. Set plugin**

![img](/assets/img/plugins/nexus_ai/Octoscreen-4.jpg)


All done!