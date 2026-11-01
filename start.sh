
#!/usr/bin/env bash
set -euo pipefail

# ==========================================
# 1. Start Tailscale
# ==========================================

echo "Starting Tailscale..."

./bin/tailscaled \
  --tun=userspace-networking \
  --state=/tmp/tailscaled.state \
  --socket=/tmp/tailscaled.sock \
  --socks5-server=127.0.0.1:1055 &

TS_PID=$!

# Wait for Tailscale daemon
for i in $(seq 1 30); do
  if ! kill -0 "$TS_PID" 2>/dev/null; then
    echo "ERROR: Tailscale daemon stopped."
    exit 1
  fi

  if ./bin/tailscale \
    --socket=/tmp/tailscaled.sock status >/dev/null 2>&1; then
    break
  fi

  sleep 1
done

# ==========================================
# 2. Connect to Tailscale network
# ==========================================

echo "Connecting to Tailscale..."

./bin/tailscale --socket=/tmp/tailscaled.sock up \
  --auth-key="$TS_KEY" \
  --hostname=arithmetic-render \
  --accept-dns=false

echo "Tailscale connected."

# ==========================================
# 3. Start MySQL TCP forwarder
# ==========================================

echo "Starting MySQL TCP forwarder..."

./bin/gost \
  -L=tcp://127.0.0.1:3307/100.64.121.62:3306 \
  -F=socks5://127.0.0.1:1055 \
  > /tmp/gost.log 2>&1 &

GOST_PID=$!

# ==========================================
# 4. Check GOST availability
# ==========================================

echo "Waiting for GOST..."

GOST_READY=false

for i in $(seq 1 20); do
  if ! kill -0 "$GOST_PID" 2>/dev/null; then
    echo "ERROR: GOST process stopped."
    cat /tmp/gost.log || true
    exit 1
  fi

  if python -c "
import socket
s = socket.create_connection(('127.0.0.1', 3307), timeout=2)
s.close()
" 2>/dev/null; then
    GOST_READY=true
    break
  fi

  sleep 1
done

if [ "$GOST_READY" != "true" ]; then
  echo "ERROR: GOST did not become ready."
  cat /tmp/gost.log || true
  exit 1
fi

echo "GOST forwarder is accepting connections."

# ==========================================
# 5. Test MySQL connection
# ==========================================

echo "Testing MySQL connection..."

python -c '
import os
from sqlalchemy import create_engine, text

engine = create_engine(
    os.environ["DATABASE_URL"],
    pool_pre_ping=True
)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1")).scalar()
        print("MySQL connection successful:", result)
finally:
    engine.dispose()
'

# ==========================================
# 6. Start Flask application
# ==========================================

echo "Starting Flask application..."

exec gunicorn "run:app" \
  --bind "0.0.0.0:${PORT:-10000}"
