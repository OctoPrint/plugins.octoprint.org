---
layout: plugin
id: siocontrol
title: SIO Control
description: Serial IO Control, an alterative way to control locally connected IO. Works on any device(PC,SBC) and OS that supports OctoPrint including Windows.  

authors: 
- jcassel
license: AGPLv3
date: 2023-05-02
homepage: https://github.com/jcassel/OctoPrint-Siocontrol
source: https://github.com/jcassel/OctoPrint-Siocontrol
archive: https://github.com/jcassel/OctoPrint-Siocontrol/archive/main.zip

tags:
- sio
- gpio
- rpio
- pc
- linux
- gpiostatus
- pin
- pins
- atx
- control
- io
- power
- estop
- psu
- psucontrol
- psucontrol subplugin
- gpiocontrol
- relay
- enclosure
- button
- filament
- usb
- serial
- rs232
- led
- windows


screenshots:
- url: /assets/img/plugins/siocontrol/SettingsExampleConn.PNG
  alt: SIO Control Serial Connection
  caption: SIO Control Serial Connection 
- url: /assets/img/plugins/siocontrol/SettingsExampleIOConfig.PNG
  alt: SIO Control Example IO Configuration
  caption: SIO Control Example IO Configuration
- url: /assets/img/plugins/siocontrol/SideBarExample.PNG
  alt: SIO Control Side bar example
  caption: SIO Control Side bar example


featuredimage: /assets/img/plugins/siocontrol/SideBarExample.PNG

compatibility:
  python: ">=3,<4"

---
#### Alternative to GPIO if you want to add some electronic/improvements to your printer. Works on Linux and Windows. 

Control relays and lights or add buttons at your printer to help with setup and Filament changes. Automate your enclosure. Get GPIO features if you are running OctoPrint on Windows or a Linux mini PC. It adds a sidebar with on/off buttons for controlling of outputs/relays and monitoring of Input states. It also can place buttons and indicators in the top navigation bar for quick access. It can be configured to act as a Sub-PlugIn for integration with PSU control PlugIn, incorporates a physical E-Stop configuration and a Filament runout as sensor configuration. The alterative when native GPIO is not available on your OctoPrint  device. This solution uses an inexpensive microcontroller as the IO. Just plug it into your USB Port and use its IO to control your devices.

Find Sub Plugins: <https://plugins.octoprint.org/by_tag/#tag-siocontrol-subplugin>

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/jcassel/OctoPrint-Siocontrol/archive/main.zip

Use the power of an Arduino compatible micro controller to be the IO. 
The inexpensive ESP8266 and ESP32(Examples available) or even an Arduino Nanno, all can be used as the IO controller. 
The firmware makes use of the serial UART connection of the micro controller when communicating with Octoprint. 


There are lots of options for the Firmware. Its easily adapted to run on many standard Arduino compatible devices or you can buy an already setup [controler kit](https://www.tindie.com/stores/softwaresedge/) at a reasonable price. 


See [Example firmware](https://github.com/jcassel/OctoPrint_SIOControl_Firmware) and information on how to make or buy a [compatible IO board](https://www.tindie.com/products/softwaresedge/octoprint-serial-io-kit/). and other OctoPrint adjacent products.


## Configuration

Configure the Serial port details. 
- Port path(name)
- Baudrate  
- Sensing/reporting interval


Simple built in Integrations
- Enable and select IO point as a switching and sensing; PSU Control Sub Plugin.
- Enable and select IO point for physical EStop using (M112) GCode when triggered.
- Enable and select IO point for Filament runout sensor. Causes a pause to be sent to the printer.


Setting up IO in the plugIn is easy:
- Select icon using icon picker
- Name for your device connected to IO point
- Select the IO number to control.
- select if the IO is an INPUT or OUTPUT as well as how it is seen when active, low or high
    - [Type]_HIGH means that device is __on for high state__ and __off for low state__
    - [Type]_LOW means that device is __on for low state__ and __off for high state__
- select if device should be on or off by default e.g. on Octoprint startup.

## Do more with a Sub Plugin:

Use the [SIO Reacton sub plugin](https://plugins.octoprint.org/plugins/SIOReaction/) and create "Reactions" to take place when SIO configured IO points change state.
