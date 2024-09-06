---
layout: plugin

id: Spoolman
title: octoprint-spoolman
description: Plugin integrating OctoPrint with Spoolman, a universal filament spools inventory manager.
authors:
- Michał Dziekoński (mdziekon)
license: AGPLv3

date: 2024-04-27

homepage: https://github.com/mdziekon/octoprint-spoolman
source: https://github.com/mdziekon/octoprint-spoolman
archive: https://github.com/mdziekon/octoprint-spoolman/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
follow_dependency_links: false

tags:
- filament
- spools
- spoolman

screenshots:
- url: /assets/img/plugins/Spoolman/showcase__selected_spools.png
  alt: Showcase - Selected spools list
  caption: Selected spools list
- url: /assets/img/plugins/Spoolman/showcase__spools_list.png
  alt: Showcase - Spools' list
  caption: Spools' list
- url: /assets/img/plugins/Spoolman/showcase__spoolman_setup.png
  alt: Showcase - Spoolman's setup
  caption: Spoolman's setup

# TODO
featuredimage: /assets/img/plugins/Spoolman/showcase__selected_spools.png

compatibility:
  octoprint:
  - 1.9.0

  python: ">=3,<4"

---

# octoprint-spoolman

An OctoPrint plugin integrating with [Spoolman](https://github.com/Donkie/Spoolman/), a universal filament spools inventory manager.

## Features

- [x] Basic Spoolman integration
    - [x] Connect to configured Spoolman instance
    - [x] Display available spools
        - By default, `archived` spools are not presented for selection
    - [x] Select & deselect spools for specified tools / extruders
    - [x] Commit spools usage to Spoolman
- [ ] Spools filtering
- [ ] Check spools before starting a print
    - [ ] Ask the user if the selected spool is correct
    - [ ] Warn when no spool is selected
    - [ ] Warn when selected spool does not have enough material
    - [ ] Warn when wrong spool material has been selected (PrusaSlicer / OrcaSlicer gcodes)

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/mdziekon/octoprint-spoolman/archive/master.zip

After installing the plugin, you have to set it up, by:
- Providing your Spoolman's instance address.
    - This should be either hostname or IP address (whatever works in your network) followed by the port (eg. 7912). Ideally, you should use secure connection (HTTPS) to connect your Octoprint with Spoolman.
    - Remember, your Spoolman's instance **has to be reachable in your local network**, otherwise the plugin won't work.
    - For reference, see [Screenshots - Spoolman's setup](#spoolmans-setup)

## Screenshots

### Selected spools list

![Showcase - Selected spools list](/assets/img/plugins/Spoolman/showcase__selected_spools.png)

### Spools' list

![Showcase - Spools' list](/assets/img/plugins/Spoolman/showcase__spools_list.png)

### Spoolman's setup

![Showcase - Spoolman's setup](/assets/img/plugins/Spoolman/showcase__spoolman_setup.png)
