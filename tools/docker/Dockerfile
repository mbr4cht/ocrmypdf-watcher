# SPDX-FileCopyrightText: 2024-2025 Michael Bracht
# SPDX-License-Identifier: MIT

FROM ubuntu:24.04

# Create ocrmypdf directory
ENV OCRMYPDF_DIR=/ocrmypdf
RUN mkdir -p ${OCRMYPDF_DIR}
WORKDIR ${OCRMYPDF_DIR}

# Install ocrmypdf and German language pack
RUN apt-get update && \
    apt-get install -y \
        python3 \
        python3-watchdog\
        python3-pip \
        python-is-python3 \
        ocrmypdf \
        tesseract-ocr-deu && \
    rm -rf /var/lib/apt/lists/*

# Copy tessdata_best training data
RUN  rm -rf /usr/share/tesseract-ocr/5/tessdata
COPY external/tessdata_best /usr/share/tesseract-ocr/5/tessdata

# Install watchdog and watcher Python script
RUN python -m pip install --break-system-packages --user --upgrade ocrmypdf
COPY watcher.py ./

CMD [ "python", "./watcher.py" ]