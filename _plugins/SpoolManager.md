---
layout: plugin

id: SpoolManager
title: SpoolManager
description: The OctoPrint-Plugin manages all spool informations and stores it in a database.
authors:
    - WildRikku
    - dojohnso
    - Olli
license: AGPLv3

date: 2020-08-23

homepage: https://github.com/WildRikku/OctoPrint-SpoolManager
source: https://github.com/WildRikku/OctoPrint-SpoolManager
archive: https://github.com/WildRikku/OctoPrint-SpoolManager/releases/latest/download/main.zip

follow_dependency_links: false

tags:
- printer
- spool
- filament

compatibility:
  python: ">=2.7,<4"
  octoprint:
  - 1.3.10
  - 1.4.0

screenshots:
- url: /assets/img/plugins/SpoolManager/listSpools-tab.png
  alt: List tab of all spools
  caption: List of all Spools

- url: /assets/img/plugins/SpoolManager/selectSpool-sidebar.png
  alt: Spool selection
  caption: Spool selection

- url: /assets/img/plugins/SpoolManager/editSpool-dialog.png
  alt: Edit spool
  caption: Edit spool

featuredimage: /assets/img/plugins/SpoolManager/editSpool-dialog.png

---

SpoolManager offers the possibility to save many properties of a Spool in a database. Like: material, color, weight, length, purchase-info, last/first-usage, ...

For a full overview of the latest feature set and planed features, please visit the [Git Hub Homepage]({{ page.homepage | absolute_url }})
