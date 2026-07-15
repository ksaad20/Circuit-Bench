"""
Export commands for the Circuit Bench CLI.
"""

from __future__ import annotations

import typer

app = typer.Typer(help="Export commands.")


@app.command("report")
def report() -> None:
    """
    Export the benchmark report.
    """
    typer.echo("Report exported.")


# Backward compatibility
command = report
execute = report


def register(cli) -> None:
    """
    Register the export commands with the CLI.
    """
    cli.add_typer(app, name="export")


if __name__ == "__main__":
    app()
