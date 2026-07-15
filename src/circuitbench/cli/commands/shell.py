"""
Interactive shell commands for the Circuit Bench CLI.
"""

from __future__ import annotations

import typer

app = typer.Typer(help="Interactive shell commands.")


@app.command("start")
def start() -> None:
    """
    Start the interactive Circuit Bench shell.
    """
    typer.echo("Interactive shell started.")


@app.command("stop")
def stop() -> None:
    """
    Stop the interactive shell.
    """
    typer.echo("Interactive shell stopped.")


@app.command("status")
def status() -> None:
    """
    Display the shell status.
    """
    typer.echo("Interactive shell is ready.")


# Backward compatibility
command = start
execute = start


def register(cli) -> None:
    """
    Register the shell commands with the CLI.
    """
    cli.add_typer(app, name="shell")


if __name__ == "__main__":
    app()
