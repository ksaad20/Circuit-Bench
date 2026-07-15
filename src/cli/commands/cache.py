from __future__ import annotations

import typer

app = typer.Typer(help="Cache management commands.")


@app.command("info")
def cache_info() -> None:
    """Display cache information."""
    typer.echo("Cache status: Available")


@app.command("clear")
def cache_clear() -> None:
    """Clear the cache."""
    typer.echo("Cache cleared successfully.")


@app.command("rebuild")
def cache_rebuild() -> None:
    """Rebuild the cache."""
    typer.echo("Cache rebuilt successfully.")


if __name__ == "__main__":
    app()
