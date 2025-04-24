<div align="center">

# Simple OCR Watcher

[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)
[![REUSE status](https://api.reuse.software/badge/github.com/mbr4cht/ocrmypdf-watcher)](https://api.reuse.software/info/github.com/mbr4cht/ocrmypdf-watcher)

This is a simple OCR (optical character recognition) tool based on [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF/tree/main).

</div>

# How to clone this repository

This repository can be cloned including the tessdata_best submodule via the following command.

```bash
git clone --recurse-submodules https://github.com/mbr4cht/ocrmypdf-watcher.git
```

If you have already cloned the repository, the tessdata_best submodule can be initialized with the following command.

```bash
git submodule update --init --recursive --remote
```

# How to use this tool with Docker

This tool can be used as Docker image using the following convencience scripts.


## Build the Docker image

```bash
# Docker image based on Ubuntu 24.04
sudo .scripts/build_docker_image_ubuntu.sh
# Docker image based on alpine
sudo .scripts/build_docker_image_alpine.sh
```

## Run the Docker container

```bash
sudo .scripts/start_container.sh
```

Adapt [.docker/docker-componse.yml](.docker/docker-componse.yml) to your specific needs. E.g. set the `input` and `output` folders.