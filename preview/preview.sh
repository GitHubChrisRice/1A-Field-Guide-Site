#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
VENV="$REPO_ROOT/.venv-preview"
PYTHON="$VENV/bin/python"

if [[ ! -x "$PYTHON" ]]; then
  echo "Creating local preview environment..."
  python3 -m venv "$VENV"
fi

echo "Checking preview dependencies..."
"$PYTHON" -m pip install --disable-pip-version-check -r "$SCRIPT_DIR/requirements.txt"

echo
echo "California 1A Field Guide preview"
echo "Open http://127.0.0.1:8000/"
echo "Press Ctrl+C to stop the preview server."
echo

cd "$REPO_ROOT"

if command -v open >/dev/null 2>&1; then
  (sleep 2; open "http://127.0.0.1:8000/" >/dev/null 2>&1) &
elif command -v xdg-open >/dev/null 2>&1; then
  (sleep 2; xdg-open "http://127.0.0.1:8000/" >/dev/null 2>&1) &
fi

"$PYTHON" -m mkdocs serve --dev-addr 127.0.0.1:8000
