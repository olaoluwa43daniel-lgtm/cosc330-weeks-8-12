#!/usr/bin/env python3
"""Example 2: a background clock with systemd readiness and status messages."""
from datetime import datetime
import os
import signal
import socket
import threading

stop_event = threading.Event()


def notify(message):
    """Send newline-separated state fields to systemd, if available."""
    address = os.environ.get("NOTIFY_SOCKET")
    if not address:
        return
    if address.startswith("@"):
        address = "\0" + address[1:]
    with socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM) as connection:
        connection.connect(address)
        connection.sendall(message.encode("utf-8"))


def stop_service(signum, frame):
    stop_event.set()


def main():
    signal.signal(signal.SIGTERM, stop_service)
    signal.signal(signal.SIGINT, stop_service)
    notify("READY=1\nSTATUS=Clock initialized")
    print("Clock service started.", flush=True)
    try:
        while not stop_event.is_set():
            current_time = datetime.now().isoformat(timespec="seconds")
            print("Current time: " + current_time, flush=True)
            notify("STATUS=Last update: " + current_time)
            stop_event.wait(5)
    finally:
        notify("STOPPING=1\nSTATUS=Clock stopping")
        print("Clock service stopped.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
