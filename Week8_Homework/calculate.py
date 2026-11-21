#!/usr/bin/env python3
"""Read two integers and subtract or multiply them."""
import sys


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ("subtract", "multiply"):
        print("Usage: python3 calculate.py subtract|multiply")
        return 1
    try:
        first = int(input("First integer: "))
        second = int(input("Second integer: "))
    except (ValueError, EOFError):
        print("Error: enter two integers, one per line.")
        return 1
    if sys.argv[1] == "subtract":
        result = first - second
    else:
        result = first * second
    print(f"Result: {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
