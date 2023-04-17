---
layout: plugin

id: arc_welder
title: Arc Welder
description: Anti-Stutter and GCode Compression.  Replaces G0/G1 with G2/G3 where possible.
author: Brad Hochgesang
license: AGPL-3.0

# today's date in format YYYY-MM-DD, e.g.
date: 2020-10-24

homepage: https://github.com/FormerLurker/ArcWelderPlugin
source: https://github.com/FormerLurker/ArcWelderPlugin
archive: https://github.com/FormerLurker/ArcWelderPlugin/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- gcode
- compression
- arc
- preprocessing
- g2
- g3
- stutter

#screenshots:
#- url: url of a screenshot, /assets/img/...
#  alt: alt-text of a screenshot
#  caption: caption of a screenshot
#- url: url of another screenshot, /assets/img/...
#  alt: alt-text of another screenshot
#  caption: caption of another screenshot
#- ...

featuredimage: /assets/img/plugins/arc_welder/tab_full.jpg

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
  # Possible values:
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
  - freebsd
  # Not supported Yet
  # - macos

  # Compatible Python version
  #
  # Plugins should aim for compatibility for Python 2 and 3 for now, in which case the value should be ">=2.7,<4".
  #
  # Plugins that only wish to support Python 3 should set it to ">=3,<4".
  #
  # If your plugin only supports Python 2 (worst case, not recommended for newly developed plugins since Python 2
  # is EOL), leave at ">=2.7,<3"

  python: ">=2.7,<4"

---
# Arc Welder: Anti Stutter and GCode Compression
<figure style="text-align:center">
    {% include youtube.html vid="18uYYXecH5g" %}
    <figcaption>
        <a href="https://www.youtube.com/channel/UCevttltfkZ76jwqfV1vrRbQ">Makers Mashup</a> Review of Arc Welder
    </figcaption>
</figure>

<figure style="text-align:center">
    <img src="{{site.url}}/assets/img/plugins/arc_welder/tab_mini.jpg" alt="The Arc Welder Tab" title="The Arc Welder Tab."/>
    <figcaption>
        <a href="https://github.com/FormerLurker/ArcWelderPlugin/wiki/">
            <i>The Arc Welder Tab</i>
        </a>
    </figcaption>
