---
layout: plugin
    
id: PrusaXLFix
title: "Prusa XL/XL+ Fix"
description: "A fix for an incompatibility introduced with Prusa firmware 6.10.x and later"
authors:
  - "Greg Anuzelli"
license: MIT License
    
date: 2026-10-06
    
homepage: https://github.com/anuzellig/octoprint-prusa-xl-fix
source: https://github.com/anuzellig/octoprint-prusa-xl-fix
archive: https://github.com/anuzellig/octoprint-prusa-xl-fix/releases/download/1.0.0/octoprint_prusaxltoolfix-1.0.0.tar.gz
    
    
tags:
  - prusa
  - ai-developed
        
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