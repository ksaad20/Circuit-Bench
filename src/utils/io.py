"""
Input/output helper functions.
"""

import json
import pandas as pd
from pathlib import Path


def load_csv(path):
    return pd.read_csv(path)


def save_csv(df, path):
    df.to_csv(path, index=False)


def load_json(path):
    with open(path) as f:
        return json.load(f)


def save_json(data, path):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def ensure_directory(path):
    Path(path).mkdir(parents=True, exist_ok=True)
