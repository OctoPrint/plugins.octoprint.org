---
layout: plugin

id: FileDescription
title: FileDescription
description: Adds description and searchable tags entries to all files in the file manager.
authors:
- Larsjuhw
license: AGPLv3

date: 2023-08-23

homepage: https://github.com/larsjuhw/Octoprint-FileDescription
source: https://github.com/larsjuhw/Octoprint-FileDescription
archive: https://github.com/larsjuhw/Octoprint-FileDescription/archive/master.zip

tags:
- descriptions
- tags
- file manager
- info

screenshots:
- url: /assets/img/plugins/FileDescription/featured.png
  alt: File view
  caption: View of file in file manager
- url: /assets/img/plugins/FileDescription/expanded.png
  alt: Expanded file view
  caption: View of expanded file in file manager
- url: /assets/img/plugins/FileDescription/featured.png
  alt: Edit view
  caption: View of the edit panel

featuredimage: /assets/img/plugins/FileDescription/featured.png

compatibility:
  python: ">=3,<4"

---

# Octoprint-FileDescription

Adds a description and tags entry to all gcode files in the file manager. Tags are also searchable.

When you click on the arrow button on a file to expand the info, an edit button should appear next to the file's "load and print" button. Clicking the button opens a panel where you can set the description and/or tag of the file. After setting a description or tag, you can also click on the "Description: " and "Tags: " fields to open the edit panel. **Setting empty strings will delete the entries.**

This plugin is fully compatible with my other plugin [ExtraFileInfo](https://github.com/larsjuhw/OctoPrint-ExtraFileInfo).