#!/usr/bin/env python3
"""
Execute the app & restart it when there are source file changes.

This is totally overbuilt. Deal with it.
"""
import sys
import time
import threading
from pathlib import Path

import docker
from pyrate_limiter import BucketFullException, Duration, Limiter, RequestRate
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


DOCKER_CLIENT = docker.from_env()
DOCKER_CONTAINER = None

PATH_TO_PROCESS = str(Path(__name__).parent.absolute())
PATH_TO_OBSERVE = str(Path(__name__).parent.joinpath("src").absolute())

RESTART_COUNT = 1
LIMITER = Limiter(RequestRate(1, Duration.SECOND))


def start_container():
    global DOCKER_CONTAINER

    kill_container()

    image, logs_json = DOCKER_CLIENT.images.build(
        path=PATH_TO_PROCESS, tag="youtube-discord-alert"
    )
    for log in list(logs_json):
        if "stream" in log:
            sys.stdout.write(log["stream"])

    DOCKER_CONTAINER = DOCKER_CLIENT.containers.run(
        image.id, detach=True, auto_remove=True
    )

    container = DOCKER_CONTAINER

    def print_container_logs():
        for log in container.logs(stream=True):
            sys.stdout.write(log.decode("utf-8"))

    threading.Thread(target=print_container_logs).start()


def restart_container(event_path, event_type):
    global RESTART_COUNT
    try:
        LIMITER.try_acquire("process")
    except BucketFullException:
        return
    print(f"\n{event_path} {event_type} - performing restart {RESTART_COUNT}")
    RESTART_COUNT += 1
    start_container()


def kill_container():
    global DOCKER_CONTAINER
    if DOCKER_CONTAINER:
        DOCKER_CONTAINER.kill()


class SrcChangeHandler(PatternMatchingEventHandler):
    def on_modified(self, event):
        restart_container(event.src_path, event.event_type)

    def on_created(self, event):
        restart_container(event.src_path, event.event_type)

    def on_deleted(self, event):
        restart_container(event.src_path, event.event_type)


if __name__ == "__main__":
    start_container()

    event_handler = SrcChangeHandler(patterns=["*.py"])
    observer = Observer()
    observer.schedule(event_handler, path=PATH_TO_OBSERVE, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        kill_container()
        observer.stop()
    finally:
        observer.join()
