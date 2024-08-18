# SPDX-FileCopyrightText: 2024 Michael Bracht
# SPDX-License-Identifier: MIT
#!/bin/bash

SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"

mkdir -p input
mkdir -p output

docker compose --file ${SCRIPT_DIR}/../.docker/docker-compose.yml up