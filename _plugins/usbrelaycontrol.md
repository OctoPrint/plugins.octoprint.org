---
layout: plugin

id: usbrelaycontrol
title: USB Relay Control
description: Control USB relays from within OctoPrint
authors:
- A. S. Budden
license: AGPL

date: 2022-03-01

homepage: https://github.com/abudden/OctoPrint-USBRelayControl
source: https://github.com/abudden/OctoPrint-USBRelayControl
archive: https://github.com/abudden/OctoPrint-USBRelayControl/archive/master.zip

tags:
- control
- usb
- relay

screenshots:
- url: /assets/img/plugins/usbrelaycontrol/sidebar.png
  alt: USB Relay Control sidebar
  caption: USB Relay Control sidebar
- url: /assets/img/plugins/usbrelaycontrol/settings.png
  alt: USB Relay Control settings
  caption: USB Relay Control settings

featuredimage: /assets/img/plugins/usbrelaycontrol/sidebar.png

compatibility:
  octoprint:
  - 1.5.0
  os:
  - linux
  python: ">=3,<4" # Python 3 only

---

Useful if you want to add some lights or other devices to your printer but you don't want to mess about with GPIO pins.

I use it with the a custom Prusa Einsy case that has space for a raspberry pi but not much more - a USB relay can be connected to the USB port and it controls the lights around the printer.  It should work with any HID-controlled USB relay, such as [this one](https://www.ebay.co.uk/itm/253297488368).  There are some photos of two compatible relays on the [github page for one of the projects that this code was based upon](https://github.com/jaketeater/Very-Simple-USB-Relay).

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/abudden/OctoPrint-USBRelayControl/archive/master.zip

See the [homepage](https://github.com/abudden/OctoPrint-USBRelayControl) for more tips that might be helpful if you have problems installing it (you may need to install some extra development packages with `apt-get` if your raspberry pi doesn't have them already).

## Device Privileges

You'll also need to make sure that the USB relay can be controlled without root privileges.  For example, edit `/etc/udev/rules.d/99-usbrelay.rules` and add this line:

```
SUBSYSTEM=="usb", ATTR{idVendor}=="16c0", ATTR{idProduct}=="05df", MODE="777"
```

Then restart your raspberry pi.

The vendor ID and product ID (which you'll also need in the octoprint configuration) can be found using the `lsusb` command.  The easiest way to do this is to run `lsusb`, then plug your device in, then run `lsusb` again.  One new line should have appeared and this will contain the `ID XXXX:YYYY` where `XXXX` is the vendor ID and `YYYY` is the product ID.

## Configuration

Just add correct relay configuration:

- select icon using icon picker (or typing manually) for better identification
- type name for your device connected to the relay
- Add the vendor ID and product ID for the relay (defaults to 16C0 and 05DF)
- Add the relay number on the board
- select whether relay active corresponds with turning your device on or off
    - _active high_ means that device is **on when the relay is activated**
    - _active low_ means that device is **off when the relay is activated**
- select if device should be on or off by default eg. after startup

Note that there's very little in the way of error checking, so if you put incorrect values into any of the fields, it'll probably break something.

## Credits

This plugin was created as a combination of two other excellent projects:

* [OctoPrint GPIO Control](https://github.com/catgiggle/OctoPrint-GpioControl) by Damian Wójcik, which provided the framework and most of the octoprint interaction.
* [Very Simple USB Relay](https://github.com/jaketeater/Very-Simple-USB-Relay) by jaketeater, which provided the code required to drive the relays.

