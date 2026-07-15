from __future__ import annotations

import typer

from src.cli.commands.create import app as create_app
from src.cli.commands.doctor import app as doctor_app
from src.cli.commands.version import app as version_app
from src.cli.commands.benchmarks import app as benchmarks_app
from src.cli.commands.cache import app as cache_app
from src.cli.commands.clean import app as clean_app
from src.cli.commands.config import app as config_app
from src.cli.commands.datasets import app as datasets_app
from src.cli.commands.evaluate import app as evaluate_app
from src.cli.commands.export import app as export_app
from src.cli.commands.info import app as info_app
from src.cli.commands.leaderboard import app as leaderboard_app
from src.cli.commands.list import app as list_app
from src.cli.commands.plugins import app as plugins_app
from src.cli.commands.report import app as report_app
from src.cli.commands.run import app as run_app
from src.cli.commands.shell import app as shell_app
from src.cli.commands.stats import app as stats_app
from src.cli.commands.validate import app as validate_app

app = typer.Typer(
    name="circuitbench",
    help="Circuit-Bench command line interface.",
    no_args_is_help=False,
)

app.add_typer(create_app, name="create")
app.add_typer(version_app, name="version")
app.add_typer(doctor_app, name="doctor")
app.add_typer(benchmarks_app, name="benchmarks")
app.add_typer(cache_app, name="cache")
app.add_typer(clean_app, name="clean")
app.add_typer(config_app, name="config")
app.add_typer(datasets_app, name="datasets")
app.add_typer(evaluate_app, name="evaluate")
app.add_typer(export_app, name="export")
app.add_typer(info_app, name="info")
app.add_typer(leaderboard_app, name="leaderboard")
app.add_typer(list_app, name="list")
app.add_typer(plugins_app, name="plugins")
app.add_typer(report_app, name="report")
app.add_typer(run_app, name="run")
app.add_typer(shell_app, name="shell")
app.add_typer(stats_app, name="stats")
app.add_typer(validate_app, name="validate")


@app.callback(invoke_without_command=True)
def callback() -> None:
    """CLI callback."""
    return


def main() -> None:
    """Run the CLI."""
    app()


if __name__ == "__main__":
    main()
