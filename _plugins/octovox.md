---
layout: plugin

id: octovox
title: OctoPrint-OctoVox
description: OctoPrint plugin for OctoVox Amazon Alexa Integration
author: John Ruzick
license: AGPLv3

date: 2019-09-11

homepage: https://github.com/johnnyruz/OctoPrint-OctoVox
source: https://github.com/johnnyruz/OctoPrint-OctoVox
archive: https://github.com/johnnyruz/OctoPrint-OctoVox/archive/master.zip

tags:
- octovox
- Amazon Echo
- Alexa
- Printer Status
- Printer Temperature

screenshots:
- url: /assets/img/plugins/octovox/settings.png
  alt: Configure OctoVox
  caption: Configure OctoVox
- url: /assets/img/plugins/octovox/successful_registration.png
  alt: Printer Registration
  caption: Printer Registration
- url: /assets/img/plugins/octovox/alexa_response.png
  alt: Alexa Response
  caption: Alexa Response

featuredimage: /assets/img/plugins/octovox/alexa_response.png
compatibility:
  python: '>=2.7,<4'

attributes:
- cloud

---

The OctoVox plugin for OctoPrint sends limited printer information to a database for access via Amazon Echo devices.
The problem with other Alexa solutions is that they require exposing access to your Octoprint server over the public internet
as well as require providing the external service with your Octoprint API key.

The OctoVox plugin eliminates that security risk by publishing only small informational status updates about your printer
that can then be retrieved by the Octovox Amazon Alexa Skill. This plugin and Alexa Skill do not allow any manipulation or
control over your printer, it is entirely read-only and secured via user accounts.

## OctoVox Plugin Installation and Configuration

Installation is super easy. There is no need to change your router configuration, do
port forwarding or open holes in your firewall.

1. Download and install this plugin from the OctoPrint Plugin Repository or Github URL
2. Open the Settings tab of the OctoPrint-OctoVox Plugin
3. Enter a desired name for your printer
4. Click the ***Request Printer Registration*** button
5. You will be redirected to the OctoVox Login Page. If you do not yet have an account, click "Sign-Up" and enter a valid
email address and create a password. You will have to verify your email address and then you will be directed to a page
that will provide a unique key for your printer.
6. Enter that unique key in the box for Step 3 on the OctoVox Settings Page.
7. Click the ***Verify Registration*** button to make sure things were configured correctly.
8. After the info is verified, click Save.

## Alexa Setup

1. Use the Alexa companion mobile app or website to find and enable the Octovox Skill.
2. Once enabled, click on Settings and select Link Account.
3. Enter the Username and Password created in step 4 of the Plugin Configuration.
4. You can now ask Alexa for your printer status by saying "Alexa, ask my 3-D print server for my printer status"

## Setup Walkthrough

{% include youtube.html vid="4LcqT-awm-0" preview="'/assets/img/plugins/octovox/octovox_video_title.png'" %}

## Privacy

This plugin uses two external services to function. A user management and registration portal, and an API/Database to store printer information.
Upon successful configuration, your OctoPrint server will occasionally publish updates to the service via the API. These updates are secured
using your unique printer API key. This is NOT your OctoPrint API key! At no point will you need to provide your OctoPrint API key or Url, and
you do not need to expose your server to the public.

Currently, the OctoVox service stores the following information which can be retrieved by Alexa:
- Registration Email Address
- Printer Name
- Encrypted Printer Key Value
- Printer Status (Offline, Operational, Printing, etc.)
- Hot End Temperature
- Bed Temperature
- Current Job Completion Percentage
- Current Job Z-height
- Current Filename
- Previous Job Duration
- Previous Job Result (Completed, Cancelled, Failed, etc.)

Printers that have not updated their status in 10 days will automatically be removed from the database and will have to be re-registered
