---
layout: plugin

id: ArducamCameraControl
title: ArducamCameraControl
description: Plugin to control Arducam motorized and ptz camera
authors:
- Arducam
license: AGPLv3

date: 2021-06-18

homepage: https://github.com/arducam/ArducamCameraControl
source: https://github.com/arducam/ArducamCameraControl
archive: https://github.com/arducam/ArducamCameraControl/archive/master.zip

tags:
- Arducam
- Camera

featuredimage: /assets/img/plugins/ArducamCameraControl/ArducamCameraControl.png

compatibility:
  octoprint:
  - 1.4.0
  os:
  - linux
  python: ">=2.7,<4"

---

## Arducam Camera Control

A plugin to control your arducam camera with motorized and ptz camera on octoprint.

![screenshot](/assets/img/plugins/ArducamCameraControl/ArducamCameraControl.png)

## Hardware Install

Please follow the manufacturer's instructions.

#### I2C 
This plugin uses I2C to communicate with the camera.  That is not enabled by default.  The Arducam Camera Control plugin will not function until
you enable I2C.

SSH to your octopi, install system dependencies and enable i2c:
```bash
sudo apt update
sudo apt install i2c-tools
sudo nano /boot/config.txt
```
at the very end of the file add the following:
```bash
#ArduCamFocus
dtparam=i2c_vc=on
dtparam=i2c_arm=on
```
press ctrl+s to save and ctrl+x to exit


Enable the I2C kernel module using raspi-config:
```bash
sudo raspi-config
```

1. select "3 Interfacing Options"
2. select "P5 I2C"
3. raspi-config will ask, "Would you like the ARM I2C interface to be enabled?"
4. select "Yes"
5. you should see, "The ARM I2C interface is enabled"
6. select "Finish"


#### Plugin  
Install plugin from Plugin Manager > Get More and search for ArducamCameraControl.

After you restart, the camera should be controllable from OctoPrint's Control tab. 






 

