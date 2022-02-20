#!/usr/bin/env bash

set -e

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)
cd "$SCRIPT_DIR"/..

set -x

black --check scripts packages/backend
flake8 --benchmark scripts packages/backend
mypy scripts packages/backend
