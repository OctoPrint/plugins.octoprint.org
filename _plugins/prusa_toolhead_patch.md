---
layout: plugin
    
id: prusa_toolhead_patch
title: "Prusa Buddy Toolhead Fix"
description: "A fix for an incompatibility introduced with Prusa firmware 6.10.x and later"
authors:
  - "Greg Anuzelli"
  - jneilliii
license: MIT License
    
date: 2026-10-22
    
homepage: https://gist.github.com/jneilliii/5198b0e5a0057f57821459dec510a659
source: https://gist.github.com/jneilliii/5198b0e5a0057f57821459dec510a659
archive: https://gist.githubusercontent.com/jneilliii/5198b0e5a0057f57821459dec510a659/raw/prusa_toolhead_patch.py
    
    
tags:
  - prusa
        
compatibility:    
  octoprint:
    - 1.11.0
    
  os:
  - linux
  - windows
  - macos
  - freebsd
    
  python: ">=3,<4" # Python 3 only

    
---
Prusa firmware v6.10.x for the XL and XL+ printers introduced an incompatibility with Octorprint. Specifically the the `M106/M107/M201/M203/M221` commands now want a valid tool to be specified. This is (probably) a temporary fix until the bug in the firmware is corrected, assuming it is in-fact a bug. 
