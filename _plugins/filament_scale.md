---
layout: plugin

id: filament_scale
title: Filament Scale Enhanced
description: Display filament weight using a HX-711 and a load cell
authors:
- Victor Noordhoek
- Techman83
license: AGPLv3

date: 2021-04-29

homepage: https://github.com/techman83/Filament-Scale-Enhanced
source: https://github.com/techman83/Filament-Scale-Enhanced
archive: https://github.com/techman83/Filament-Scale-Enhanced/releases/latest/download/Filament_Scale_Enhanced.zip


tags:
- raspberry pi
- filament
- gpio

screenshots:
- url: /assets/img/plugins/filament_scale/display.png
  alt: Example of filament remaining weight in UI
  caption: Filament Remaining will be displayed in the UI, with the amount in grams.
- url: /assets/img/plugins/filament_scale/configuration.png
  alt: configuration screen
  caption: Configuration gives you the ability to tare, calibrate using a known weight, and offset the spool/holder weight.

featuredimage: /assets/img/plugins/filament_scale/display.png

compatibility:
  octoprint:
  - 1.5.0
  os:
  - linux
  python: ">=3,<4"

---

This plugin allows connecting an HX711-based load cell to a Raspberry PI, and Octoprint display the current weight of the remaining filament.

You will need an HX711 breakout board and a compatible load cell. You can find these bundled together on Ebay/Aliexpress for roughly $8. Any load cell rated for more than 1kg and less than 50kg should work; I used a 5kg load cell with solid results.

See [here](https://tutorials-raspberrypi.com/digital-raspberry-pi-scale-weight-sensor-hx711/) for instructions on wiring up the load cell

This plugin assumes you connected the data pin to GPIO20, and the clock pin to GPIO21.

You will also need the bracket to connect the load cell to your printer:
- [Regular Spool Holder](https://www.thingiverse.com/thing:3037926)
- [Spannerhands Spool Holder](https://www.thingiverse.com/thing:4834908)