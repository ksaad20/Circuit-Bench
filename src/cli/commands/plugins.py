"""
Plugin management commands for the Circuit Bench CLI.
"""

from __future__ import annotations

import click


@click.group(name="plugins")
def plugins() -> None:
    """Manage Circuit Bench plugins."""


@plugins.command("list")
def list_plugins() -> None:
    """List installed plugins."""
    click.echo("No plugins are currently installed.")


@plugins.command("install")
@click.argument("plugin_name")
def install_plugin(plugin_name: str) -> None:
    """Install a plugin."""
    click.echo(f"Installing plugin: {plugin_name}")


@plugins.command("remove")
@click.argument("plugin_name")
def remove_plugin(plugin_name: str) -> None:
    """Remove an installed plugin."""
    click.echo(f"Removing plugin: {plugin_name}")


@plugins.command("enable")
@click.argument("plugin_name")
def enable_plugin(plugin_name: str) -> None:
    """Enable a plugin."""
    click.echo(f"Enabled plugin: {plugin_name}")


@plugins.command("disable")
@click.argument("plugin_name")
def disable_plugin(plugin_name: str) -> None:
    """Disable a plugin."""
    click.echo(f"Disabled plugin: {plugin_name}")
