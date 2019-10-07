---
layout: plugin

id: metadatapreprocessor
title: MetadataPreprocessor
description: Speed up gcode analysis
author: Sven Lohrmann
license: AGPLv3
date: 2019-10-03
homepage: https://github.com/malnvenshorn/OctoPrint-MetadataPreprocessor
source: https://github.com/malnvenshorn/OctoPrint-MetadataPreprocessor
archive: https://github.com/malnvenshorn/OctoPrint-MetadataPreprocessor/archive/master.zip
tags:
- gcode
- metadata
---

This OctoPrint plugin uses a generated metadata comment in the gcode file to speed up the analyzing process on systems with limited resources like the Raspberry PI.

As an example: Analyzing a 7MB gcode file on my Raspberry PI B+ took ~17min. With included metadata only 2s while generating the metadata itself took additional 8s on my laptop.

## How it works

The separate analysis script uses OctoPrint's gcode interpreter to analyze the given gcode file. After the analysis has finished the metadata is written to the beginning of the file.

If the gcode is uploaded the plugin stops the gcode analysis started by OctoPrint and looks whether the file contains such metadata or not. If metadata is found it will be added to the _.metadata.yaml_ and the _METADATA&#95;ANALYSIS&#95;FINISHED_ event will be fired. Otherwise the file will be analyzed by OctoPrint as usual by adding it to the analysis queue again.

## Installation of the analysis script

This is a guide how I set it up for [Slic3r](https://slic3r.org/). If your slicer doesn't support post-processing scripts you need to run the analysis manually.

```
$ mkdir -p ~/.Slic3r/utils/gcode_metadata
$ cd ~/.Slic3r/utils/gcode_metadata
$ wget https://github.com/malnvenshorn/OctoPrint-MetadataPreprocessor/archive/master.zip
$ unzip -j master.zip "OctoPrint-MetadataPreprocessor-master/analysis/*" -d .
$ virtualenv -p /usr/bin/python2 venv
$ source venv/bin/activate
$ python setup.py install
```

### Usage

```
$ analysis --help
Usage: analysis [OPTIONS] PATH

Options:
  --speed-x FLOAT
  --speed-y FLOAT
  --offset <FLOAT FLOAT>...
  --max-t INTEGER
  --g90-extruder
  --help                     Show this message and exit.
```

### Slic3r

You can easily integrate the analysis script in your workflow with slic3r. Simply add the absolute path of the script under the [post-processing scripts](http://manual.slic3r.org/advanced/post-processing) option.

![Screenshot](https://raw.githubusercontent.com/malnvenshorn/OctoPrint-MetadataPreprocessor/master/docs/slic3r.png)

If you want to supply arguments, e.g. `--g90-extruder`, you need to write a wrapper script. I placed mine under `~/.Slic3r/utils/gcode_metadata/generate_octoprint_metadata.sh`, see screenshot above.

```
#!/bin/bash

~/.Slic3r/utils/gcode_metadata/venv/bin/analysis --g90-extruder "$@"
```
