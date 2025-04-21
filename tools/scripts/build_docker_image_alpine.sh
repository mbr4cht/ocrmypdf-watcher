# SPDX-FileCopyrightText: 2024 Michael Bracht
# SPDX-License-Identifier: MIT
#!/bin/bash

SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
ROOT_DIR="$(realpath "$(dirname "$(readlink -f "$0SCRIPT_DIR/../..")")")"

docker build --file ${ROOT_DIR}/tools/docker/Dockerfile_alpine --tag ocrmypdf-watcher:alpine-latest ${ROOT_DIR}
