#!/bin/bash
# Generate Python gRPC stubs from protobuf definitions
set -euo pipefail

PROTO_DIR="../eebus-bridge/proto"
OUT_DIR="custom_components/eebus/generated"

mkdir -p "$OUT_DIR"

python -m grpc_tools.protoc \
  -I "$PROTO_DIR" \
  --python_out="$OUT_DIR" \
  --grpc_python_out="$OUT_DIR" \
  --pyi_out="$OUT_DIR" \
  eebus/v1/common.proto \
  eebus/v1/device_service.proto \
  eebus/v1/lpc_service.proto \
  eebus/v1/monitoring_service.proto

touch "$OUT_DIR/__init__.py"
touch "$OUT_DIR/eebus/__init__.py"
touch "$OUT_DIR/eebus/v1/__init__.py"

echo "Proto stubs generated in $OUT_DIR"
