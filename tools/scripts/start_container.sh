# SPDX-FileCopyrightText: 2024 Michael Bracht
# SPDX-License-Identifier: MIT
#!/bin/bash

SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
ROOT_DIR="$(realpath "$(dirname "$(readlink -f "$0SCRIPT_DIR/../..")")")"

mkdir --parents input
mkdir --parents output

docker compose --file ${ROOT_DIR}/tools/docker/docker-compose.yml up