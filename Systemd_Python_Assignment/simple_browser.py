#!/usr/bin/env python3
"""Example 1: request that the desktop opens a web page."""
import webbrowser


def main():
    opened = webbrowser.open("https://www.python.org", new=2)
    if not opened:
        print("No browser could be launched. Run in a graphical desktop session.",
              flush=True)
        return 1
    print("Browser launch requested: https://www.python.org", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
