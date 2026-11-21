#!/usr/bin/env bash
# Question 1: repeat addition until the user exits.
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)" || exit 1

while true; do
    printf '\nType add or exit: '
    IFS= read -r choice || break
    case "$choice" in
        add) make --no-print-directory -C "$script_dir" add ;;
        exit) echo "Goodbye."; break ;;
        *) echo "Invalid choice. Type add or exit." ;;
    esac
done
