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
archive: https://github.com/jcassel/OctoPrint-Siocontrol/archive/master.zip

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
- url: /assets/img/plugins/SIOControl/SettingsExampleConn.PNG
  alt: SIO Control Serial Connection
  caption: SIO Control Serial Connection 
- url: /assets/img/plugins/SIOControl/SettingsExampleIOConfig.PNG
  alt: SIO Control Example IO Configuration
  caption: SIO Control Example IO Configuration
- url: /assets/img/plugins/SIOControl/SideBarExample.PNG
  alt: SIO Control Side bar example
  caption: SIO Control Side bar example


featuredimage: /assets/img/plugins/SIOControl/SideBarExample.PNG

compatibility:
  python: ">=3,<4"

---
#### Alternative to GPIO if you want to add some electronic/improvements to your printer. Works on Linux and Windows. 

You can now control local IO for Octoprint instances that are not running on a SBC like a Rasberry Pi. You can have GPIO like features if you are running OctoPrint on Windows. 
The interface was modeled after the GPIO Control Plugin, but has some very distinguishing features that set it apart. Adds a sidebar with on/off buttons for controlling of Outputs 
and monitoring of Inputs. Is also a SubPlugin for integration with PSU control, incorporates a physical EStop and a Simple Filament runout as sensor. A true alterative GPIO 
control for users that are not using a Raspberry Pi or other device that has onboard local IO. Does requires a Microcontroller as the IO. 


## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/jcassel/OctoPrint-Siocontrol/archive/master.zip

Use the power of an Arduino compatible micro controller to be the IO. 
The inexpensive ESP8266 and ESP32(Examples available), both can be used as the IO controller. 
This uses the serial connection of the controler when communicating with Octoprint. Wifi version is in the works. 
Firmware is easily adapted to run on many standard Arduino compatible devices. 
See [Example firmware](https://github.com/jcassel/OctoPrint_SIOControl_Firmware) and information on how to make or buy a [compatible IO board](https://www.tindie.com/products/softwaresedge/octoprint-serial-io-kit/). 

## Configuration

Configure the Serial port details. 
- Port path(name)
- Baudrate  
- Sensing/reporting interval

Simple selections for integrations
- Enable and select IO point for PSU Control Sub Plugin.
- Enable and select IO point for physical EStop.
- Enable and select IO point for Filament runout sensor.


Setting up IO in the plugIn is easy:
- Select icon using icon picker
- Name for your device connected to IO point
- Select the IO number to control.
- select if the IO is an INPUT or OUTPUT as well as how it is seen when active, low or high
    - [Type]_HIGH means that device is __on for high state__ and __off for low state__
    - [Type]_LOW means that device is __on for low state__ and __off for high state__
- select if device should be on or off by default e.g. on Octoprint startup.
