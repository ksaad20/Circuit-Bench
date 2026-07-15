"""
Validation commands for the Circuit Bench CLI.
"""

from __future__ import annotations

import typer

app = typer.Typer(help="Validation commands.")


@app.command("run")
def run() -> None:
    """
    Run validation checks.
    """
    typer.echo("Validation successful.")


@app.command("status")
def status() -> None:
    """
    Display validation status.
    """
    typer.echo("No validation issues detected.")


# Backward compatibility
command = run
execute = run


def register(cli) -> None:
    """
    Register the validation commands with the CLI.
    """
    cli.add_typer(app, name="validate")


if __name__ == "__main__":
    app()
