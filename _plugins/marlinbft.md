---
layout: plugin

id: marlinbft
title: OctoPrint-MarlinBft
description: Upload files using Marlin Binary File Transfer Mark II
author: Charles Willis
license: MIT

date: 2020-07-26

homepage: https://github.com/charleswillis3/OctoPrint-MarlinBft
source: https://github.com/charleswillis3/OctoPrint-MarlinBft
archive: https://github.com/charleswillis3/OctoPrint-MarlinBft/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
follow_dependency_links: false

tags:
- marlin
- file
- transfer
- firmware.bin
- binary

screenshots:
- url: /assets/img/plugins/marlinbft/marlinbft-feature.png
  alt: marlin binary file transfer dialog
  caption: The transfer dialog
- url: /assets/img/plugins/marlinbft/marlinbft-navbar.png
  alt: marlin binary file transfer navbar button
  caption: THe navbar button

featuredimage: /assets/img/plugins/marlinbft/marlinbft-feature.png

compatibility:

  octoprint:
  - 1.4.0

  os:
  - linux
  - windows
  - macos
  - freebsd

  python: ">=2.7,<4"

up_for_adoption: https://github.com/CharlesWillis3/OctoPrint-MarlinBft/issues/18
---

**DEVELOPER NOTE**

There are several major issues currently reported:

* Installation on systems with python 3 but not python 2
* Failed transfers on latest Marlin bugfix-2.0.x

I am not currently in a position to maintain this plugin, or the library that handles
the actual binary transfer. If you're interested, please respond to the pinned issues on
the repositories:

* https://github.com/CharlesWillis3/OctoPrint-MarlinBft
* https://github.com/CharlesWillis3/marlin-binary-protocol

---

This will transfer a file to a printer using Marlin firmware's experimental binary file transfer protocol.

* Marlin bugfix-2.0.x
* Enable BINARY_FILE_TRANSFER feature in Configuration_adv.h
* Ensure capability reporting is enabled

General use:

1. Connect to the printer
1. Click the Marlin BFT icon in the Nav bar to open the transfer dialog
1. Click the gear icon to adjust the timeouts in the settings dialog
1. Back in the transfer dialog, adjust the transfer settings "Reconnect" and "Send GCode after Transfer"
1. Click the upload button to select the file. Transfer will start immediately
1. The dialog will close automatically when the transfer and post-transfer phases are complete

Updating firmware on BigTreeTech boards:

1. In settings:
    1. Ensure `bin` is in the "Accept file extensions" list
    1. Set "Wait before reconnect" to a reasonable value like 12000 (12 seconds)
1. In the transfer dialog:
    1. Enable "Send GCode after transfer" and set the Gcode to `M997` (marlin reset)
    1. Click the upload button and select the `firmware.bin` file. Click OK.
    1. After the M997 reset, reconnect the printer (or enable "Reconnect after transfer")

It's also possible to transfer a file using the http api.

1. Upload the file to OctoPrint using the [`files` api](https://docs.octoprint.org/en/master/api/files.html#upload-file-or-create-folder)
1. Disconnect the printer using the [`connection` api](https://docs.octoprint.org/en/master/api/connection.html#issue-a-connection-command)
1. POST a json object to the `marlinbft` api:
```
POST /api/plugin/marlinbft
Content-Type: application/json
X-Api-Key: abcdef...

Body:
{
  "command":                    "start_transfer",
  "handler_type":               "api"
  "port":                       "/dev/ttyACM0",
  "baudrate":                   250000,
  "local_path":                 "marlinbft/firmware.bin",
  "comm_timeout_ms":            1000,
  "wait_after_connect_ms":      3000,
  "post_transfer_gcode_enable": true,
  "post_transfer_gcode":        ["M997"]
}
```

The properties:

`command`
: required. must be the value "start_transfer"

`api`
: required. must be the value "api"

`port`
: required. the serial port the printer is connected on

`baudrate`
: required.

`local_path`
: required. the local path on the server to the uploaded file

`comm_timeout_ms`
: optional, settings override, int. the communication timeout

`wait_after_connect_ms`
: optional, settings override, int. if provided, how long to wait after establishing connection

`post_transfer_gcode_enable`
: optional, settings override, bool. whether to send gcode after the transfer completes

`post_transfer_gcode`
: optional, settings override, string array. the gcode to send

For settings override properties, if no value is provided the current configuration will be used.
