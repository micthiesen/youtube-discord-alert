#!/usr/bin/env bash

set -e

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)
cd "$SCRIPT_DIR"/..

set -x

black --check scripts src/backend
flake8 --benchmark scripts src/backend
mypy scripts src/backend
