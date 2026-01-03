---
layout: plugin

id: octo_fire_guard
title: Octo Fire Guard
description: Temperature monitoring plugin that prevents fire hazards by monitoring hotend and heatbed temperatures in real-time
author: rdar-lab
license: MIT

date: 2026-01-02

homepage: https://github.com/rdar-lab/octo-fire-guard
source: https://github.com/rdar-lab/octo-fire-guard
archive: https://github.com/rdar-lab/octo-fire-guard/archive/main.zip

tags:
- safety
- temperature
- monitoring
- fire
- emergency
- thermal
- protection

screenshots:
- url: /assets/img/plugins/octo_fire_guard/settings-panel.png
  alt: Octo Fire Guard Settings Panel
  caption: Settings panel with temperature thresholds and termination mode configuration
- url: /assets/img/plugins/octo_fire_guard/alert-modal.png
  alt: Temperature Alert Modal
  caption: Alert modal displayed when temperature threshold is exceeded

featuredimage: /assets/img/plugins/octo_fire_guard/alert-modal.png

compatibility:
  python: ">=3.8,<4"

---

An OctoPrint plugin that monitors printer temperatures in real-time to prevent fire hazards. The plugin watches both hotend and heatbed temperatures and triggers emergency shutdown procedures when configurable thresholds are exceeded.


> [!WARNING]
> **⚠️ THIS PLUGIN IS A SAFETY FEATURE, NOT A REPLACEMENT FOR PROPER PRINTER SUPERVISION ⚠️**
> 
> **This plugin does not guarantee safety and should not be relied upon as the sole fire prevention mechanism. Always monitor your printer during operation. OctoPrint may not be running, the plugin may malfunction, or other failure modes may occur that prevent the plugin from responding to dangerous conditions.**


## Motivation

Designed to address scenarios where hardware failures (such as a MOSFET failing in closed-circuit mode) can cause uncontrolled temperature increases that firmware alone cannot stop. By integrating with OctoPrint's temperature monitoring system and optional PSU control, this plugin provides an additional safety layer to prevent potential fire hazards.

## Features

- **Real-time Temperature Monitoring**: Continuously monitors hotend and heatbed temperatures via OctoPrint's temperature data stream
- **Self-Test Monitoring**: Automatically detects if temperature data stops arriving and issues warnings to ensure the plugin is actively monitoring
- **Dual Threshold Configuration**: Separate configurable thresholds for hotend (default: 250°C) and heatbed (default: 100°C)
- **Immediate Alert System**: Displays a prominent alert popup in the OctoPrint interface when thresholds are exceeded
- **Flexible Emergency Response**: Choose between two termination modes:
  - **GCode Commands**: Execute custom GCode commands (default: M112 emergency stop + heater shutdown)
  - **PSU Control Integration**: Turn off power entirely via PSU Control plugin
- **User-Friendly Interface**: Easy-to-use settings panel with test functionality to verify proper operation
- **Audio Alerts**: Plays an alert sound when temperature threshold is exceeded

## Configuration

After installation, configure the plugin in OctoPrint Settings → Plugins → Octo Fire Guard:

![settings screenshot](/assets/img/plugins/octo_fire_guard/settings-panel.png)

### Temperature Thresholds

- **Hotend Threshold**: Maximum safe temperature for the hotend in °C (default: 250°C)
- **Heatbed Threshold**: Maximum safe temperature for the heatbed in °C (default: 100°C)

### Self-Test Monitoring

- **Enable Self-Test Monitoring**: When enabled, the plugin monitors itself to ensure it's receiving temperature data from the printer
- **Temperature Data Timeout**: Time in seconds before issuing a warning if no temperature data is received (default: 300 seconds / 5 minutes)

If the printer is connected but the plugin doesn't receive temperature data for the configured timeout period, it will issue a warning notification. This helps ensure the plugin is functioning correctly and actively monitoring your printer.

### Termination Mode

Choose how the plugin responds when a threshold is exceeded:

#### GCode Commands Mode

Execute custom GCode commands to handle the emergency. Default commands:

```gcode
M112        # Emergency stop
M104 S0     # Turn off hotend
M140 S0     # Turn off heatbed
```

You can customize these commands to suit your printer's requirements.

#### PSU Control Mode

Integrates with the [PSU Control plugin](https://plugins.octoprint.org/plugins/psucontrol/) to turn off power completely. This mode:
1. Turns off heaters using GCode
2. Signals the PSU Control plugin to cut power

**Note**: Requires the PSU Control plugin to be installed and configured.

## Testing

The plugin provides two test buttons in the settings panel to verify functionality:

- **Test Alert System**: Tests the alert popup display without triggering emergency actions. This verifies that the visual alert, audio notification, and user interface components work correctly.

![alert screenshot](/assets/img/plugins/octo_fire_guard/alert-modal.png)
  
- **Test Emergency Actions**: Tests the actual emergency response by executing your configured termination commands (GCode or PSU control). Use this to verify that your emergency shutdown procedure works correctly before an actual emergency occurs.

**Important**: The "Test Emergency Actions" button will execute the real emergency shutdown commands configured in your termination settings. Make sure your printer is in a safe state before testing.

## Safety Considerations

- **This plugin is a safety feature, not a replacement for proper printer supervision**
- Set thresholds appropriate for your printer and materials
- Regularly test the plugin to ensure it's functioning correctly
- Ensure your printer's firmware has proper thermal runaway protection
- For PSU Control mode, verify your PSU Control setup works correctly before relying on it

## Requirements

- OctoPrint 1.4.0 or higher
- Python 3.8 or higher
- For PSU Control mode: PSU Control plugin installed and configured
