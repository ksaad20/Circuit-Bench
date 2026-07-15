"""
Create benchmark command for the Circuit Bench CLI.
"""

from __future__ import annotations

import typer

app = typer.Typer(help="Create a new benchmark.")


@app.command("benchmark")
def main(
    name: str = typer.Argument(..., help="Benchmark name"),
) -> None:
    """
    Create a new benchmark.
    """
    typer.echo(f"Creating benchmark: {name}")


# Backward compatibility
command = main
execute = main


def register(cli) -> None:
    """
    Register the create commands with the CLI.
    """
    cli.add_typer(app, name="create")


if __name__ == "__main__":
    app()
