# SPDX-FileCopyrightText: 2024 Michael Bracht
# SPDX-License-Identifier: MIT
#!/bin/bash

SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
ROOT_DIR="$(realpath "$(dirname "$(readlink -f "$0SCRIPT_DIR/../..")")")"

docker build ${ROOT_DIR} --file ${ROOT_DIR}/tools/docker/Dockerfile --tag ocrmypdf-watcher:latest
