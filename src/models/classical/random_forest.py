"""
CircuitBench Random Forest Regressor
====================================

Production-quality wrapper around sklearn RandomForestRegressor.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import numpy as np
from sklearn.ensemble import RandomForestRegressor

from src.models.classical.sklearn_model import SklearnModel
from src.models.registry import register_model


@register_model(
    category="classical",
    task="regression",
    framework="scikit-learn",
)
class RandomForestRegressionModel(SklearnModel):
    """
    Random Forest Regression.

    Supports feature importance, out-of-bag scoring,
    and parallel execution.
    """

    def __init__(
        self,
        n_estimators: int = 100,
        criterion: str = "squared_error",
        max_depth=None,
        min_samples_split: int = 2,
        min_samples_leaf: int = 1,
        max_features: str | float = "sqrt",
        bootstrap: bool = True,
        oob_score: bool = False,
        n_jobs: int = -1,
        random_state: int = 42,
    ):

        estimator = RandomForestRegressor(
            n_estimators=n_estimators,
            criterion=criterion,
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            min_samples_leaf=min_samples_leaf,
            max_features=max_features,
            bootstrap=bootstrap,
            oob_score=oob_score,
            n_jobs=n_jobs,
            random_state=random_state,
        )

        super().__init__(
            estimator=estimator,
            name="RandomForestRegression",
            random_state=random_state,
        )

    # --------------------------------------------------

    def fit(self, X, y):

        super().fit(X, y)

        self.metadata.update(
            {
                "n_estimators": self.model.n_estimators,
                "criterion": self.model.criterion,
                "max_depth": self.model.max_depth,
                "bootstrap": self.model.bootstrap,
                "max_features": self.model.max_features,
            }
        )

        if getattr(self.model, "oob_score", False):
            self.metadata["oob_score"] = getattr(
                self.model,
                "oob_score_",
                None,
            )

        return self

    # --------------------------------------------------

    def feature_importance(self):

        importance = np.asarray(
            self.model.feature_importances_,
            dtype=float,
        )

        total = importance.sum()

        if total == 0:
            return importance

        return importance / total

    # --------------------------------------------------

    def n_trees(self):

        return len(self.model.estimators_)

    # --------------------------------------------------

    def summary(self):

        print("=" * 70)
        print("CircuitBench Random Forest")
        print("=" * 70)

        for key, value in self.metadata.items():
            print(f"{key:20}: {value}")

        print(f"Trees               : {self.n_trees()}")
        print("=" * 70)

    # --------------------------------------------------

    def __repr__(self):

        return (
            "RandomForestRegressionModel("
            f"trees={self.model.n_estimators}, "
            f"fitted={self.is_fitted})"
        )


__all__ = [
    "RandomForestRegressionModel",
]
