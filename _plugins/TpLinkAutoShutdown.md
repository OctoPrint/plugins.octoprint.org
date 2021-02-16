---
layout: plugin

id: TpLinkAutoShutdown

title: OctoPrint-Tplinkautoshutdown

description:
This plugin is designed to help you integrate your IoT TP-Link Kasa wireless plug into OctoPrint. The basis of the plug-in is to enable you to automatically switch-off your 3D printer once a print has successfully completed.

authors:
- James D. McCannon

license: AGPLv3

date: 2020-02-15

homepage: https://github.com/jamesmccannon02/OctoPrint-Tplinkautoshutdown

source: https://github.com/jamesmccannon02/OctoPrint-Tplinkautoshutdown

archive: https://github.com/jamesmccannon02/OctoPrint-Tplinkautoshutdown/archive/master.zip

follow_dependency_links: false

tags:
- Printer
- Kasa
- Tp-Link
- Auto_Shutdown

compatibility:
  octoprint:
  - 1.5.3

  os:
  - linux
  - windows
  - macos

  python: ">=3,<4"

---

This plugin is designed to help you integrate your IoT TP-Link Kasa wireless plug into OctoPrint. The basis of the plug-in is to enable you to automatically switch-off your 3D printer
once a print has successfully completed.

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/jamesmccannon02/OctoPrint-Tplinkautoshutdown/archive/master.zip

#### Simple installation

Installation can be achieved through two options. The first and simplest option is to use the plugin manager within OctoPrint and search for TpLinkHandler. Then upon installation all you need to do is re-start you device and the plugin will be installed and ready for use.

#### Manual installation

To manually install your plugin, follow these steps:

1.	Open settings,
2.	Click on ‘Plugin Manager’
3.	Now click ‘Get More’
4.	A window will then pop-up. There will be a text box with ‘Enter URL…’. Paste the URL from above. This URL must be the URL from this README.md file not the URL of the webpage within your browser.
5.	Finally click install
6.	Restart OctoPrint and you are ready.

#### Connection to a device
Currently, the plugin is always activated. This means that whilst activated within the Plugin Manager, the 3D printer will turn off automatically upon completion of a 3D Print. Additionally, there will also be a ‘Turn on’ and a “Turn off” button within the navigation bar at the top of the OctoPrint page. This allows for manual control of the device.

#### Features coming soon
1.	Within the near future, you will be able to control how your printer reacts once a print has finished, paused, started etc.
2.	Additionally, an automatic search for your IoT device will be added. This will save you as the user searching for your Smart Plug.
3.	Integration will be added to control other Kasa devices including smart lights, bulbs and power strips.
4.	Any other recommendations are welcomed.

To connect your Kasa device, you will need to click the settings icon within the navigation bar and then down the right-hand side of your screen (under ‘plugins’) you can select the ‘TpLinkHandler’. Then type the IP address of your smart-plug and click save. Now you are ready.

## How the plugin works
Currently, the plugin is always activated. This means that whilst activated within the Plugin Manager, the 3D printer will turn off automatically upon completion of a 3D Print.

## compatibility

Although, this plugin may work with a number of other Kasa devices, this plugin has been designed to definitively work with the following devices.

#### Smart Plugs:

* HS100
* HS103
* HS105
* HS107
* HS110

## Authors

- James D. McCannon - https://mccannon.me.uk

## Contributions
Contributions (be it adding missing features, fixing bugs or improving documentation) are more than welcome, feel free to submit pull requests!
