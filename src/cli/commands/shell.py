"""
Shell command module for the Circuit Bench CLI.

Provides interactive shell capabilities for Circuit Bench operations.
"""

import code
import sys

import click


@click.command()
@click.option(
    "--banner",
    default="Welcome to the Circuit Bench interactive shell.",
    help="Custom banner for the shell.",
)
def shell(banner: str) -> None:
    """
    Launch an interactive Python shell with the Circuit Bench environment
    pre-loaded.
    """
    click.echo(f"--- {banner} ---")

    # Define the local context for the shell.
    ctx = {
        "sys": sys,
    }

    code.interact(
        banner="Circuit Bench Interactive Mode",
        local=ctx,
    )


if __name__ == "__main__":
    shell()
