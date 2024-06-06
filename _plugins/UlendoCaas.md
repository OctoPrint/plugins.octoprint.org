---
layout: plugin

id: autocal
title: Ulendo Calibration as a Service
description: Double the performance of your legacy printer with Ulendo CaaS. CaaS automatically tunes vibration compensation parameters for firmware using FT-MOTION module, allowing printers to reduce print times by 50% while maintaining high levels of accuracy.
authors: info@ulendo.io
license: ""

# today's date in format YYYY-MM-DD, e.g.
date: 2024-06-06

homepage: https://github.com/S2AUlendo/UlendoCaaS
source: https://github.com/S2AUlendo/UlendoCaaS
archive: https://github.com/S2AUlendo/UlendoCaaS/archive/refs/tags/v0.1.3.zip

# Set this if your plugin heavily interacts with any kind of cloud services.
privacypolicy: https://live.d11dolnrbc1eee.amplifyapp.com/privacy

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
follow_dependency_links: false

tags:
- control
- performance
- input shaping
- speed

screenshots:
- url: /assets/img/plugins/UlendoCaas/realtime_accelerometer_updates.png
  alt: view of the pre-computed response of the selected input shaper
  caption: projected response
- url: /assets/img/plugins/UlendoCaas/detailed_vibration_compensation_analysis.png
  alt: view of the pre-computed response of the selected input shaper
  caption: projected response
- url: /assets/img/plugins/UlendoCaas/compensation_verification.png
  alt: view of the measured vibration response after the compensation is applied
  caption: actual vibration response after compensation
- url: /assets/img/plugins/UlendoCaas/plugin_configuration.png
  alt: overview of configuration available through the settings window
  caption: advanced configuration options

featuredimage: /assets/img/plugins/UlendoCaas/CaaS_Ad4.png

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

  octoprint:
  - 1.3.0

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

  # Compatible Python version
  #
  # Plugins should aim for compatibility for Python 2 and 3 for now, in which case the value should be ">=2.7,<4".
  #
  # Plugins that only wish to support Python 3 should set it to ">=3,<4".
  #
  # If your plugin only supports Python 2 it will no longer be accepted on the plugin repository.
  #
  # Uncomment the appropriate setting
  python: ">=3,<4" # Python 3 only

---

# Ulendo Calibration as a Service / CaaS

Ulendo Calibration as a service plugin for OctoPrint is a plugin that is designed to help users maximize the performance of their printer. 

This tool is meant to allow users to quickly and efficiently evaluate and select a compensation strategy that is right for their printer. Ulendo's Calibration as a Service platform quickly evaluates hundreds of potential compensation parameters and directly recommends the option that will provide the best vibration compensation while minimizing rounding. 

With the support of the FT_MOTION feature, this plugin can allow printers to print at over 2X the typical speed and acceleration without any additional hardware modifications to their machines. 

In testing on the Ender V2, speeds of over 150 mm/s and accelerations of 5,000 mm/s<sup>2</sup> were tested with minimal rounding. This plugin has been tested to run on several other machines that were retrofitted with the Marlin software, machines with build sizes varying from 150 mm<sup>3</sup> to 1000 mm<sup>3</sup>. In all scenarios the when used in conjunction with the software all the printers were able to achieve over 2X speed increase.

The CaaS difference - high speed vibration compensation: 
![The CaaS Difference Ender 3 V2][neov2]

[neov2]: https://github.com/S2AUlendo/UlendoCaaS/blob/main/octoprint_ulendocaas/assets/img/ulendo_autocal/CaaS_Ender3NeoV2.png "The CaaS difference"



The CaaS difference - high speed vibration compensation:: 
![The CaaS Difference Lulzbot TazPro][tazpro]

[tazpro]: https://github.com/S2AUlendo/UlendoCaaS/blob/main/octoprint_ulendocaas/assets/img/ulendo_autocal/CaaS_TazPro.png "The CaaS difference"


Ulendo's CaaS is a great option for contract manufacturers looking to improve the performance of their existing assets. When paired with a compatible printer this plugin can reduce print times by more than 50% percent, improving facility throughput. 


## About Input Shaping
Input Shaping is a technology that is used to help compensated unwanted vibration that is present in many manufacturing machines. However, one of the common downsides is that it often introduces unwanted rounding due to the delay in the system.

For more on the downsides, and how Ulendo is able to address it through it's other offerings. Checkout our Whitepaper on FBS vs Input Shaping
[Ulendo's Input Shaping Whitepaper](https://www.ulendo.io/s/Ulendo-Input-Shaping-Comparison-White-Paper-2023.pdf "Input Shaping Whitepaper")

### Avoiding rounding
While other tools and manually configured input shapers allow you to set the target frequency, Ulendo's CaaS tool also automatically determines depth of the filter required to compensate for the vibration. This helps to mitigate potential unwanted rounding from the shaper being applied. i.e. The strength of the filter is designed to match the vibration of your individual machine.

## Dependencies 
This plugin works in conjunction with the FT_MOTION system that is available in Marlin. This FT_MOTION feature is an external dependency, and this plugin will not be able to work without it. 
Additionally, this software requires an accelerometer to be connected. As of the 0.1.2 update only the ADXL345 is supported. However, there is additional planned support for the ADXL365 and the LIS3DH accelerometer. 

## FAQ
1. Does this work with all printers
    ⋅⋅* No, This plugin was specifically made to work with a Marlin feature called FT_MOTION developed by ULENDO. It is only compatible with versions of Marlin >2.1.3. [Fixed Time Motion](https://marlinfw.org/docs/gcode/M493.html "Fixed Time Motion")

2. Does this software require changes to the machine components?
    ⋅⋅*No, aside from attaching an accelerometer, there are no other machine requirements

3. Does this only work on COREXY machines?
    ⋅⋅* No, This software has been tested on traditional cartesian, COREXY, Ultimaker-style cartesian printers, and bed slinger printers, all printer types were able to see some relatively improvement in their performance when compared against the uncompensated prints. 

4. Will my failure rates increase, if I increase the speed?
    ⋅⋅* When compared to the uncompensated, default behavior most printers were able to achieve 2X without any decrease in reliability. However, there are other factors besides vibration that may affect printer performance.

5. Can I run this on my desktop computer without a Raspberry Pi
    - No, a Raspberry Pi is a required to connect and collect data from the accelerometer

6. Can I use this on my printer that does not run Marlin
    ⋅⋅* No, there is planned support for other platforms in the future. However, currently only Marlin versions >2.1.3 is supported. Talk with your OEM about adding support for Ulendo CaaS