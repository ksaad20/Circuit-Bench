from __future__ import annotations

import typer

app = typer.Typer(help="Configuration commands.")


@app.command("show")
def show() -> None:
    typer.echo("Configuration loaded.")


@app.command("reset")
def reset() -> None:
    typer.echo("Configuration reset.")


if __name__ == "__main__":
    app()
