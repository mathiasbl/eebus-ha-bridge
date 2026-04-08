#!/usr/bin/with-contenv bashio

# Map HA add-on options to environment variables
# The Go bridge reads these via applyEnvOverrides() in config.go
export EEBUS_GRPC_PORT=$(bashio::config "GRPC_PORT")
export EEBUS_PORT=$(bashio::config "EEBUS_PORT")
export EEBUS_VENDOR=$(bashio::config "EEBUS_VENDOR")
export EEBUS_BRAND=$(bashio::config "EEBUS_BRAND")
export EEBUS_MODEL=$(bashio::config "EEBUS_MODEL")

SERIAL=$(bashio::config "EEBUS_SERIAL")
if bashio::var.has_value "${SERIAL}"; then
    export EEBUS_SERIAL="${SERIAL}"
fi

# Store certificates in persistent add-on config directory
export EEBUS_CERT_STORAGE="/config/certs"
mkdir -p "${EEBUS_CERT_STORAGE}"

# Generate minimal config file (env vars override all values)
CONFIG_FILE="/etc/eebus-bridge/config.yaml"
mkdir -p "$(dirname "${CONFIG_FILE}")"
cat > "${CONFIG_FILE}" <<EOF
grpc:
  port: ${EEBUS_GRPC_PORT}
eebus:
  port: ${EEBUS_PORT}
certificates:
  auto_generate: true
  storage_path: "${EEBUS_CERT_STORAGE}"
EOF

bashio::log.info "Starting EEBUS Bridge"
bashio::log.info "  gRPC port:  ${EEBUS_GRPC_PORT}"
bashio::log.info "  EEBUS port: ${EEBUS_PORT}"
bashio::log.info "  Cert store: ${EEBUS_CERT_STORAGE}"

# Exec replaces the shell so signals reach the Go binary directly
exec /usr/local/bin/eebus-bridge --config "${CONFIG_FILE}"
