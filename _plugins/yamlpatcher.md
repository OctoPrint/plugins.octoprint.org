---
layout: plugin

id: yamlpatcher
title: Yamlpatcher
description: Allows patching up config.yaml through the web interface
author: Gina Häußge
license: AGPLv3

date: 2015-07-09

homepage: https://github.com/OctoPrint/OctoPrint-Yamlpatcher
source: https://github.com/OctoPrint/OctoPrint-Yamlpatcher
archive: https://github.com/OctoPrint/OctoPrint-Yamlpatcher/archive/master.zip

tags:
- admin
- config

screenshots:
- url: http://i.imgur.com/Xs1xGHu.png
  alt: Screenshot
- url: http://i.imgur.com/0Av9NB5.gif
  alt: JSON patch string
  caption: Supports JSON based change sets
- url: http://i.imgur.com/VzHeRHn.gif
  alt: YAML patch string
  caption: Supports merging YAML dictionaries

featuredimage: http://i.imgur.com/Xs1xGHu.png
---

The OctoPrint Yamlpatcher Plugin allows patching OctoPrint's [`config.yaml`](http://docs.octoprint.org/en/master/configuration/config_yaml.html)
through a new dialog within OctoPrint's settings, using easily shareable
patch strings.

This allows applying configuration changes that are not easily achievable through
the UI even for users who don't feel comfortable manually editing a YAML
configuration file. And for those that do feel comfortable with YAML, it is
also is a very fast way to make quick adjustments to configuration settings for
which no UI inputs exist, e.g. [development settings](http://docs.octoprint.org/en/master/configuration/config_yaml.html#development-settings).

Before allowing to apply the patch string, the plugin will present the user
with a preview of the changes that will take place, visualizing both added
and removed entries within `config.yaml`.

> ⚠ **Note**
>
> This plugin primarily targets developers, not endusers. It is not actively maintained since it does what is needed from it for regular OctoPrint development activities. If someone wants to make it more versatile and add more or fix existing functionality, feel free to get in touch about adoption on the [community forums](https://community.octoprint.org/c/plugins) about it.

## Usage

Paste a valid patch string into the input field below, then hit the "Preview" button. Make sure the changes look like they should (if a screenshot of a preview was provided along side the patch string, compare!). If they do, hit "Apply". Then restart your server.

## Patch format

See [the documentation](https://github.com/OctoPrint/OctoPrint-Yamlpatcher#patch-format).