</figure>
## How To Use Arc Welder
Please read the [readme file](https://github.com/FormerLurker/ArcWelderPlugin/#arc-welder-anti-stutter) in the Github Repository for installation and usage instructions.  I am planning to add a complete wiki for the plugin in the near future and will link to that here when it is complete.

Please note that if you are using Python 3, you may need to install the *python3-dev* package before *Arc Welder* will install. This is detailed in the [prerequisites section of the readme file](https://github.com/FormerLurker/ArcWelderPlugin/#prerequisites) linked to above.

## Support *Arc Welder* Development
Please consider supporting my work by becoming a [patron](https://www.patreon.com/join/FormerLurker), a [Github Sponsor](https://github.com/sponsors/FormerLurker), or by sending me beer money via [PayPal](https://paypal.me/formerlurker).  Almost all of the donations go towards offsetting the cost of development, which is substantial. Plus, it always makes my day!  If you cannot afford to leave a tip or just don't want to, that is fine too! *Arc Welder* is [free and open source](https://raw.githubusercontent.com/FormerLurker/ArcWelderPlugin/master/LICENSE) after all.

## What *Arc Welder* Does
*Arc Welder* attempts to replace G0/G1 (linear move) GCodes with G2/G3 (arc move) GCodes.  This can substantially compress many GCode files and may reduce stuttering caused by sending many tiny movements in rapid succession over a slower serial connection.  Here is an example of the before and after of a single layer of a cylinder with archimedean infill produced by PrusaSlicer:
<figure style="text-align:center">
    <a href="{{site.url}}/assets/img/plugins/arc_welder/gcode_cylinder_before_after.png" target="_blank">
        <img src="{{site.url}}/assets/img/plugins/arc_welder/gcode_cylinder_before_after.png" alt="An ncviewer visualization of GCode produced by PrusaSlicer." title="An ncviewer visualization of GCode produced by PrusaSlicer.  Click to view the full sized image."/>
    </a>
    <figcaption>
        <i>Before:  GCode generated by PrusaSlicer.  After: GCode processed by ArcWelder.  Visualized with <a href="https://ncviewer.com/">ncviewer</a>. <a href="{{site.url}}/assets/img/plugins/arc_welder/gcode_cylinder_before_after.png" target="_blank">View the Full Sized Image</a>.</i>
    </figcaption>
</figure>
Each dot in the image above represents the start or endpoint of an extrusion.  You can see that the *After* GCode above has far fewer moves. The processed GCode is 76.1% smaller with 96.4% fewer extrusion/retraction commands than the original file.  Detailed statistics are created and stored for each GCode file processed:
<figure style="text-align:center">
    <img src="{{site.url}}/assets/img/plugins/arc_welder/gcode_cylinder_test_statistics.jpg" alt="Postprocessing Statistics"/>
    <figcaption>
        <i>Statistics of the arc-welded file, showing a substantial reduction in file size and extrusion/retraction moves.</i>
    </figcaption>
</figure>

The results above are not typical since the source file is almost entirely circular.  A better real world example, the first layer of the famous [3DBenchy](http://www.3dbenchy.com/), sliced with PrusaSlicer using archimedean infill is shown below:

<figure style="text-align:center">
    <a href="{{site.url}}/assets/img/plugins/arc_welder/3dbenchy_before_after.png" target="_blank">
        <img src="{{site.url}}/assets/img/plugins/arc_welder/3dbenchy_before_after.png" alt="A Before and After of 3D Benchy." title="A Before and After of 3D Benchy.  Click to view the full sized image."/>
    </a>
    <figcaption>
        <i>Before:  GCode generated by PrusaSlicer.  After: GCode processed by Arc Welder.  Visualized with <a href="https://ncviewer.com/">ncviewer</a>.  <a href="{{site.url}}/assets/img/plugins/arc_welder/3dbenchy_before_after.png" target="_blank">View the Full Sized Image</a>.</i>
    </figcaption>
</figure>

The result is a GCode file that is 56.2% smaller (2.3 compression ratio) with 75.0% fewer extrusion/retraction commands.  In this case, *Arc Welder* shows a massive decrease in small extrusion moves between 0.01mm and 1mm in length:
```
   Min          Max   Source  Target  Change
--------------------------------------------
  0.000mm to   0.002mm     0      0     0.0%
  0.002mm to   0.005mm     0      0     0.0%
  0.005mm to   0.010mm     0      0     0.0%
  0.010mm to   0.050mm     7      1   -85.7%
  0.050mm to   0.100mm    29      6   -79.3%
  0.100mm to   0.500mm  1342     74   -94.5%
  0.500mm to   1.000mm   810    114   -85.9%
  1.000mm to   5.000mm   145    341   135.2%
  5.000mm to  10.000mm     1     25  2400.0%
 10.000mm to  20.000mm     2     14   600.0%
 20.000mm to  50.000mm     8      8     0.0%
 50.000mm to 100.000mm     2      2     0.0%
          >= 100.000mm     2      2     0.0%
--------------------------------------------
       Total distance:............1929.879mm
   Total count source:..................2348
   Total count target:...................587
 Total percent change:................-75.0%
```
## How *Arc Welder* Works
*Arc Welder* reads each GCode in the source file, searching for three extrusion or retraction commands in a row.  It adds adds these points to a special shape detection class that determines if the collected points can be represented by an arc command (G2/G3).  Once an arc is detected, *Arc Welder* compares the original GCode path with the resulting arc command to ensure that any deviation is within the specified resolution (by default, +-0.025mm).  *Arc Welder* will continue to add new points to the arc until it detects either a significant deviation from the original GCode or a change in the printer's state (a new layer, a feedrate or offset change, etc.).  It will then pull off the final point from the arc, output the altered G2/G3 command, and continue to process the file.  The resulting GCode will not vary from the source file by more than half of the specified resolution, which is configurable.  Here is a rudimentary illustration:

<figure style="text-align:center">
    <a href="{{site.url}}/assets/img/plugins/arc_welder/arc_creation_example.png" target="_blank">
        <img src="{{site.url}}/assets/img/plugins/arc_welder/arc_creation_example.png" alt="An illustration of how arcs are created.  Click to view the full sized image." title="An illustration of how arcs are created.  Click to view the full sized image."/>
    </a>
    <figcaption>
        <i>An illustration of how arcs are generated.  <a href="{{site.url}}/assets/img/plugins/arc_welder/arc_creation_example.png" target="_blank">View the Full Sized Image</a>.</i>
    </figcaption>
</figure>

In the example above, *Arc Welder* has created two arcs.  The first arc starts at P1 and ends at P5 on the blue line. The original path is shown in red.  In this example *Arc Welder* first adds three consecutive points (P1-P3) to its shape detection class and determines that the generated arc does not deviate significantly from the original path.  It then adds P4 and P5, again detecting no significant deviation.  However, at P6, the detected deviation exceeds the maximum, so P6 is not added, and an arc is generated that replaces P1-P5.  *Arc Welder* then starts a new arc from P5, P6, and P7 and continues the process.  Note:  The endpoints of every arc will ALWAYS line up exactly with the original GCode.

It is important to note that the example above is zoomed WAY in so that the deviation looks very large.  It is, in fact, extremely small and almost impossible to see with the naked eye.  You can customize the resolution in the plugin settings if 0.05mm (+- 0.025mm) is too large for you.

## *Arc Welder* Plugin Features

* **Customizable Resolution** - You control the maximum allowable deviation from the original tool path.  Higher values will result in more compression but more deviation.  Lower values will produce more accurate GCode but less compression.  The default value of 0.05mm (+- 0.025mm) produces excellent results in most cases.  I would recommend a lower value only for extreme cases, like extremely high resolution models with small nozzles and very low layer heights.  Values higher than 0.05 are not recommended.
* **Automatic and/or Manual Processing** - *Arc Welder* can be configured to automatically process newly added file or to allow manual processing via an integration with the OctoPrint file manager.  You can enable one or both of these methods depending on your preference.
* **Rename or Overwrite the Source File** - Choose to keep the original source GCode file or replace it entirely with the arc-welded file.  You can also add a custom prefix or postfix to the output file.
* **Delete the Source File After Processing** - You can create a new file and have *Arc Welder* delete the original file automatically in most cases.
* **See Detailed Conversion Statistics** - *Arc Welder* creates and stores statistics for each converted file, including compression percentage and ratio, source/target file size, and line count, as well as a detailed comparison of extrusion/retraction counts at various lengths between the source and target file.  You can view statistics for any arc-welded file by selecting it in the file manager or by clicking on the icon within the file manager.
* **Detailed Conversion Progress Bar** - See real time progress info as *Arc Welder* processes your file, including several useful statistics.  You can cancel the conversion at any time.
* **Enable/Disable Notifications** - Tired of popup messages?  Turn them off in the settings.
* **Advanced Logging Settings** - You can control logging from within the plugin's settings page if you run into problems.  You can even delete the existing log(s) completely.
* **Restore Plugin Defaults** - Easily restore the default settings if you run into trouble.
* **Receive Notifications for New Development or Maintenance Release Candidates** - Get early notifications about new features and bug fixes.  Help contribute to the project!  *Arc Welder* also supports plugin-specific release channels in a future version of OctoPrint (if that feature is eventually released).

## *Arc Welder* Library and Console Application
The core of the *Arc Welder* plugin is a set of libraries written in c++ based on code that was originally designed for the Octolapse plugin.  This code allows *Arc Welder* to parse GCode and determine the printer's position and extruder state after each command.  Since the code is written entirely in c++, it is orders of magnitude faster than similar code written in Python.  The complete source, as well as a console version and inverse processor (convert G2/G3 to G0/G1), can be found [here](https://github.com/FormerLurker/ArcWelderLib).  There are also [pre-compiled binaries](https://github.com/FormerLurker/ArcWelderLib/actions?query=workflow%3A%22CMake+Build+Matrix%22), though I've not gotten them to work properly in MacOS or in some flavors of Linux.  There are currently no GitHub hosted runners for any Raspberry Pi.  I am working on these issues.

Using the console application, it is possible to arc-weld files via most slicers as a post-processor.  However, all slicers that I have tested except for [Simplify 3D](https://www.simplify3d.com/) fail to correctly visualize the G2/G3 commands.  Simplify 3D does seem to work perfectly for this, but other slicers make it look like the GCode is faulty.  Keep that in mind if you plan to integrate the *Arc Welder Console Application* with your slicer.

## Firmware Considerations
Your printer's firmware must be capable of printing G2/G3 commands to use the GCode produced by *Arc Welder*.  Additionally, arc support must be enabled and properly configured.  Firmware support varies, and many older versions produce arcs less accurately and more slowly than expected.

### Marlin
[Marlin](https://github.com/MarlinFirmware/Marlin/) has supported arc commands for a long time.  However, starting with [version 2.0.6](https://github.com/MarlinFirmware/Marlin/releases/tag/2.0.6) arc support has been greatly enhanced.  I recommend you upgrade to at least this version before using *Arc Welder* because your experience will be much better.  Arc support must be enabled in your Configuration_adv.h file.

For recent versions of Marlin (2.0.6 and above), you can send an ```M115``` to see if your firmware has *ARC_SUPPORT* enabled.  For earlier versions you can send an empty ```G2``` or ```G3``` command.  If your printer responds with ```unknown command```, arc support is not enabled.

If your printer is running a fork of Marlin, but arc support is not enabled or is buggy, I recommend creating an issue within the fork's repository.

> "A plugin that can convert curves into arcs will be massively welcome and should make a great improvement in performance and print results."
>
> **[`Scott Lahteine`](https://www.patreon.com/thinkyhead)** - _Creator of [Marlin Firmware](https://github.com/MarlinFirmware/Marlin/)_

### Prusa Firmware
[Prusa's fork of Marlin](https://github.com/prusa3d/Prusa-Firmware) does support G2/G3 commands, however the default settings can produce sharp corners for very small arcs.  I've only noticed this in a few of my test prints, so it is not a particularly common issue.  You should be able to see it on the roof of a Benchy if you look closely.  Reducing the *MM_PER_ARC_SEGMENT* setting slightly can correct this but can also introduce stuttering.  Reducing the value massively (say to 0.1mm) will introduce a LOT of stutter and is NOT recommended.  Please note that adjusting this setting currently requires a manual firmware recompile.

I have been toying with the firmware and have submitted a pull request to enhance the capabilities, but it hasn't made it into the firmware yet and may require further modifications.  I am planning to add some enhancements from Marlin 2.0.6 as well.  I also added some new GCodes for adjusting arc interpolating and for retrieving the firmware settings for arc generation.  You can view the pull request [here](https://github.com/prusa3d/Prusa-Firmware/pull/2657).  Feel free to give this pull request a thumbs up, but realize that it needs some work and that the good folks at [Prusa Research]([https://www.prusa3d.com/) have a lot on their plates.

Also, some very old versions of Prusa's firmware (I'm not sure exactly how old) do not support bed leveling adjustments during arc movements.  Please make sure you are using a recent version of the firmware so that interpolated movements are properly leveled.

### Klipper
[Klipper](https://github.com/KevinOConnor/klipper/) seems to handle G2/G3 commands with ease, as long as the *GCode_arcs* config section is enabled.  G2/G3 support was added on September 13, 2019, so make sure you update Klipper if you are using an older version.

### Other Firmware
Though G2/G3 support is not universal, nor are all implementations equal, it is relatively easy to test.  You can do so in the OctoPrint terminal by sending the the following commands, one at a time:

```
G90
G28 X Y
G0 X0 Y0
G2 X40 I20
```

If your printer supports arc commands, it should move across a small arc from the origin.  Please feel free to let me know if your firmware supports arc movements, and I may add it to the list.

**Warning**:  The above GCode has not been tested on all printers.  Please use it with caution and [report any issues here](https://github.com/FormerLurker/ArcWelderPlugin/issues).

### Other Firmware Considerations

Most firmware will convert G2/G3 commands to many small segments through a process called interpolation.  The length of these segments varies by implementation.  In most cases the interpolated segments are much closer together than the linear segments you will find within your GCode file, but it's impossible to know for sure without examining the firmware in detail.

All firmware that I am aware of will inscribe these interpolated segments within the arc.  These segments will be entirely within the arc, only touching it at the endpoints.  This will reduce the average radius slightly.  In most cases, this effect is minimal and has no practical impact.  However, in some odd cases, like a snap fitting that is extremely sensitive to changes in diameter, the effect may be noticeable.  The smaller the interpolated segments (all firmware controlled), the less of an effect there is.  In general, it will be a much smaller effect than normal variations in filament diameter.  I hope to find a solution to this problem.

G2/G3 support is not perfect at the moment, but I suspect things will start to improve as they become more common.  If you are willing and have the skills to improve G2/G3 support in any way, please do!

## License

View the [*Arc Welder* license](https://raw.githubusercontent.com/FormerLurker/ArcWelderPlugin/master/LICENSE).
