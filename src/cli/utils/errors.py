"""
CLI exception classes.
"""


class CLIError(Exception):
    """Base CLI error."""


class ValidationError(CLIError):
    """Configuration validation error."""


class BenchmarkError(CLIError):
    """Benchmark execution error."""


class DatasetError(CLIError):
    """Dataset related error."""


class ConfigurationError(CLIError):
    """Configuration loading error."""
