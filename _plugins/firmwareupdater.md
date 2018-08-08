---
layout: plugin

id: firmwareupdater
title: Firmware Updater
description: Flash pre-compiled firmware images to the printer from OctoPrint.
author: Gina Häußge and Ben Lye, based on work by Nicanor Romero Venier
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2018-01-15

homepage: https://github.com/OctoPrint/OctoPrint-FirmwareUpdater
source: https://github.com/OctoPrint/OctoPrint-FirmwareUpdater
archive: https://github.com/OctoPrint/OctoPrint-FirmwareUpdater/archive/master.zip

tags:
- firmware
- avrdude
- firmware updater

screenshots:
- url: /assets/img/plugins/firmwareupdater/firmwareupdater.png
  alt: Firmware Updater
  caption: Firmware Updater
- url: /assets/img/plugins/firmwareupdater/firmwareupdater-settings.png
  alt: Firmware Updater Settings
  caption: Firmware Updater Settings

featuredimage: /assets/img/plugins/firmwareupdater/firmwareupdater.png

---
<style>
.tablelines table, .tablelines td, .tablelines th {
        border: 1px solid gray;
				 padding: 5px;
        }
</style>

Works with boards with `Atmega1280`, `Atmega1284p`, and `Atmega2560` MCUs using `arduino`, `usbasp`, or `wiring` programmers.

More boards can be added, please request additions via a [Github issue](https://github.com/OctoPrint/OctoPrint-FirmwareUpdater/issues).

### Requirements
AVRDUDE needs to be installed on the server where OctoPrint is running.

#### Raspberry Pi
```
sudo apt-get update
sudo apt-get install avrdude
```

### Configuration
The plugin needs the following configuration:

* Path to avrdude (typically `/usr/bin/avrdude`)
* Path to avrdude configuration file (optional)
* AVR MCU Type
* AVR Programmer Type

Typical MCU/programmer combinations are:

| AVR MCU | Programmer |
| --- | --- |
| Atmega1284p | arduino |
| Atmega2560 | wiring |
{: .tablelines}
