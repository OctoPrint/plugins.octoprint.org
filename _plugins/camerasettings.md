---
layout: plugin

id: camerasettings
title: Camera Settings
description: Interactive camera settings via v4l2-ctl
authors:
- Taylor Talkington
license: AGPLv3

date: 2021-04-29

homepage: https://github.com/The-EG/OctoPrint-CameraSettings
source: https://github.com/The-EG/OctoPrint-CameraSettings
archive: https://github.com/The-EG/OctoPrint-CameraSettings/archive/main.zip


tags:
- camera

screenshots:
- url: /assets/img/plugins/camerasettings/screenshot.png
  alt: Camera Settings Plugin
  caption: Camera Settings Plugin

featuredimage: /assets/img/plugins/camerasettings/screenshot.png

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
  - 1.4.0

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

  python: ">=3,<4"

---

# OctoPrint-CameraSettings

![screenshot](/assets/img/plugins/camerasettings/screenshot.png)

Camera Settings allows a user to interactively change camera settings by running v4l2-ctl on the backend. This method should work for any Linux environment, including OctoPi, as long as the camera is attached to the same device running OctoPrint.

*Note: not compatible with The Spaghetti Detective premium.*

Have a RaspiCam or ArduCam? Look at the [setup guide](https://github.com/The-EG/OctoPrint-CameraSettings/blob/main/docs/setup.md).

See the [GitHub repo](https://github.com/The-EG/OctoPrint-CameraSettings) for the most up to date information, including [setup information](https://github.com/The-EG/OctoPrint-CameraSettings/blob/main/docs/setup.md) and [frequently asked questions](https://github.com/The-EG/OctoPrint-CameraSettings/blob/main/docs/faq.md)

For issues and feature requests, [check the issues on GitHub](https://github.com/The-EG/OctoPrint-CameraSettings/issues) and create one if needed.

