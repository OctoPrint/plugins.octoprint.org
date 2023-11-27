---
layout: plugin

id: PrintJobHistory
title: PrintJobHistory
description: The OctoPrint-Plugin stores all print-job information of a print in a database.
authors:
    - dojohnso
    - Olli
license: AGPLv3

date: 2023-11-27

homepage: https://github.com/dojohnso/OctoPrint-PrintJobHistory
source: https://github.com/dojohnso/OctoPrint-PrintJobHistory
archive: https://github.com/dojohnso/OctoPrint-PrintJobHistory/releases/latest/download/main.zip

follow_dependency_links: false

tags:
- printer
- history

compatibility:
  python: ">=2.7,<4"
  octoprint:
  - 1.3.10
  - 1.4.0

screenshots:
- url: /assets/img/plugins/PrintJobHistory/plugin-tab.png
  alt: History Overview Tab
  caption: History Overview Tab

- url: /assets/img/plugins/PrintJobHistory/editPrintJob-dialog.png
  alt: Edit of a Print Job Item
  caption: Edit of a Print Job Item

- url: /assets/img/plugins/PrintJobHistory/editPrintJob-changeStatus-dialog.png
  alt: Change print status
  caption: Change print status

- url: /assets/img/plugins/PrintJobHistory/statistics-dialog.png
  alt: Print Statistics
  caption: Print Statistics


- url: /assets/img/plugins/PrintJobHistory/plugin-settings.png
  alt: Plugin Settings
  caption: Plugin Settings

- url: /assets/img/plugins/PrintJobHistory/missingPlugins-dialog.png
  alt: Optional Plugin Dependencies
  caption: Optional Plugin Dependencies


featuredimage: /assets/img/plugins/PrintJobHistory/editPrintJob-dialog.png

abandoned: https://github.com/OctoPrint/plugins.octoprint.org/issues/1222

---

Print Job History-Plugin collects a lot of attributes from OctoPrint itself, like **Filename, Start/End-Time, Status, Username, Slicer-Settings** and many more. But it also grabs information from other plugins: **Thumbnail, Layer-Information, Filament usage**...

For a full overview of the latest feature set and planed features, please visit the [Git Hub Homepage]({{ page.homepage | absolute_url }})


## *NOTE: this plugin has been abandoned by the original creator and adopted here by a new maintainer*

**This plugin is under new management** and will focus on critical bug fixes to start. Please bear with me as I get acclimated to this new plugin. If you would like to support these new efforts, please consider buying me a coffee or two. Thank you!

<a href="https://www.buymeacoffee.com/djohnson.tech" target="_blank"><img src="https://djohnson.tech/images/white-button.png" width=300 /></a>
