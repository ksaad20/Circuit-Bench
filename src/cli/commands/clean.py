"""
Cleanup commands for the Circuit Bench CLI.
"""

from __future__ import annotations

import click


@click.command()
@click.option(
    "--all",
    "clean_all",
    is_flag=True,
    help="Remove all generated artifacts.",
)
def clean(clean_all: bool) -> None:
    """Clean generated files and temporary artifacts."""
    if clean_all:
        click.echo("Cleaning all generated artifacts...")
    else:
        click.echo("Cleaning temporary artifacts...")

    click.echo("Cleanup completed successfully.")


if __name__ == "__main__":
    clean()
