"""Tests for EEBUS diagnostics."""

from unittest.mock import MagicMock

import pytest

from custom_components.eebus.diagnostics import async_get_config_entry_diagnostics


@pytest.mark.asyncio
async def test_diagnostics_output():
    """Test diagnostics returns expected structure."""
    hass = MagicMock()
    entry = MagicMock()
    entry.data = {
        "grpc_host": "192.168.1.100",
        "grpc_port": 50051,
        "device_ski": "abcdef1234567890",
    }
    coordinator = MagicMock()
    coordinator.data = {"power_watts": 1500.0, "connected": True}
    entry.runtime_data = coordinator

    result = await async_get_config_entry_diagnostics(hass, entry)

    assert "config" in result
    assert result["config"]["grpc_host"] == "192.168.1.100"
    assert result["config"]["device_ski"] == "**REDACTED**"
    assert "coordinator_data" in result
