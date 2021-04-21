---
layout: plugin

id: OctoText
title: OctoPrint-Octotext
description: Send text messages on common printer events
authors:
- Stephen Berry
license: AGPLv3

# TODO
date: 2021-03-26

homepage: https://github.com/berrystephenw/OctoText
source: https://github.com/berrystephenw/OctoText
archive: "https://github.com/berrystephenw/OctoText/archive/refs/heads/main.zip"

# TODO
# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

# TODO
tags:
- octotext
- printer status
- email
- text
- notification

# TODO
screenshots:
- url: /assets/img/plugins/OctoText/IMG_6025.PNG
  alt: Webcam integration
  caption: Text message received
- url: /assets/img/plugins/OctoText/test-button.PNG
  alt: Touch UI
  caption: Touch UI
- url: /assets/img/plugins/OctoText/IMG_6143.PNG
  alt: Thumbnail
  caption: Thumbnail text
- url: /assets/img/plugins/OctoText/settings.PNG
  alt: Settings page
  caption: Settings page


# TODO
featuredimage: /assets/img/plugins/OctoText/octotext-email.PNG

# TODO
# You only need the following if your plugin requires specific OctoPrint versions or
# specific operating systems to function - you can safely remove the whole
# "compatibility" block if this is not the case.

compatibility:

  # List of compatible versions
  #
  # A single version number will be interpreted as a minimum version requirement,
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
  - windows
  - macos
  - freebsd

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
# OctoText - Simple, Easy to use, Free text or email notifications
OctoText is a notification plugin that will send you a text or email on configurable printer events. All
you need is an email account! The printer status - along with a webcam snapshot if configured - will
be sent to you either through email or SMS text message.

OctoText is not a service, you will never be charged, and your information is only stored on the device it
is installed on and never transmitted anywhere for any reason.

New in this release:
<li> Thumbnails from PrusaSlicer and Cura are read from newly uploaded files
and sent on printer start notifications.</li>
<li> Pause detection for Prusa "wait for user" messages on filament change events.</li>
<li> SSL protocol has been added for services that don't support TLS.</li>
<li> better message formatting.</li>
<li> the test button on the navigation bar is now an envelope and can be hidden.</li>
<li> bug fixes with webcams that are rotated and flipped.</li>
<li> the printer name is now used in the messages to identify the source of the notification.</li>

## Get optionally notified on the following printer events:
<ul>
   <li> File uploaded</li>
   <li> Print started</li>
   <li> Print finished</li>
   <li> Print failure </li>
   <li> Print cancel </li>
   <li> Print pause </li>
   <li> Print resume </li>
   <li> Periodic progress updates </li>
   <li> Error (unrecoverable)</li>
</ul>

# OctoText plugin installation
If you can set up an email account you can configure OctoText!

1. Install the plugin via the [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
2. Choose an existing email or set up a new email account to be used for the plugin. It is recommended that you use a free
service such as Microsoft's Outlook just for this. Your email host will must allow you to send messages
via an SMTP connection and you will need the port and server address information to set up OctoText.
3. Open the settings tab on Octoprint for the OctoText settings and change the default gateway and port
for your email hosting service. As an example, Outlook uses smtp.office365.com for its gateway and 587 for the port number.
   If your service uses SSL encryption then you will need to check the SSL box and set the port number appropriately
   (usually this is port 465). TLS encryption is the default.
4. Optionally modify the "Message" setting for the test.
5. Change the email address and password settings to match the account you have set up. The password is stored securely on
the OctoPrint server and NEVER transmitted beyond initiating the email connection.
6. For a text message enter the phone number and SMS gateway(1), for email destination enter the username and host.com address
7. If you are going to use the webcam - test the snapshot setting first!
8. Save your settings.
9. Press the test button!

That's it! You will get feedback relatively quickly if the text/email was configured correctly.
The only error case that we cannot detect easily is a bad destination address of the text or email.

Some email services such as gmail and yahoo require an "app" password that you will need to use
in order to login to the account. Check your email provider to see how this is done or go to the
OctoText discussion board for instructions: [FAQ](https://github.com/berrystephenw/OctoText/discussions/1#discussion-3279932)

(1) [https://en.wikipedia.org/wiki/SMS_gateway](https://en.wikipedia.org/wiki/SMS_gateway)

# Problems?
If you are having trouble with your setup, you can post on the discussion board and I'll get to your question as soon as I can.
Please include a copy of the octoprint log from the logging menu of octoprint.
[https://github.com/berrystephenw/OctoText/discussions](https://github.com/berrystephenw/OctoText/discussions)

<img width="128" alt="OctoText" src="/assets/img/plugins/OctoText/iconfinder_13_1236350.png">
