"""Diagnostics for the EEBUS integration."""

from __future__ import annotations

from typing import Any

from homeassistant.core import HomeAssistant

from . import EebusConfigEntry


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant,
    entry: EebusConfigEntry,
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""
    coordinator = entry.runtime_data

    return {
        "config": {
            "grpc_host": entry.data.get("grpc_host"),
            "grpc_port": entry.data.get("grpc_port"),
            "device_ski": "**REDACTED**",
        },
        "coordinator_data": dict(coordinator.data) if coordinator.data else None,
    }
