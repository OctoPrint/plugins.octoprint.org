---
layout: plugin

id: filetypes
title: Filetypes
description: Lets you control which file extensions are allowed to be uploaded thru the 'Upload' and 'Upload to SD' buttons.
authors:
 - Kestin Goforth
 - thelongrunsmoke
license: AGPLv3

date: 2017-08-23

homepage: https://github.com/kforth/OctoPrint-Filetypes
source: https://github.com/kforth/OctoPrint-Filetypes
archive: https://github.com/kforth/OctoPrint-Filetypes/archive/master.zip

follow_dependency_links: false

tags:
- stl
- gcode
- ui
- upload
- files

screenshots:
- url: /assets/img/plugins/filetypes/settings.png
  alt: Filetype Settings Page
  caption: Filetype Settings Page

featuredimage: /assets/img/plugins/filetypes/settings.png

---

This plugin lets you control which file extensions are allowed to be uploaded thru the 'Upload' and 'Upload to SD' buttons.

If you have installed plugins that support additional file types, add them to the list so that you can easily upload them.

**Note:** The server will still reject uploads for unsupported file types. Only add extensions that are supported by your installed plugins.

## Configuration

Go to 'Settings' -> 'Filetypes Plugin' and configure the extensions you need.

![Settings](/assets/img/plugins/filetypes/settings.png)
