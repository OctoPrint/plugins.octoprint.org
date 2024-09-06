---
layout: plugin

id: wakeonlan
title: Wake-on-LAN
description: An OctoPrint plugin to send Wake-on-LAN packets.
authors:
- Aridor Joskowich
- Itay Zelikovich
license: AGPLv3

date: 2024-06-07

homepage: https://github.com/Aridor2003/OctoPrint-Wakeonlan
source: https://github.com/Aridor2003/OctoPrint-Wakeonlan
archive: https://github.com/Aridor2003/OctoPrint-Wakeonlan/archive/main.zip

tags:
- network
- utility

screenshots: 
- url:  /assets/img/plugins/wakeonlan/OctoPrint-Navbar.png
- url:  /assets/img/plugins/wakeonlan/OctoPrint-Settings.png

compatibility:
  python: ">=3,<4"
---
# OctoPrint Wake-on-LAN Plugin

An OctoPrint Plugin letting you turn on your computer from anywhere using a raspberry pi.
To use the Plugin just download the zip and install using the plugin Manager and input your Mac address in the settings

**Overview:**

The OctoPrint Wake-on-LAN (WoL) Plugin adds the capability to send Wake-on-LAN packets to designated devices directly from the OctoPrint interface. This is useful for waking up networked devices such as printers or computers before starting a print job.

**Features:**

Send Wake-on-LAN packets with a click of a button.
Configure MAC addresses for target device.
Easy-to-use interface integrated into OctoPrint.

**Prerequisites:**

OctoPrint instance up and running.
Networked device(s) with Wake-on-LAN capability enabled.

After the plugin is installed, OctoPrint will prompt you to restart.
Click Restart Now to apply the changes.

**Configuration:**

Access Plugin Settings:

Go to Settings > Wake-on-LAN.
Add Devices:

Enter the MAC address of the device you want to wake up.

Save Settings:

Click Save to store the device configuration.

**Usage:**

Wake Device:

In the OctoPrint interface, click the wake on lan button in the navbar.

**Monitor Status:**

Ensure the target device powers on and is ready for use.

**Troubleshooting:**

Device Not Waking Up:
Verify the MAC address is correct.
Ensure Wake-on-LAN is enabled on the target device.
Check network configuration and ensure the device is reachable.

**Contributing:**

Contributions are welcome! If you have suggestions, bug reports, or feature requests, please open an issue or submit a pull request on GitHub.

**License:**

This project is licensed under the AGPL3 commercial use License. See the LICENSE file for details.

**Acknowledgments:**

This project was done with tremendous help from [itay zelikovich](https://github.com/zelikit) and [jneilliii](https://github.com/jneilliii) ,Thank you!
