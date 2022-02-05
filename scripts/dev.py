#!/usr/bin/env python3
"""
Execute the app & restart it when there are source file changes.

This is totally overbuilt. Deal with it.
"""
import sys
import threading
import time
from pathlib import Path

import docker
from dotenv import dotenv_values
from pyrate_limiter import BucketFullException, Duration, Limiter, RequestRate
from watchdog.events import FileSystemEvent, PatternMatchingEventHandler
from watchdog.observers import Observer


ENVIRONMENT = dotenv_values(".env.local")

DOCKER_CLIENT = docker.from_env()
DOCKER_CONTAINER = None

PATH_TO_PROCESS = str(Path(__name__).parent.absolute())
PATH_TO_OBSERVE = str(Path(__name__).parent.joinpath("src").absolute())

LIMITER = Limiter(RequestRate(1, Duration.SECOND))


def start_container() -> None:
    global DOCKER_CONTAINER

    kill_container()

    image, logs_json = DOCKER_CLIENT.images.build(
        path=PATH_TO_PROCESS, tag="youtube-discord-alert"
    )
    for log in list(logs_json):
        if "stream" in log:
            sys.stdout.write(log["stream"])

    DOCKER_CONTAINER = DOCKER_CLIENT.containers.run(
        image.id,
        detach=True,
        remove=True,
        auto_remove=True,
        environment=ENVIRONMENT,
        volumes=[f"{PATH_TO_PROCESS}/data:/data"],
    )

    container = DOCKER_CONTAINER
    print(f"Created container {container.short_id}")

    def print_container_logs() -> None:
        try:
            for log in container.logs(stream=True):
                sys.stdout.write(log.decode("utf-8"))
        except docker.errors.APIError as err:
            print(f"Reading container logs failed: {err}")

    threading.Thread(target=print_container_logs).start()


def restart_container(event_path: str, event_type: str) -> None:
    try:
        LIMITER.try_acquire("process")
    except BucketFullException:
        return
    print(f"{event_path} {event_type}")
    start_container()


def kill_container() -> None:
    global DOCKER_CONTAINER
    if DOCKER_CONTAINER:
        print(f"Stopping and removing container {DOCKER_CONTAINER.short_id}")
        try:
            DOCKER_CONTAINER.remove(force=True)
        except docker.errors.APIError:
            pass


class SrcChangeHandler(PatternMatchingEventHandler):
    def on_modified(self, event: FileSystemEvent) -> None:
        restart_container(event.src_path, event.event_type)

    def on_created(self, event: FileSystemEvent) -> None:
        restart_container(event.src_path, event.event_type)

    def on_deleted(self, event: FileSystemEvent) -> None:
        restart_container(event.src_path, event.event_type)


if __name__ == "__main__":
    print(f"Using environment: {dict(ENVIRONMENT)}")
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
