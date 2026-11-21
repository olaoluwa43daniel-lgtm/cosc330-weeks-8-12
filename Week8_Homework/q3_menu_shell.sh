#!/usr/bin/env bash
# Question 3: numbered calculator menu with directory listing.
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)" || exit 1

while true; do
    printf '\n1. Add\n2. Subtract\n3. Multiply\n4. List a directory\n5. Exit\nChoose: '
    IFS= read -r choice || break
    case "$choice" in
        1) make --no-print-directory -C "$script_dir" add ;;
        2) make --no-print-directory -C "$script_dir" subtract ;;
        3) make --no-print-directory -C "$script_dir" multiply ;;
        4)
            printf 'Directory path (blank for current directory): '
            IFS= read -r directory || break
            if [[ -z "$directory" ]]; then directory="."; fi
            if [[ -d "$directory" ]]; then
                ls -la -- "$directory"
            else
                echo "Error: directory does not exist."
            fi
            ;;
        5) echo "Goodbye."; break ;;
        *) echo "Invalid choice. Enter 1 through 5." ;;
    esac
done
