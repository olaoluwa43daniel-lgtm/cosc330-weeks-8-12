#!/usr/bin/env bash
# Question 2: repeat add, subtract, or multiply until exit.
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)" || exit 1

while true; do
    printf '\nType add, subtract, multiply, or exit: '
    IFS= read -r choice || break
    case "$choice" in
        add|subtract|multiply)
            make --no-print-directory -C "$script_dir" "$choice"
            ;;
        exit) echo "Goodbye."; break ;;
        *) echo "Invalid choice." ;;
    esac
done
