from __future__ import annotations

import subprocess
import sys


def test_cli_runs() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "circuitbench.cli.main"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
