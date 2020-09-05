---
layout: plugin

id: auth_ldap
title: Auth LDAP
description: LDAP authentication for OctoPrint
author: Gillaume Gill, Seth Battis, Paul K. Stelis
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2020-09-05

homepage: https://github.com/battis/OctoPrint-LDAP
source: https://github.com/battis/OctoPrint-LDAP
archive: https://github.com/battis/OctoPrint-LDAP/archive/v1.1.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- ldap
- authentication
- login
- user
- group

screenshots:
- url: /assets/img/plugins/auth_ldap/screenshot_settings.png
  alt: Auth LDAP settings
  caption: Fully configurable LDAP server connection and local caching
- url: /assets/img/plugins/auth_ldap/screenshot_access_control_syncing.png
  alt: Synced LDAP groups in Access Control settings
  caption: Capable of syncing LDAP organizational units to local OctoPrint groups
- url: /assets/img/plugins/auth_ldap/screenshot_synced_group_privileges.png
  alt: Editing a synced LDAP group's access privileges
  caption: LDAP organizational units can be used to set group permissions locally

featuredimage: /assets/img/plugins/auth_ldap/screenshot_access_control_syncing.png

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
  # If your plugin only supports Python 2 (worst case, not recommended for newly developed plugins since Python 2
  # is EOL), leave at ">=2.7,<3"
      
  python: ">=3,<4"
      
---

Authenticate to your OctoPrint instances via LDAP, giving all users authenticated, individually configurable access to the 3D printers.

Configurable local caching allows you to use LDAP organizational units as access control groups for OctoPrint, giving differentiated levels of access to groups of users, or allowing you to give custom permissions to individual users.