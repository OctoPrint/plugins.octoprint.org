---
layout: plugin

id: connectandprint
title: Connect And Print
description: Automatically connect to your printer and start the print job on file upload
authors:
- Max Grallinger

license: AGPLv3

date: 2023-04-26

homepage: https://github.com/Maxinger15/connectandprint
source: https://github.com/Maxinger15/connectandprint
archive: https://raw.githubusercontent.com/Maxinger15/connectandprint/master/connectandprint.py

tags:
- connect
- upload
- file

compatibility:
  python: ">=2.7,<4"

---

With the Connect and Print plugin, you can save time and effort, as there's no need to manually connect to the printer and start the print job after uploading a file. 
Just upload your G-code file and let the plugin handle the rest.

#### Features

- Automatically connects to the printer if not already connected upon file upload.
- Starts printing the uploaded file immediately after a successful connection.
- Implements a 2-minute timeout for printer connection attempts.
- Works with OctoPrint's REST API to streamline the printing process.

#### Note: 
Please ensure that your printer is properly configured and connected to OctoPrint before using this plugin. 
In case of a failed connection attempt, the plugin will log an error message after the 2-minute timeout.

