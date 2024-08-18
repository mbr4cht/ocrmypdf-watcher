[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)
[![REUSE status](https://api.reuse.software/badge/github.com/mbr4cht/ocrmypdf-watcher)](https://api.reuse.software/info/github.com/mbr4cht/ocrmypdf-watcher)

# Simple OCR Watcher

This is a simple OCR (optical character recognition) tool based on [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF/tree/main).

# How to use this tool with Docker

This tool can be used as Docker image as in the following `docker-compose.yml`.

## Build the Docker image

```bash
sudo .scripts/build_docker_image.sh
```

## Run the Docker container

```bash
sudo .scripts/start_container.sh
```

Adapt [.docker/docker-componse.yml](.docker/docker-componse.yml) to your specific needs. E.g. set the `input` and `output` folders.