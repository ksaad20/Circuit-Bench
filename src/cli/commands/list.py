"""List command."""

from __future__ import annotations


def list_command(args) -> None:
    """List available Circuit Bench resources."""
    print("Listing available resources.")


# Backward compatibility
execute = list_command
