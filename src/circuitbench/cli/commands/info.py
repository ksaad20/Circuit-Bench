"""
Information commands for the Circuit Bench CLI.
"""

from __future__ import annotations

import typer

app = typer.Typer(help="Information commands.")


@app.command("show")
def show() -> None:
    """
    Display information about Circuit-Bench.
    """
    typer.echo("Circuit-Bench information.")


# Backward compatibility
command = show
execute = show


def register(cli) -> None:
    """
    Register the information commands with the CLI.
    """
    cli.add_typer(app, name="info")


if __name__ == "__main__":
    app()
