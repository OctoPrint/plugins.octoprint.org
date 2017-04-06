---
layout: plugin

id: m33fio
title: M33 Fio
description: Allows viewing uploaded models, using a Micro 3D printer, modifying a slicer profile and model before slicing, uploading OBJs and other 3D file formats, hosting a webcam stream, and much more
author: donovan6000
license: GPLv3

date: 2016-10-25

homepage: https://github.com/donovan6000/M33-Fio
source: https://github.com/donovan6000/M33-Fio
archive: https://github.com/donovan6000/M33-Fio/archive/master.zip

follow_dependency_links: false

tags:
- m33 fio
- micro 3d
- helper
- ui

screenshots:
- url: /assets/img/plugins/m33fio/model_editor.png
  alt: Model Editor
  caption: Model Editor
- url: /assets/img/plugins/m33fio/profile_editor.png
  alt: Profile Editor
  caption: Profile Editor
- url: /assets/img/plugins/m33fio/model_viewer.png
  alt: Model Viewer
  caption: Model Viewer

featuredimage: /assets/img/plugins/m33fio/model_editor.png

disabled: There's a compatibility issue between this plugin and OctoPrint 1.3.2+ (current stable). A fixed version by a third party is available but requires
    manual installation steps. Please [refer to this ticket on the plugin's bug tracker](https://github.com/donovan6000/M33-Fio/issues/216)
    on how to install the fixed version. Until the fix has been merged into the plugin by the maintainer and a new version
    has been released, this plugin will stay disabled on the repository.

---

M33 Fio extends OctoPrint's capabilities to include the following features:

- Adds a model viewer tab to OctoPrint's interface where any uploaded model can be viewed
- Allows importing OBJ, M3D, AMF, VRML, COLLADA, and 3MF files into OctoPrint
- Updates OctoPrint's list of available serial ports in real time
- Includes an OctoPrint instance manager that can create and terminate OctoPrint instances which allows easily running multiple printers on the same host
- Adds support for the Micro 3D printer
- Wraps groups of buttons in OctoPrint's controls tab into sections that can be collapsed and expanded
- Capable of hosting a webcam stream and configuring OctoPrint to use it
- Disables the hosts sleep functionality when printing
- Includes a slicer profile editor that allows customizing everything in the selected slicer profile before slicing
- Includes a model editor that allows modifying a model before slicing and can perform operations like moving, rotating, scaling, cutting, merging, cloning, and importing other models into the scene
