---
layout: plugin

id: AutoLogout
title: AutoLogout
description: Plugin starts a countdown timer after login and if the timer is count to zero, the user is automatically logged out.

author: Olli
license: AGPLv3

date: 2019-10-03

homepage: https://github.com/OllisGit/OctoPrint-AutoLogout
source: https://github.com/OllisGit/OctoPrint-AutoLogout
archive: https://github.com/OllisGit/OctoPrint-AutoLogout/releases/latest/download/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- printer

compatibility:
  python: ">=2.7,<4"
  octoprint:
  - 1.3.10
  - 1.4.0

screenshots:
- url: https://github.com/OllisGit/Octoprint-AutoLogout/raw/master/screenshots/plugin-navbar.png
  alt: Plugin Navbar
  caption: Plugin Navbar
- url: https://github.com/OllisGit/Octoprint-AutoLogout/raw/master/screenshots/plugin-settings.png
  alt: Plugin Settings
  caption: Plugin Settings
featuredimage: https://github.com/OllisGit/Octoprint-AutoLogout/raw/master/screenshots/plugin-settings.png

---

Plugin starts a countdown timer after login and if the timer is count to zero, the user is automatically logged out.
The timer is restarted each time a user clicks on "something" like a tab-change.

For implementation details please visit the [homepage]({{ page.homepage | absolute_url }}).

#### Support my Efforts

This plugin, as well as my [other plugins](https://github.com/OllisGit/) were developed in my spare time.
If you like it, I would be thankful about a cup of coffee :)

[![More coffee, more code](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=6SW5R6ZUKLB5E&source=url)
