---
layout: plugin

id: prometheus_exporter
title: Prometheus Exporter
description: A plugin for prometheus compatible metrics endpoint
author: Gergo Torcsvari
license: MIT

date: 2019-12-09

homepage: https://github.com/tg44/OctoPrint-Prometheus-Exporter
source: https://github.com/tg44/OctoPrint-Prometheus-Exporter
archive: https://github.com/tg44/OctoPrint-Prometheus-Exporter/archive/master.zip

follow_dependency_links: false

tags:
- prometheus
- grafana
- monitor
- monitoring
- usage
- status

---

This is a utility plugin, which enables the [prometheus server](https://prometheus.io/) to scrape metrics from your octoprint instance.
Later on, you can use data vizualisation tools (for example [grafana](https://grafana.com/)) to track and visualize your printer(s) status(es).

This plugin has no visible UI!

Currently exported metrics:
 - python version - as info
 - octoprint version, hostname, os - as info
 - actual temperature - as gauge with tool identifier label
 - target temperature - as gauge with tool identifier label
 - client number - as gauge; the actually connected clients to the host
 - printer state - as info
 - started prints - as counter
 - failed prints - as counter
 - done prints - as counter
 - cancelled prints - as counter
 - timelaps count - as counter
 - print progress - as gauge with path label
 - slice progress - as gauge with path label
 
All of the metrics are prefixed as `octoprint_` for easier identification. 
 
The metrics endpoint is: http://localhost:5000/plugin/prometheus_exporter/metrics (change the host+port to your actual host+port)

Example scrape config (or check it from the project repo):
```
- job_name: 'octoprint'
    scrape_interval: 5s
    metrics_path: '/plugin/prometheus_exporter/metrics'
    static_configs:
      - targets: ['octoprint:80']
```
