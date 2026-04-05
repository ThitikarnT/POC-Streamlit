#!/usr/bin/env bash
set -euo pipefail
URL="$1"
curl -fsS "$URL" >/dev/null
echo "Smoke test passed: $URL"
