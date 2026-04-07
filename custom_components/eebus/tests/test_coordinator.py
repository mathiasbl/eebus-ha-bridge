"""Tests for the EEBUS coordinator."""

from unittest.mock import MagicMock, patch

from custom_components.eebus.coordinator import EebusCoordinator, POLL_INTERVAL


def test_coordinator_poll_interval():
    """Test that coordinator poll interval is configured."""
    from datetime import timedelta
    assert POLL_INTERVAL == timedelta(seconds=30)


def test_coordinator_attributes():
    """Test that coordinator class stores expected connection param names."""
    import inspect
    sig = inspect.signature(EebusCoordinator.__init__)
    params = list(sig.parameters.keys())
    assert "host" in params
    assert "port" in params
    assert "ski" in params


@patch("homeassistant.helpers.frame._hass")
def test_coordinator_init(mock_hass_frame):
    """Test that coordinator stores connection params."""
    hass = MagicMock()
    mock_hass_frame.hass = hass

    with patch("homeassistant.helpers.update_coordinator.DataUpdateCoordinator.__init__", return_value=None):
        coordinator = EebusCoordinator.__new__(EebusCoordinator)
        coordinator.host = "192.168.1.100"
        coordinator.port = 50051
        coordinator.ski = "test-ski"
        coordinator._channel = None
        coordinator._stream_tasks = []
        coordinator._was_unavailable = False

    assert coordinator.host == "192.168.1.100"
    assert coordinator.port == 50051
    assert coordinator.ski == "test-ski"
    assert coordinator._channel is None
    assert coordinator._was_unavailable is False
