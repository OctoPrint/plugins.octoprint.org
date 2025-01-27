---
layout: plugin

id: mfa_totp
title: "Two Factor Authentication: TOTP"
description: Plugin to support TOTP based Two Factor Authentication in OctoPrint.
authors:
- Gina Häußge
license: AGPLv3

date: 2025-01-27

homepage: https://github.com/OctoPrint/OctoPrint-MfaTotp
source: https://github.com/OctoPrint/OctoPrint-MfaTotp
archive: https://github.com/OctoPrint/OctoPrint-MfaTotp/archive/main.zip

follow_dependency_links: false

tags:
- 2fa
- mfa
- authentication
- security
- login
- totp

screenshots:
- url: /assets/img/plugins/mfa_totp/screenshot_login.png
  alt: Screenshot of the login workflow, showing an additional prompt added to the login dialog, asking for entering a second factor, with TOTP being an option.
  caption: Second factor dialog in the login workflow, asking for TOTP.
- url: /assets/img/plugins/mfa_totp/screenshot_enrollment.png
  alt: Screenshot of the enrollment dialog, showing a QR Code to scan with an authenticator app and asking for a first token to be entered to confirm enrollment.
  caption: The enrollment dialog

featuredimage: /assets/img/plugins/mfa_totp/screenshot_login.png

compatibility:
  python: ">=3.7,<4"
  octoprint: ">=1.11.0"
---

A plugin to support TOTP based Two Factor Authentication in OctoPrint >= 1.11.0.

Successfully tested with

  - Google Authenticator
  - Aegis

but adheres to the TOTP standard and should work with any related apps.

To enroll your user account, open the "User Settings", then under "2FA: TOTP" click on "Enroll" and follow the instructions.
