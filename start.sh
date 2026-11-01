
#!/usr/bin/env bash
set -euo pipefail

echo "Starting Tailscale..."

./bin/tailscaled \
  --tun=userspace-networking \
  --state=/tmp/tailscaled.state \
  --socket=/tmp/tailscaled.sock \
  --socks5-server=127.0.0.1:1055 &

for i in $(seq 1 30); do
  if ./bin/tailscale --socket=/tmp/tailscaled.sock status >/dev/null 2>&1; then
    break
  fi
  sleep 1
done

./bin/tailscale --socket=/tmp/tailscaled.sock up \
  --auth-key="$TS_KEY" \
  --hostname=arithmetic-render \
  --accept-dns=false

echo "Tailscale connected."

echo "Starting MySQL TCP forwarder..."

./bin/gost \
  -L=tcp://127.0.0.1:3307/100.64.121.62:3306 \
  -F=socks5://127.0.0.1:1055 &

echo "Starting Flask application..."

exec gunicorn "run:app" --bind "0.0.0.0:${PORT:-10000}"
