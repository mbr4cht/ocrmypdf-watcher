# SPDX-FileCopyrightText: 2024 Michael Bracht
# SPDX-License-Identifier: MIT

import os, time, logging, sys, re
from pathlib import Path

from watchdog.events import RegexMatchingEventHandler
from watchdog.observers.polling import PollingObserver

INPUT_DIRECTORY = os.getenv("OCR_INPUT_DIRECTORY", "/input")
OUTPUT_DIRECTORY = os.getenv("OCR_OUTPUT_DIRECTORY", "/output")
LOG_DIRECTORY = OUTPUT_DIRECTORY + "log/"
LOG_FILE = LOG_DIRECTORY + "log.txt"

REGEXES = [".*.pdf"]

logger = logging.getLogger()


def setup_custom_logger(name):
    formatter = logging.Formatter("%(asctime)s %(levelname)-8s %(message)s")
    handler = logging.FileHandler(LOG_FILE, mode="a")
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)
    return logger


def execute_ocrmypdf(file_path):
    filename = Path(file_path).name
    output_path = OUTPUT_DIRECTORY + "/" + filename
    logger.info("New file: {}".format(file_path))
    logger.info("Attempting to OCRmyPDF to {}".format(output_path))

    if os.path.exists(file_path):
        command = (
            'ocrmypdf --redo-ocr --jobs 3 "' + file_path + '" "' + output_path + '"'
        )

        logger.info("Command to run: {}".format(command))
        result = os.system(command)
        logger.info("Result of OCR: {}".format(result))

        if result == 0:
            logger.info("OCR successful. Deleting source file" + file_path)
            os.remove(file_path)
        if result == 512:
            logger.info("OCR issue with file. Trying again in a few seconds")
            time.sleep(10)
            execute_ocrmypdf(file_path)
    else:
        logger.error("File has been already deleted: {}".format(file_path))


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


def handle_existing_files(dir_path):
    logger.info("Handling existing files in path: {}".format(dir_path))

    for file in os.listdir(dir_path):
        for REGEX in REGEXES:
            re_pattern = re.compile(REGEX)
            if re_pattern.match(file):
                file_path = os.path.join(dir_path, file)
                logger.info("Existing file: {}".format(file_path))
                execute_ocrmypdf(file_path)


class HandleObserverEvent(RegexMatchingEventHandler):
    def on_any_event(self, event):
        if event.event_type in ["created"]:
            logger.info("File event detected: {}".format(event.event_type))
            # Wait for 5 seconds to make sure that all files are fully written before analyzing them
            time.sleep(5)
            execute_ocrmypdf(event.src_path)


if __name__ == "__main__":
    # Create folders if they don't exist yet
    create_folder(INPUT_DIRECTORY)
    create_folder(OUTPUT_DIRECTORY)
    create_folder(LOG_DIRECTORY)

    # Setup logger
    logger = setup_custom_logger("ocrmypdf")

    logger.info("Starting OCRmyPDF watcher with config:")
    logger.info("Input Directory:  {}".format(INPUT_DIRECTORY))
    logger.info("Output Directory: {}".format(OUTPUT_DIRECTORY))

    # Handle existing files first
    handle_existing_files(INPUT_DIRECTORY)

    # Then start observing file changes
    handler = HandleObserverEvent(regexes=REGEXES)
    observer = PollingObserver()
    observer.schedule(handler, INPUT_DIRECTORY, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
