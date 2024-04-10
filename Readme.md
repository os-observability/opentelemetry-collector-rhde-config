# OpenTelemetry Collector for Red Hat Device Edge (RHDE)

[![Copr build status](https://copr.fedorainfracloud.org/coprs/miyunari/redhat-opentelemetry-collector/package/opentelemetry-collector-rhde-config/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/miyunari/redhat-opentelemetry-collector/package/opentelemetry-collector-rhde-config/)

This repository contains RPM configuration for OpenTelemetry collector for Red Hat Device Edge.

The RPM is built at [redhat-opentelemetry-collector](https://copr.fedorainfracloud.org/coprs/miyunari/redhat-opentelemetry-collector/package/opentelemetry-collector-rhde-config/)

## Overview

The RPM will:
* install and configure OpenTelemetry collector
* install systemd collector service
* configure collector service on Microshift which forwards data to systemd collector service

## Build locally

```bash
fedpkg --release f37 mockbuild
```

Then upload the source RPM into Copr and build it there.

Install and uninstall: 
```bash
sudo rpm -i opentelemetry-collector-rhde-config-1.0-1.fc39.noarch.rpm 
sudo dnf remove opentelemetry-collector-rhde-config.noarch
```

List and start systemd service
```bash
sudo systemctl list-unit-files --all | grep opentelemetry
sudo systemctl start opentelemetry-collector-rhde-config.service
journalctl -u opentelemetry-collector-rhde-config.service
```
