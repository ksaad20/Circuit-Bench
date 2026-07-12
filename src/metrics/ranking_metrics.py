"""
CircuitBench Ranking Metrics
============================

Ranking and retrieval metrics.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import numpy as np


class RankingMetrics:
    """
    Ranking evaluation metrics.
    """

    @staticmethod
    def precision_at_k(
        y_true,
        y_pred,
        k=10,
    ):
        """
        Precision@K
        """

        y_true = np.asarray(y_true)[:k]
        y_pred = np.asarray(y_pred)[:k]

        return float(
            np.sum(y_true == y_pred)
            / k
        )

    @staticmethod
    def recall_at_k(
        y_true,
        y_pred,
        k=10,
    ):
        """
        Recall@K
        """

        y_true = np.asarray(y_true)
        y_pred = np.asarray(y_pred[:k])

        relevant = np.isin(
            y_pred,
            y_true,
        )

        if len(y_true) == 0:
            return 0.0

        return float(
            np.sum(relevant)
            / len(y_true)
        )

    @staticmethod
    def hit_rate(
        y_true,
        y_pred,
        k=10,
    ):
        """
        Hit@K
        """

        y_true = set(y_true)

        y_pred = set(y_pred[:k])

        return float(
            len(
                y_true.intersection(
                    y_pred
                )
            ) > 0
        )

    @staticmethod
    def reciprocal_rank(
        y_true,
        y_pred,
    ):
        """
        Reciprocal Rank
        """

        for rank, item in enumerate(
            y_pred,
            start=1,
        ):

            if item in y_true:

                return 1.0 / rank

        return 0.0

    @classmethod
    def basic_report(
        cls,
        y_true,
        y_pred,
        k=10,
    ):

        return {

            "Precision@K":
                cls.precision_at_k(
                    y_true,
                    y_pred,
                    k,
                ),

            "Recall@K":
                cls.recall_at_k(
                    y_true,
                    y_pred,
                    k,
                ),

            "HitRate":
                cls.hit_rate(
                    y_true,
                    y_pred,
                    k,
                ),

            "ReciprocalRank":
                cls.reciprocal_rank(
                    y_true,
                    y_pred,
                ),

        }


__all__ = [
    "RankingMetrics",
]

    @staticmethod
    def average_precision(
        y_true,
        y_pred,
    ):
        """
        Average Precision (AP)
        """

        y_true = set(y_true)

        if len(y_true) == 0:
            return 0.0

        score = 0.0
        hits = 0

        for i, item in enumerate(y_pred, start=1):

            if item in y_true:

                hits += 1

                score += hits / i

        return float(score / len(y_true))

    @staticmethod
    def mean_average_precision(
        truth_lists,
        prediction_lists,
    ):
        """
        Mean Average Precision (MAP)
        """

        scores = [

            RankingMetrics.average_precision(
                truth,
                pred,
            )

            for truth, pred in zip(
                truth_lists,
                prediction_lists,
            )

        ]

        return float(np.mean(scores))

    @staticmethod
    def dcg(
        relevance,
    ):
        """
        Discounted Cumulative Gain.
        """

        relevance = np.asarray(
            relevance,
            dtype=float,
        )

        if relevance.size == 0:
            return 0.0

        discounts = np.log2(
            np.arange(
                2,
                relevance.size + 2,
            )
        )

        return float(
            np.sum(
                relevance / discounts
            )
        )

    @staticmethod
    def ndcg(
        relevance,
    ):
        """
        Normalized Discounted Cumulative Gain.
        """

        relevance = np.asarray(
            relevance,
            dtype=float,
        )

        ideal = np.sort(
            relevance
        )[::-1]

        ideal_dcg = RankingMetrics.dcg(
            ideal,
        )

        if ideal_dcg == 0:
            return 0.0

        return float(
            RankingMetrics.dcg(
                relevance,
            )
            /
            ideal_dcg
        )

    @staticmethod
    def mean_reciprocal_rank(
        truth_lists,
        prediction_lists,
    ):
        """
        Mean Reciprocal Rank (MRR)
        """

        scores = [

            RankingMetrics.reciprocal_rank(
                truth,
                pred,
            )

            for truth, pred in zip(
                truth_lists,
                prediction_lists,
            )

        ]

        return float(
            np.mean(scores)
        )

