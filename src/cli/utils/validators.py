"""
Validation utilities.
"""

from __future__ import annotations

from pathlib import Path


def validate_file(path: str | Path) -> bool:
    return Path(path).is_file()


def validate_directory(path: str | Path) -> bool:
    return Path(path).is_dir()


def validate_yaml(path: str | Path) -> bool:
    return str(path).endswith((".yaml", ".yml"))


def validate_json(path: str | Path) -> bool:
    return str(path).endswith(".json")


def validate_python(path: str | Path) -> bool:
    return str(path).endswith(".py")
