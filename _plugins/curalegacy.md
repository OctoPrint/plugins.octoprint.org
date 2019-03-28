---
layout: plugin

id: curalegacy
title: Cura Legacy
description: Plugin for slicing via the legacy version of CuraEngine from within OctoPrint, unbundled from OctoPrint starting with version 1.3.11
author: Gina Häußge
license: AGPLv3

date: 2019-03-28

homepage: https://github.com/OctoPrint/OctoPrint-CuraLegacy
source: https://github.com/OctoPrint/OctoPrint-CuraLegacy
archive: https://github.com/OctoPrint/OctoPrint-CuraLegacy/archive/master.zip

tags:
- cura
- cura engine
- cura legacy
- slicer
- gcode
- stl

---

The Cura Plugin allows slicing of STL files uploaded to OctoPrint directly via the legacy version of CuraEngine (**up to and including 
version 15.04.x**). It was bundled with OctoPrint up until version 1.3.10.

> 📝 **Note**
>
> Versions of CuraEngine later than 15.04.x have changed their calling parameters in such a way that this 
> plugin is not compatible to it. For this reason, please use only CuraEngine versions up to and including 15.04, 
> as available in the `legacy` branch of the CuraEngine repository on Github.

The plugin offers a settings module that allows configuring the path to the CuraEngine executable to use, as well as 
importing and managing slicing profiles to be used. Please note that the Cura Legacy plugin will use the printer parameters 
you configured within OctoPrint (meaning bed size and extruder count and offsets) for slicing.

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/OctoPrint/OctoPrint-CuraLegacy/archive/master.zip

### First Steps

Before you can slice from within OctoPrint, you’ll need to

  1. Install CuraEngine Legacy
  2. Configure the path to CuraEngine Legacy within OctoPrint
  3. Export a slicing profile from Cura <15.04.x and import it within OctoPrint

OctoPi ships with steps 1 and 2 already done, you only need to supply one or more slicing 
profiles to get going :)

If you are coming from an OctoPrint version prior to 1.3.11 and already had the then still bundled version of this plugin
configured, your configuration & profiles will be migrated.

### Installing CuraEngine Legacy

You'll need a build of `legacy` branch of [CuraEngine](http://github.com/Ultimaker/CuraEngine) in order to be able to 
use the Cura Legacy OctoPrint plugin. You can find the `legacy` branch [here](https://github.com/ultimaker/curaengine/tree/legacy).

#### Compiling for Raspbian

Building on Raspbian Jessie and later is as easy as:

```
sudo apt-get -y install gcc-4.7 g++-4.7
git clone -b legacy https://github.com/Ultimaker/CuraEngine.git
cd CuraEngine
make
```

After this has completed, you’ll find your shiny new build of CuraEngine in the build folder (full path for above 
example: `~/CuraEngine/build/CuraEngine`).

### Using Cura Profiles

The Cura Plugin supports importing your existing profiles for Cura **up to and including Cura 15.04.x**. Newer Cura 
releases (e.g. 15.06 or 2.x) use a different internal format that will not work with the Cura Legacy Plugin.

You can find downloads of Cura 15.04.x for Windows, Mac and Linux on [Ultimaker’s download page](https://ultimaker.com/en/products/cura-software/list).

In order to export a slicing profile from the Cura desktop UI, open it, set up your profile, then click on "File" and 
there on "Save Profile". You can import the .ini-file this creates via the "Import Profile" button in the Cura Settings 
within OctoPrint.

## Configuration

The Cura plugin needs to be configured with the full path to your copy of the CuraEngine executable that it’s supposed 
to use. You can do this either via the Cura plugin settings dialog or by manually configuring the path to the 
executable via ``config.yaml``, example:

``` yaml
plugins:
  curalegacy:
    cura_engine: /path/to/CuraEngine
```
