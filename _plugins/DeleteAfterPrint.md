---
layout: plugin

id: DeleteAfterPrint
title: DeleteMoveAfterPrint
description: Deletes/Move automaticaly the Print-Model
author: Olli
license: AGPLv3

date: 2018-04-20

homepage: https://github.com/OllisGit/OctoPrint-DeleteAfterPrint
source: https://github.com/OllisGit/OctoPrint-DeleteAfterPrint
archive: https://github.com/OllisGit/OctoPrint-DeleteAfterPrint/releases/latest/download/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- printer

screenshots:
- url: https://raw.githubusercontent.com/OllisGit/OctoPrint-DeleteAfterPrint/master/screenshots/sidebar.jpg
  alt: sidebar
  caption: sidebar
- url: https://raw.githubusercontent.com/OllisGit/OctoPrint-DeleteAfterPrint/master/screenshots/plugin-settings.jpg
  alt: plugin-settings
  caption: plugin-settings
  
featuredimage: https://raw.githubusercontent.com/OllisGit/OctoPrint-DeleteAfterPrint/master/screenshots/sidebar.jpg

compatibility:
  python: ">=2.7,<4"

---

Delete/Move automatically the Print-Model: 
* after successful print. If the print fails, the deletion is not executed!
* after predefined days

#### Support my Efforts

This plugin, as well as my [other plugins](https://github.com/OllisGit/) were developed in my spare time.
If you like it, I would be thankful about a cup of coffee :) 

[![More coffee, more code](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=6SW5R6ZUKLB5E&source=url)

## Details
The user can enable automatic deletion/movement after each print by using a checkbox in the sidebar.

If you want to delete/move files after a couple of days, use the Plugin-Settings. Deletion/Movement is done while opening OctoPrint.

For implementation details, please visit the [homepage]({{ page.homepage | absolute_url }}).
