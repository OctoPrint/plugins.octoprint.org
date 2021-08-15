---
layout: plugin

id: autobim
title: AutoBim
description: A bed tramming utility for OctoPrint
authors:
- Juri Berlanda
license: AGPLv3

date: 2021-08-15

homepage: https://github.com/j-be/AutoBim
source: https://github.com/j-be/AutoBim
archive: https://github.com/j-be/AutoBim/archive/master.zip

tags:
- abl
- bed level
- bed levelling
- auto bed leveling
- bl-touch
- maintenance

screenshots:
- url: /assets/img/plugins/autobim/ui_1.png
  alt: UI is just a single button
  caption: UI is just a single button
- url: /assets/img/plugins/autobim/settings_1.png
  alt: AutoBim's settings screen
  caption: AutoBim's settings screen

featuredimage: /assets/img/ui_1.png

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

#  octoprint:
#  - 1.2.0

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

#  os:
#  - linux
#  - windows
#  - macos
#  - freebsd

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

AutoBim is a simple bed tramming utility for OctoPrint using ABL. Tramming is the process of making sure your bed is as
parallel to your printer's X axis as possible. Or, put simply:

`Tilted Bed + Tramming = Parallel Bed`

![The UI is just a single button - that's all it needs](/assets/img/plugins/autobim/ui_1.png)


## How does it work

The plugin adds a single button to OctoPrint's navbar, because that's all it needs. When the button is clicked, a
combination of GCodes `G0`, `G28`, `G30`, `M117` and a bit of message parsing is used to create something like
[this (link to YouTube)](https://www.youtube.com/watch?v=iXtuS8pXz94&start=190). Jump to 3:10 if it didn't already.

A (hopefully) complete documentation can be found on the [plugin's Github page](https://github.com/j-be/AutoBim). You'll
also find an extensive troubleshooting section there.

## Disclaimer

The plugin will instruct the printer to move. I work to the best of my knowledge, and I put some effort into reducing
the risk of damage (like highering Z before moving). Yet, **I do not take any responsibility** for damages to you, your
printer, or stuff and people around you.

I have been using the plugin since I started developing it in February 2021, and it always worked fine for me (Ender 3
Pro, SKR Mini E3 v2.0, Antclabs BL-Touch 3.1), but I was extra cautious until I saw the plugin working fine - and I can
only advise you do the same.

## Why the name?

This plugin is meant to help with bed tramming. I am from Vienna, and [trams](https://en.wikipedia.org/wiki/Tram) in
Vienna are called "Bim" (like "bin" as in "trash bin", just with an `m` instead of the `n`).

## Roadmap

I know that there are a couple of rough edges when setting up the plugin - not easy to solve, but thinking about it.
Highest priority is a method to find out if the given points are actually reachable of not (see
[here](https://github.com/j-be/AutoBim#works-fine-on-the-first-or-first-and-second-corner-display-says-ok-moving-to-next-but-nothing-happens)
). If you have suggestions on this, or any other functionality: feel free to open an issue
[here](https://github.com/j-be/AutoBim) and let's discuss stuff.

## Credits

Credit goes to the following projects for being there and letting me look at and copy their code:

* https://github.com/jneilliii/OctoPrint-BedLevelVisualizer
* https://github.com/marian42/octoprint-preheat

Make sure to check them out, and don't forget:

> "Toss a coin to your developers, o valley of plenty, o valley of plenty..."
