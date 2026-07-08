"""
Validation utilities for CircuitBench.
"""

from pathlib import Path
import pandas as pd


def validate_dataset(df: pd.DataFrame):
    """
    Check whether a dataset is valid.
    """
    if df.empty:
        raise ValueError("Dataset is empty.")

    if df.isnull().sum().sum() > 0:
        raise ValueError("Dataset contains missing values.")

    return True


def validate_columns(df, required_columns):

    missing = [c for c in required_columns if c not in df.columns]

    if missing:
        raise ValueError(
            f"Missing columns: {missing}"
        )

    return True


def validate_file(filepath):

    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError(filepath)

    return True


def validate_numeric(df):

    non_numeric = df.select_dtypes(exclude="number")

    if len(non_numeric.columns):

        raise ValueError(
            f"Non-numeric columns detected: {list(non_numeric.columns)}"
        )

    return True


def validate_train_test(X_train,
                        X_test):

    if len(X_train) == 0:
        raise ValueError("Training set is empty.")

    if len(X_test) == 0:
        raise ValueError("Test set is empty.")

    return True
