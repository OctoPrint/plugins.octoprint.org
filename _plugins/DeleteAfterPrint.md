---
layout: plugin

id: DeleteAfterPrint
title: OctoPrint-DeleteAfterPrint
description: Deletes automaticaly the Print-Model after succesful print
author: Olli
license: AGPLv3

date: 2018-04-20

homepage: https://github.com/OllisGit/OctoPrint-DeleteAfterPrint
source: https://github.com/OllisGit/OctoPrint-DeleteAfterPrint
archive: https://github.com/OllisGit/OctoPrint-DeleteAfterPrint/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- printer

screenshots:
- url: https://raw.githubusercontent.com/OllisGit/OctoPrint-DeleteAfterPrint/master/screenshots/sidebar.jpg
  alt: sidebar
  caption: sidebar

featuredimage: https://raw.githubusercontent.com/OllisGit/OctoPrint-DeleteAfterPrint/master/screenshots/sidebar.jpg

---

Delete automatically the Print-Model after successful print. If the print fails, the deletion is not executed.

The user can enable automatic deletion for each print by using a checkbox in the sidebar.

For implementation details please visit the [homepage]({{ page.homepage | absolute_url }}).
