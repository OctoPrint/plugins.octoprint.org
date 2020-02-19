---
layout: plugin

id: Change_Filament
title: Change_Filament
description: Facilitates changing filament (backs out old, loads new)
author: Jim Pingle
license: bsd-3-clause

date: 2019-05-29

homepage: https://github.com/jim-p/Change_Filament
source: https://github.com/jim-p/Change_Filament
archive: https://github.com/jim-p/Change_Filament/archive/master.zip

tags:
- filament

screenshots:
- url: /assets/img/plugins/Change_Filament/cf_buttons.png
  alt: Change Filament Buttons
  caption: Change Filament Buttons
- url: /assets/img/plugins/Change_Filament/cf_settings.png
  alt: Change Filament Settings
  caption: Change Filament Settings

featuredimage: /assets/img/plugins/Change_Filament/cf_buttons.png

---

This plugin makes it simple to change filament.

The plugin mimics the actions taken by the change filament action built into
Marlin. That feature is not available on all printers and also requires using
the control box to use, instead of doing everything in OctoPrint.

Configuration:

* **Unload Length**: Length of filament to reverse extrude when unloading, in mm.
* **Unload Speed**: How fast to unload the filament, in mm/m.
* **Load Length**: Length of filament to extrude when loading, in mm.
* **Load Speed**: How fast to extrude when loading filament, in mm/m.
* **Y Park**: Position on the Y axis where the head will be moved when loading or unloading.
* **X Park**: Position on the X axis where the head will be moved when loading or unloading. Depending on the filament path, may be best set to the midpoint of the X axis.
* **Z Lift Relative**: How high to move the Z axis before unloading, in mm.
* **Park Speed**: How fast to move the head when parking, in mm/m.
