# EEBUS Bridge Add-on

## Overview

This add-on runs the EEBUS Bridge (Go) as a managed service inside Home Assistant.
It replaces the need to run the bridge via `docker-compose` separately.

The bridge speaks the EEBUS protocol (SHIP + SPINE) to communicate with
EEBUS-capable heat pumps (e.g. Vaillant aroTHERM plus) and exposes a gRPC API
that the **EEBUS custom integration** connects to.

## Prerequisites

- The **EEBUS** custom integration must be installed (via HACS or manually)
- Your heat pump gateway (e.g. VR940f) must be on the same network

## Configuration

| Option | Default | Description |
|--------|---------|-------------|
| `GRPC_PORT` | `50051` | Port for the gRPC API |
| `EEBUS_PORT` | `4712` | Port for EEBUS SHIP protocol |
| `EEBUS_VENDOR` | `HomeAssistant` | Vendor name announced via EEBUS |
| `EEBUS_BRAND` | `eebus-bridge` | Brand name announced via EEBUS |
| `EEBUS_MODEL` | `eebus-bridge` | Model name announced via EEBUS |
| `EEBUS_SERIAL` | *(auto)* | Serial number (leave empty for default) |

## Integration setup

When configuring the EEBUS integration, use:
- **Host:** `localhost` (the add-on runs on the same host network)
- **Port:** `50051` (or whatever you set `GRPC_PORT` to)

## Certificate persistence

Certificates are stored in `/config/certs` (mapped to the add-on config directory).
They persist across add-on restarts and updates. If you delete this directory,
a new certificate (and SKI) will be generated and you will need to re-pair
with your heat pump.

## Troubleshooting

Check the add-on logs in **Settings > Add-ons > EEBUS Bridge > Log**.
The bridge logs the local SKI at startup — use this for pairing.
