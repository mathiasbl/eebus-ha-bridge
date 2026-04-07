"""Convenience re-exports for generated protobuf stubs.

Run `ha-integration/generate_proto.sh` to regenerate after proto changes.
"""

try:
    from .generated.eebus.v1.common_pb2 import (
        DeviceRequest,
        Empty,
        LoadLimit,
        MeasurementEntry,
        PowerMeasurement,
    )
    from .generated.eebus.v1.device_service_pb2_grpc import DeviceServiceStub
    from .generated.eebus.v1.lpc_service_pb2 import (
        WriteLoadLimitRequest,
        WriteFailsafeLimitRequest,
    )
    from .generated.eebus.v1.lpc_service_pb2_grpc import LPCServiceStub
    from .generated.eebus.v1.monitoring_service_pb2_grpc import MonitoringServiceStub
except ImportError:
    # Stubs not yet generated — will fail at runtime if used
    pass
