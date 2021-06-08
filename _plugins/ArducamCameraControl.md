---
layout: plugin

id: ArducamCameraControl
title: ArducamCameraControl
description: Plugin to control Arducam motorized and ptz camera
authors:
- Arducam
license: AGPLv3

# TODO
date: 2021-06-07

homepage: https://github.com/arducam/ArducamCameraControl
source: https://github.com/arducam/ArducamCameraControl
archive: https://github.com/arducam/ArducamCameraControl/archive/master.zip

# TODO
# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

# TODO
tags:
- Arducam
- Camera


# TODO
screenshots:
- url: /assets/img/plugins/ArducamCameraControl/ArducamCameraControl.png
  # alt: alt-text of a screenshot
  # caption: caption of a screenshot
# - url: url of another screenshot, /assets/img/...
#   alt: alt-text of another screenshot
#   caption: caption of another screenshot
# - ...

# TODO
featuredimage: /assets/img/plugins/ArducamCameraControl/ArducamCameraControl.png

# TODO
# You only need the following if your plugin requires specific OctoPrint versions or
# specific operating systems to function - you can safely remove the whole
# "compatibility" block if this is not the case.

compatibility:

  # List of compatible versions
  #
  # A single version number will be interpretated as a minimum version requirement,
  # e.g. "1.3.1" will show the plugin as compatible to OctoPrint versions 1.3.1 and up.
  # More sophisticated version requirements can be modelled too by using PEP440
  # compatible version specifiers.
  #
  # You can also remove the whole "octoprint" block. Removing it will default to all
  # OctoPrint versions being supported.

  octoprint:
  - 1.2.0

  # List of compatible operating systems
  #
  # Valid values:
  #
  # - windows
  # - linux
  # - macos
  # - freebsd
  #
  # There are also two OS groups defined that get expanded on usage:
  #
  # - posix: linux, macos and freebsd
  # - nix: linux and freebsd
  #
  # You can also remove the whole "os" block. Removing it will default to all
  # operating systems being supported.

  os:
  - linux

  # Compatible Python version
  #
  # Plugins should aim for compatibility for Python 2 and 3 for now, in which case the value should be ">=2.7,<4".
  #
  # Plugins that only wish to support Python 3 should set it to ">=3,<4".
  #
  # If your plugin only supports Python 2 (worst case, not recommended for newly developed plugins since Python 2
  # is EOL), leave at ">=2.7,<3" - be aware that your plugin will not be allowed to register on the
  # plugin repository if it only support Python 2.

  python: ">=2.7,<4"

---

# ArducamCameraControl  

A plugin to control your arducam camera with motorized and ptz camera on octoprint.  
![screenshot](/assets/img/plugins/ArducamCameraControl/ArducamCameraControl.png)
## Install  
Please follow the manufacturer's instructions:
#### I2C 
This plugin uses I2C to communicate with the camera.  That is not enabled by default.  The ArduCamFocus plugin will not function until
you enable I2C.
  ssh to your octopi and enter this commands (this only needs to be done once):
```bash
if ! grep -Fxq "^#ArduCamFocus$" /boot/config.txt; then
sudo cat << end_of_file > /boot/config.txt
#ArduCamFocus
dtparam=i2c_vc=on
dtparam=i2c_arm=on
end_of_file
fi
```
After executing the above command, the file /boot/config.txt should now have the commands to enable I2C.  In addition, you have to enable the I2C
kernel module using raspi-config.  Again, ssh to your octopi, and then enter this command:
```bash
sudo raspi-config
```

1. select "5 Interfacing Options"
2. select "P5 I2C"
3. raspi-config will ask, "Would you like the ARM I2C interface to be enabled?"
4. select "Yes"
5. you should see, "The ARM I2C interface is enabled"
6. select "Finish"

#### Smbus
Install smbus
```shell  
pip install smbus
```


#### Plugin  
Install plugin
http://plugins.octoprint.org/plugin/ArducamCameraControl/

After you reboot, the camera should become operational in OctoPrint
## Settings

This plugin has no configurable settings.





 

