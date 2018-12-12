---
layout: plugin

id: MyMiniFactory
title: OctoPrint-MyMiniFactory
description: Plugin to integrate with MyMiniFactory and enable click and print functionality.
author: jneilliii
license: AGPLv3

date: 2018-12-11

homepage: https://github.com/jneilliii/OctoPrint-MyMiniFactory
source: https://github.com/jneilliii/OctoPrint-MyMiniFactory
archive: https://github.com/jneilliii/OctoPrint-MyMiniFactory/archive/master.zip

tags:
- MyMiniFactory
- Remote

screenshots:
- url: /assets/img/plugins/MyMiniFactory/myminifactory_tab.png
  alt: MyMiniFactory Tab
  caption: MyMiniFactory

featuredimage: /assets/img/plugins/MyMiniFactory/myminifactory_logo_128.png

compatibility:
  octoprint:
  - 1.2.0

---

# OctoPrint-MyMiniFactory

This plugin adds the ability to register your OctoPrint based printer to the MyMiniFactory&reg; __Click & Print__ service. All slicing is completed on the MyMiniFactory&reg; servers and is optimized for printing PLA to specific supported printers. E-Mail MyMiniFactory&reg; [here](mailto:info@myminifactory.com) if you would like to get your printer added.

## Install

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/jneilliii/OctoPrint-MyMiniFactory/archive/master.zip

## Setup

Once installed go into OctoPrint Settings > MyMiniFactory&reg; and select your connected printer's manufacturer and model and click the register button.  A QR code will be generated that can be scanned in the MyMiniFactory&reg; mobile application ([Android](https://play.google.com/store/apps/details?id=com.myminifactoryapps&hl=en) or [iOS](https://itunes.apple.com/us/app/myminifactory/id1313773617?mt=8)) and associates with your account. Once registration is complete the printer should be listed in the mobile application as either Free, Busy, or Offline based on the current state.

## Printing

From within the mobile application find a verified __Click & Print__ model and click the Print button.  Select your newly added printer from the top of the list under `Your Printers` and press the `Print This Object` button.  The file will be sliced and added to your printer queue; find the newly added file and press the `Print` button. The gcode file will be downloaded to OctoPrint and start printing.

## Disclaimer

This plugin adds a tab to the OctoPrint interface that loads the MyMiniFactory&reg; website within an iframe with consent from My Mini Factory Ltd. It was built by [jneilliii](https://github.com/jneilliii) using the [MyMiniFactory API](https://www.myminifactory.com/pages/for-developers).

The MyMiniFactory&reg; name, logo, website, and the __Click & Print__ service is copyright, trademark, and owned by My Mini Factory Ltd., see their [Terms and Conditions](https://www.myminifactory.com/pages/terms-and-conditions) for additional information regarding the use of their website and service(s).

By using this plugin you release jneilliii of any liability related to the use of the MyMiniFactory&reg; service.

OctoPrint-MyMiniFactory uses the [Eclipse Paho Python Client](https://www.eclipse.org/paho/clients/python/) under the hood, which is dual-licensed and used here under the terms of the [EDL v1.0 (BSD)](https://www.eclipse.org/org/documents/edl-v10.php).

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

### Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip if you find this plugin helpful.

[![paypal](/assets/img/plugins/MyMiniFactory/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>

