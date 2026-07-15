from __future__ import annotations

import typer

app = typer.Typer(help="Information commands.")


@app.command("show")
def show() -> None:
    typer.echo("Circuit-Bench information.")


if __name__ == "__main__":
    app()
