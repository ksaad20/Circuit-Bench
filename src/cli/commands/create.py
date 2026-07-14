"""Create benchmark command."""

from __future__ import annotations

import typer

app = typer.Typer(help="Create a new benchmark.")


@app.command()
def main(
    name: str = typer.Argument(..., help="Benchmark name"),
) -> None:
    """Create a benchmark."""
    typer.echo(f"Creating benchmark: {name}")
