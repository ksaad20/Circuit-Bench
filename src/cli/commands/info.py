"""
Information command for the Circuit Bench CLI.
"""

from __future__ import annotations

import platform
import sys

import click


@click.command()
def info() -> None:
    """Display information about the current Circuit Bench installation."""
    click.echo("Circuit Bench")
    click.echo("=" * 40)
    click.echo("Circuit benchmarking and evaluation framework")
    click.echo()
    click.echo(f"Python Version : {sys.version.split()[0]}")
    click.echo(f"Platform       : {platform.system()}")
    click.echo(f"Release        : {platform.release()}")
    click.echo(f"Architecture   : {platform.machine()}")
    click.echo(f"Processor      : {platform.processor() or 'Unknown'}")
    click.echo()
    click.echo("Status         : Ready")
    click.echo("CLI            : Enabled")
    click.echo("Plugins        : Supported")
    click.echo("=" * 40)


if __name__ == "__main__":
    info()
