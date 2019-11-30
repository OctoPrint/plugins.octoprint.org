---
layout: plugin

id: resource_monitor
title: OctoPrint-Resource-Monitor
description: A plugin to view the current CPU, RAM, disk and network usage on your system
author: Renaud Gaspard
license: MIT

date: 2019-12-01

homepage: https://github.com/Renaud11232/OctoPrint-Resource-Monitor
source: https://github.com/Renaud11232/OctoPrint-Resource-Monitor
archive: https://github.com/Renaud11232/OctoPrint-Resource-Monitor/archive/master.zip

follow_dependency_links: false

tags:
- resource
- monitor
- memory
- disk
- network
- cpu
- processor
- usage

screenshots:
- url: /assets/img/plugins/resource_monitor/cpu.png
  alt: CPU
  caption: Processor usage
- url: /assets/img/plugins/resource_monitor/memory.png
  alt: Memory
  caption: Memory usage
- url: /assets/img/plugins/resource_monitor/disk.png
  alt: Disk
  caption: Disk usage
- url: /assets/img/plugins/resource_monitor/network.png
  alt: Network
  caption: Network usage

featuredimage: /assets/img/plugins/resource_monitor/cpu.png

compatibility:
  octoprint:
  - 1.2.0

  os:
  - linux
  - windows
  - macos
  - freebsd

---

This plugin adds a neat tab containing various information and graphs about your system resource usage.

It displays information about your CPU, memory, disks and network usage.
