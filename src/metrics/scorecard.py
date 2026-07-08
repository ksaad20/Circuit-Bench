"""
Generate benchmark scorecards.
"""

from __future__ import annotations

import numpy as np

from .aggregation import arithmetic_mean
from .thresholds import grade


def overall_score(metrics: dict):

    return arithmetic_mean(list(metrics.values()))


def generate_scorecard(model_name: str,
                       metrics: dict):

    score = overall_score(metrics)

    return {

        "Model": model_name,

        "Overall Score": round(score, 4),

        "Grade": grade(score),

        "Metrics": metrics

    }


def compare_scorecards(scorecards: list):

    return sorted(

        scorecards,

        key=lambda x: x["Overall Score"],

        reverse=True

    )


def export_dataframe(scorecards):

    import pandas as pd

    return pd.DataFrame(scorecards)


def print_scorecard(scorecard):

    print("=" * 60)

    print(scorecard["Model"])

    print("=" * 60)

    print()

    print(f'Overall Score : {scorecard["Overall Score"]:.4f}')

    print(f'Grade         : {scorecard["Grade"]}')

    print()

    for k, v in scorecard["Metrics"].items():

        print(f"{k:<20} {v:.5f}")

    print("=" * 60)
