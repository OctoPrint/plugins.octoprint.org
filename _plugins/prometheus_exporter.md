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

compatibility:
  python: ">=2.7,<4"

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
  - print total time - as counter
  - last print time - as gauge
  - fan speed - as gauge
  - extrusion total - as counter
  - x, y and z travel - as a counter
  - last print extrusion - as gauge

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

If you have authentication enabled use this version:
```
 - job_name: 'octoprint'
    scrape_interval: 5s
    metrics_path: '/plugin/prometheus_exporter/metrics'
    params:
      apikey: ['__OCTOPRINT_APIKEY__']
    static_configs:
      - targets: ['octoprint:80']
```

For example grafana dashboard please visit [the github repo](https://github.com/tg44/OctoPrint-Prometheus-Exporter/tree/master/extras).
