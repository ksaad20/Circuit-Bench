"""
Prompt utilities.
"""

from __future__ import annotations


def confirm(message: str) -> bool:
    answer = input(f"{message} [y/N]: ").strip().lower()
    return answer in ("y", "yes")


def ask(message: str) -> str:
    return input(f"{message}: ").strip()


def choose(options):
    print()

    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("\nChoice: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
        except ValueError:
            pass

        print("Invalid selection.")
