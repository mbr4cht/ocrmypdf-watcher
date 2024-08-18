# SPDX-FileCopyrightText: 2024 Michael Bracht
# SPDX-License-Identifier: MIT

FROM python:3-slim

RUN apt-get update && apt-get install -y \
  ocrmypdf \
  && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --no-cache-dir -U watchdog


RUN mkdir -p /ocrmypdf && \
    mkdir -p /input && \
    mkdir -p /output

WORKDIR /ocrmypdf

COPY ../src/watcher.py /ocrmypdf/

CMD [ "python", "./watcher.py" ]