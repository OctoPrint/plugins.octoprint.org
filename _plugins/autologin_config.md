---
layout: plugin

id: autologin_config
title: OctoPrint-AutoLoginConfig
description: Configure AutoLoginLocal from the UI with ease.
author: Charlie Powell
license: AGPLv3

date: 2020-11-15

homepage: https://github.com/OctoPrint/OctoPrint-AutoLoginConfig
source: https://github.com/OctoPrint/OctoPrint-AutoLoginConfig
archive: https://github.com/OctoPrint/OctoPrint-AutoLoginConfig/archive/main.zip

tags:
  - settings
  - configuration
  - autologin
  - autologinlocal
  - accesscontrol

screenshots:
  - url: /assets/img/plugins/autologin_config/instructions.png
    alt: instructions
    caption: Instructions for configuration
  - url: /assets/img/plugins/autologin_config/config.png
    alt: configuration
    caption: Configuration UI

featuredimage: /assets/img/plugins/autologin_config/config.png


compatibility:
  octoprint:
    - 1.4.0

  os:
    - linux
    - windows
    - macos
    - freebsd

  python: ">=2.7,<4"

---

Allows for UI configuration of AutoLoginLocal - an OctoPrint feature that automatically logs in a user from a local network.

<div class="alert alert-block">
    <div class="row-fluid">
        <p>
            <i class="fas fa-exclamation-triangle fa-3x pull-left text-error" style="margin-right: 0.5em;"></i>
            <strong>Do not use this if you cannot trust EVERYONE on your local network.</strong> And I really
            mean everyone. If you ignore this and then someone takes over your OctoPrint instance, installs
            malware on it and makes your printer print an endless stream of benchies, that's on you.
        </p>
    </div>
</div>

**This plugin requires access control to be enabled & set up correctly on OctoPrint 1.4.0 or newer.**

### Problems, bugs, need help? Get in touch:

- on the [OctoPrint Community Forum](https://community.octoprint.org)
- on the [Issue Tracker](https://github.com/OctoPrint/OctoPrint-AutologinLocal/issues)
- on the [OctoPrint discord](https://discord.octoprint.org)

### Support my work with OctoPrint
<div class="row-fluid">
<div class="span3">
<a href="https://www.jetbrains.com/?from=cp2004"><img align="left" width="100" height="100" src="/assets/img/plugins/autologin_config/jetbrains-variant-2.png" alt="JetBrains Logo"></a>
</div>
<div class="span9">
<p>
 Thanks to JetBrains for sponsoring an open source license for their IDEs
</p>
<ul>
<li>
<a href="https://github.com/sponsors/cp2004">You can support my work through Github here!</a>
</li>
</ul>

</div>
</div>

_AutoLoginLocal Configuration by Charlie Powell and [contributors](https://github.com/OctoPrint/OctoPrint-AutoLoginConfig/graphs/contributors)_
