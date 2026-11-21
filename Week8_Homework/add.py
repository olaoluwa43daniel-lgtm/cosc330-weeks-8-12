#!/usr/bin/env python3
"""Read two integers and print their sum."""


def add(first, second):
    return first + second


def main():
    try:
        first = int(input("First integer: "))
        second = int(input("Second integer: "))
    except (ValueError, EOFError):
        print("Error: enter two integers, one per line.")
        return 1
    print(f"Result: {add(first, second)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
