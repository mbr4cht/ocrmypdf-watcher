# SPDX-FileCopyrightText: 2024 Michael Bracht
# SPDX-License-Identifier: MIT
#!/bin/bash

SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"

docker build ${SCRIPT_DIR}/.. --file ${SCRIPT_DIR}/../.docker/Dockerfile --tag ocrmypdf-watcher:latest 
