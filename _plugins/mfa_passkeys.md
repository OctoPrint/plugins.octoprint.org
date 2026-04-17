---
layout: plugin

id: mfa_passkeys
title: OctoPrint-MFA-Passkeys
description: Seamless biometric and hardware security for OctoPrint. Drop-in WebAuthn support that integrates directly into the native login interface, replacing passwords with Face ID, Touch ID, and security keys.
authors:
- Daedalas1981
license: AGPLv3

date: 2026-04-16

homepage: https://github.com/daedalas1981/Octoprint-MFA-Passkeys
source: https://github.com/daedalas1981/Octoprint-MFA-Passkeys
archive: https://github.com/daedalas1981/OctoPrint-Passkeys/archive/main.zip


follow_dependency_links: false

tags:
- security
- login
- authentication
- mfa
- passkeys
- webauthn
- touch id
- face id
- biometric

compatibility:
  python: ">=3.9,<4"
  octoprint:
  - 1.8.0

---
OctoPrint-Passkeys is a unified authentication plugin that brings modern, passwordless WebAuthn security directly to your printer.

### Powerful Security
* **Native Integration:** Replaces passwords effortlessly on the native login screen.
* **Biometrics:** Authenticate instantly with Windows Hello, Face ID, or Touch ID.
* **Hardware Keys:** YubiKey and U2F compatible.
* **Automated Security:** Contains a built-in automated TLS/HAProxy configuration deployment to instantly generate 10-year Chrome-compliant Secure Subject Alternative Name (SAN) Certificates right on your Pi.
