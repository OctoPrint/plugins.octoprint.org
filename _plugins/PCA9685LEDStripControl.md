---
layout: plugin

id: PCA9685LEDStripControl
title: PCA9685 LED Strip Control
description: OctoPrint plugin for controling RGB LED Strips via PCA9685 over I2C
author: Ozgun Ayaz
license: Apache

date: 2019-05-07

homepage: https://github.com/ozgunawesome/OctoPrint-PCA9685LEDStripControl
source: https://github.com/ozgunawesome/OctoPrint-PCA9685LEDStripControl
archive: https://github.com/ozgunawesome/OctoPrint-PCA9685LEDStripControl/archive/master.zip

follow_dependency_links: false

screenshots:
- url: /assets/img/plugins/PCA9685LEDStripControl/Screenshot.png
  alt: Configuration Screen
  caption: Configure GPIOs
- url: /assets/img/plugins/PCA9685LEDStripControl/PCA9685_dev_board.jpg
  alt: PCA9685 breakout board
  caption: PCA9685 is an I2C integrated circuit that can provide 12-bit hardware PWM on 16 channels

featuredimage: /assets/img/plugins/PCA9685LEDStripControl/PCA9685_dev_board.jpg

tags:
- pca9685
- i2c
- hardware pwm
- pwm
- raspberry pi
- led
- rgb
- gcode

compatibility:

  octoprint:
  - 1.3.1

  os:
  - linux
  - freebsd

---

# OctoPrint-PCA9685LEDStripControl

OctoPrint plugin that intercepts M150 GCode commands and controls LEDs connected to PCA9685 over I2C.

![PCA9685 dev board](/assets/img/plugins/PCA9685LEDStripControl/PCA9685_dev_board.jpg)

Implements the M150 command syntax from the latest Marlin.

        M150: Set Status LED Color - Use R-U-B for R-G-B Optional (W)
        M150 R255       ; Turn LED red
        M150 R255 U127  ; Turn LED orange (PWM only)
        M150            ; Turn LED off
        M150 R U B      ; Turn LED white
        M150 W          ; Turn LED white if using RGBW strips (optional)

## Setup

1. Connect PCA9685 (address 0x40) and enable I2C in configuration

    	sudo raspi-config

2. Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    	https://github.com/ozgunawesome/OctoPrint-PCA9685LEDStripControl/archive/master.zip

3. Restart OctoPrint

## Configuration

Configure the PCA9685 pins via the OctoPrint settings UI.
