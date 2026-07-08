"""
classification.py
=================

Classification metrics for CircuitBench.

Author: Asif Kazi
License: Apache 2.0
"""

from __future__ import annotations

import numpy as np

from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    top_k_accuracy_score,
    precision_score,
    recall_score,
    confusion_matrix,
    roc_auc_score,
    average_precision_score,
    precision_recall_curve,
    auc,
    log_loss,
    brier_score_loss,
    hamming_loss,
    zero_one_loss,
    fowlkes_mallows_score,
    coverage_error,
    label_ranking_average_precision_score,
    label_ranking_loss,
)


class ClassificationMetrics:
    """
    Collection of classification evaluation metrics.
    """

    @staticmethod
    def accuracy(y_true, y_pred):
        """
        Standard classification accuracy.
        """
        return float(
            accuracy_score(
                y_true,
                y_pred
            )
        )

    @staticmethod
    def balanced_accuracy(y_true, y_pred):
        """
        Balanced accuracy.
        """
        return float(
            balanced_accuracy_score(
                y_true,
                y_pred
            )
        )

    @staticmethod
    def top_k_accuracy(
        y_true,
        y_score,
        k=5,
        labels=None
    ):
        """
        Top-k classification accuracy.

        Parameters
        ----------
        y_score : ndarray
            Probability estimates.

        labels : list or ndarray
            Class labels.
        """

        return float(

            top_k_accuracy_score(

                y_true,

                y_score,

                k=k,

                labels=labels

            )

        )

    ###################################################
    # Precision
    ###################################################

    @staticmethod
    def precision(
        y_true,
        y_pred
    ):

        return float(

            precision_score(

                y_true,

                y_pred,

                zero_division=0

            )

        )

    @staticmethod
    def precision_macro(
        y_true,
        y_pred
    ):

        return float(

            precision_score(

                y_true,

                y_pred,

                average="macro",

                zero_division=0

            )

        )

    @staticmethod
    def precision_micro(
        y_true,
        y_pred
    ):

        return float(

            precision_score(

                y_true,

                y_pred,

                average="micro",

                zero_division=0

            )

        )

    @staticmethod
    def precision_weighted(
        y_true,
        y_pred
    ):

        return float(

            precision_score(

                y_true,

                y_pred,

                average="weighted",

                zero_division=0

            )

        )

    ###################################################
    # Recall
    ###################################################

    @staticmethod
    def recall(
        y_true,
        y_pred
    ):

        return float(

            recall_score(

                y_true,

                y_pred,

                zero_division=0

            )

        )

    @staticmethod
    def recall_macro(
        y_true,
        y_pred
    ):

        return float(

            recall_score(

                y_true,

                y_pred,

                average="macro",

                zero_division=0

            )

        )

    @staticmethod
    def recall_micro(
        y_true,
        y_pred
    ):

        return float(

            recall_score(

                y_true,

                y_pred,

                average="micro",

                zero_division=0

            )

        )

    @staticmethod
    def recall_weighted(
        y_true,
        y_pred
    ):

        return float(

            recall_score(

                y_true,

                y_pred,

                average="weighted",

                zero_division=0

            )

        )

    ###################################################
    # Confusion Matrix Utilities
    ###################################################

    @staticmethod
    def confusion(
        y_true,
        y_pred
    ):

        return confusion_matrix(
            y_true,
            y_pred
        )

    @staticmethod
    def true_positive(
        y_true,
        y_pred
    ):

        tn, fp, fn, tp = confusion_matrix(
            y_true,
            y_pred
        ).ravel()

        return int(tp)

    @staticmethod
    def true_negative(
        y_true,
        y_pred
    ):

        tn, fp, fn, tp = confusion_matrix(
            y_true,
            y_pred
        ).ravel()

        return int(tn)

    @staticmethod
    def false_positive(
        y_true,
        y_pred
    ):

        tn, fp, fn, tp = confusion_matrix(
            y_true,
            y_pred
        ).ravel()

        return int(fp)

    @staticmethod
    def false_negative(
        y_true,
        y_pred
    ):

        tn, fp, fn, tp = confusion_matrix(
            y_true,
            y_pred
        ).ravel()

        return int(fn)

###################################################
# F-SCORES
###################################################

from sklearn.metrics import (
    f1_score,
    fbeta_score,
    matthews_corrcoef,
    cohen_kappa_score,
    jaccard_score,
)

class ClassificationMetrics(ClassificationMetrics):

    @staticmethod
    def f1(y_true, y_pred):

        return float(
            f1_score(
                y_true,
                y_pred,
                zero_division=0
            )
        )

    @staticmethod
    def f1_macro(y_true, y_pred):

        return float(
            f1_score(
                y_true,
                y_pred,
                average="macro",
                zero_division=0
            )
        )

    @staticmethod
    def f1_micro(y_true, y_pred):

        return float(
            f1_score(
                y_true,
                y_pred,
                average="micro",
                zero_division=0
            )
        )

    @staticmethod
    def f1_weighted(y_true, y_pred):

        return float(
            f1_score(
                y_true,
                y_pred,
                average="weighted",
                zero_division=0
            )
        )

    @staticmethod
    def f_beta(
            y_true,
            y_pred,
            beta=2):

        return float(
            fbeta_score(
                y_true,
                y_pred,
                beta=beta,
                zero_division=0
            )
        )

###################################################
# SENSITIVITY / SPECIFICITY
###################################################

    @staticmethod
    def sensitivity(y_true, y_pred):

        tn, fp, fn, tp = confusion_matrix(
            y_true,
            y_pred
        ).ravel()

        return tp / (tp + fn)

    @staticmethod
    def specificity(y_true, y_pred):

        tn, fp, fn, tp = confusion_matrix(
            y_true,
            y_pred
        ).ravel()

        return tn / (tn + fp)

###################################################
# PREDICTIVE VALUES
###################################################

    @staticmethod
    def positive_predictive_value(
            y_true,
            y_pred):

        tn, fp, fn, tp = confusion_matrix(
            y_true,
            y_pred
        ).ravel()

        return tp / (tp + fp)

    @staticmethod
    def negative_predictive_value(
            y_true,
            y_pred):

        tn, fp, fn, tp = confusion_matrix(
            y_true,
            y_pred
        ).ravel()

        return tn / (tn + fn)

###################################################
# FALSE RATES
###################################################

    @staticmethod
    def false_positive_rate(
            y_true,
            y_pred):

        tn, fp, fn, tp = confusion_matrix(
            y_true,
            y_pred
        ).ravel()

        return fp / (fp + tn)

    @staticmethod
    def false_negative_rate(
            y_true,
            y_pred):

        tn, fp, fn, tp = confusion_matrix(
            y_true,
            y_pred
        ).ravel()

        return fn / (fn + tp)

###################################################
# AGREEMENT METRICS
###################################################

    @staticmethod
    def matthews_correlation(
            y_true,
            y_pred):

        return float(
            matthews_corrcoef(
                y_true,
                y_pred
            )
        )

    @staticmethod
    def cohens_kappa(
            y_true,
            y_pred):

        return float(
            cohen_kappa_score(
                y_true,
                y_pred
            )
        )

###################################################
# SIMILARITY METRICS
###################################################

    @staticmethod
    def jaccard(
            y_true,
            y_pred):

        return float(
            jaccard_score(
                y_true,
                y_pred,
                average="binary"
            )
        )

    @staticmethod
    def jaccard_macro(
            y_true,
            y_pred):

        return float(
            jaccard_score(
                y_true,
                y_pred,
                average="macro"
            )
        )

    @staticmethod
    def dice(
            y_true,
            y_pred):

        f1 = f1_score(
            y_true,
            y_pred
        )

        return float(f1)

###################################################
# BALANCED METRICS
###################################################

    @staticmethod
    def balanced_error_rate(
            y_true,
            y_pred):

        sensitivity = ClassificationMetrics.sensitivity(
            y_true,
            y_pred
        )

        specificity = ClassificationMetrics.specificity(
            y_true,
            y_pred
        )

        return 1 - (
            sensitivity +
            specificity
        ) / 2

    @staticmethod
    def g_mean(
            y_true,
            y_pred):

        sensitivity = ClassificationMetrics.sensitivity(
            y_true,
            y_pred
        )

        specificity = ClassificationMetrics.specificity(
            y_true,
            y_pred
        )

        return np.sqrt(
            sensitivity *
            specificity
        )

    @staticmethod
    def youdens_j(
            y_true,
            y_pred):

        sensitivity = ClassificationMetrics.sensitivity(
            y_true,
            y_pred
        )

        specificity = ClassificationMetrics.specificity(
            y_true,
            y_pred
        )

        return (
            sensitivity +
            specificity -
            1
      )

###################################################
# ROC / AUC METRICS
###################################################

    @staticmethod
    def roc_auc(y_true, y_score):

        return float(
            roc_auc_score(
                y_true,
                y_score
            )
        )

    @staticmethod
    def average_precision(
            y_true,
            y_score):

        return float(
            average_precision_score(
                y_true,
                y_score
            )
        )

    @staticmethod
    def pr_auc(
            y_true,
            y_score):

        precision, recall, _ = precision_recall_curve(
            y_true,
            y_score
        )

        return float(
            auc(
                recall,
                precision
            )
        )

###################################################
# LOSS FUNCTIONS
###################################################

    @staticmethod
    def log_loss(
            y_true,
            probabilities):

        return float(
            log_loss(
                y_true,
                probabilities
            )
        )

    @staticmethod
    def brier_score(
            y_true,
            probabilities):

        return float(
            brier_score_loss(
                y_true,
                probabilities
            )
        )

###################################################
# ERROR METRICS
###################################################

    @staticmethod
    def hamming(
            y_true,
            y_pred):

        return float(
            hamming_loss(
                y_true,
                y_pred
            )
        )

    @staticmethod
    def zero_one(
            y_true,
            y_pred):

        return float(
            zero_one_loss(
                y_true,
                y_pred
            )
        )

###################################################
# CLUSTERING / AGREEMENT
###################################################

    @staticmethod
    def fowlkes_mallows(
            y_true,
            y_pred):

        return float(
            fowlkes_mallows_score(
                y_true,
                y_pred
            )
        )

###################################################
# MULTI-LABEL METRICS
###################################################

    @staticmethod
    def label_ranking_average_precision(
            y_true,
            y_score):

        return float(
            label_ranking_average_precision_score(
                y_true,
                y_score
            )
        )

    @staticmethod
    def label_ranking_loss_metric(
            y_true,
            y_score):

        return float(
            label_ranking_loss(
                y_true,
                y_score
            )
        )

    @staticmethod
    def coverage(
            y_true,
            y_score):

        return float(
            coverage_error(
                y_true,
                y_score
            )
        )

###################################################
# COST METRICS
###################################################

    @staticmethod
    def expected_cost(
            fp,
            fn,
            fp_cost=1.0,
            fn_cost=5.0):

        return fp * fp_cost + fn * fn_cost

###################################################
# LIFT
###################################################

    @staticmethod
    def lift(
            y_true,
            probabilities,
            threshold=0.5):

        predictions = (
            np.asarray(probabilities)
            >= threshold
        ).astype(int)

        positive_rate = np.mean(y_true)

        precision = precision_score(
            y_true,
            predictions,
            zero_division=0
        )

        return precision / positive_rate

###################################################
# GAIN
###################################################

    @staticmethod
    def gain(
            y_true,
            probabilities):

        order = np.argsort(
            probabilities
        )[::-1]

        sorted_true = np.asarray(
            y_true
        )[order]

        cumulative = np.cumsum(
            sorted_true
        )

        return cumulative / cumulative[-1]

###################################################
# KS STATISTIC
###################################################

    @staticmethod
    def ks_statistic(
            positive_scores,
            negative_scores):

        positive_scores = np.sort(
            positive_scores
        )

        negative_scores = np.sort(
            negative_scores
        )

        p = np.searchsorted(
            positive_scores,
            positive_scores,
            side="right"
        ) / len(positive_scores)

        n = np.searchsorted(
            negative_scores,
            positive_scores,
            side="right"
        ) / len(negative_scores)

        return float(
            np.max(
                np.abs(
                    p - n
                )
            )
        )

###################################################
# SUMMARY
###################################################

    @staticmethod
    def summary(
            y_true,
            y_pred):

        return {

            "Accuracy":
            ClassificationMetrics.accuracy(
                y_true,
                y_pred
            ),

            "Balanced Accuracy":
            ClassificationMetrics.balanced_accuracy(
                y_true,
                y_pred
            ),

            "Precision":
            ClassificationMetrics.precision(
                y_true,
                y_pred
            ),

            "Recall":
            ClassificationMetrics.recall(
                y_true,
                y_pred
            ),

            "F1":
            ClassificationMetrics.f1(
                y_true,
                y_pred
            ),

            "MCC":
            ClassificationMetrics.matthews_correlation(
                y_true,
                y_pred
            ),

            "Kappa":
            ClassificationMetrics.cohens_kappa(
                y_true,
                y_pred
            )

        }

###################################################
# KOLMOGOROV-SMIRNOV TEST
###################################################

    @staticmethod
    def ks_statistic(
            positive_scores,
            negative_scores):
        """
        Two-sample Kolmogorov-Smirnov statistic.

        Parameters
        ----------
        positive_scores : array-like
        negative_scores : array-like

        Returns
        -------
        dict
            KS statistic and p-value.
        """

        statistic, p_value = ks_2samp(
            positive_scores,
            negative_scores
        )

        return {
            "KS Statistic": float(statistic),
            "p-value": float(p_value)
        }


###################################################
# CLASS-WISE METRICS
###################################################

    @staticmethod
    def per_class_precision(
            y_true,
            y_pred):

        return precision_score(
            y_true,
            y_pred,
            average=None,
            zero_division=0
        )

    @staticmethod
    def per_class_recall(
            y_true,
            y_pred):

        return recall_score(
            y_true,
            y_pred,
            average=None,
            zero_division=0
        )

    @staticmethod
    def per_class_f1(
            y_true,
            y_pred):

        return f1_score(
            y_true,
            y_pred,
            average=None,
            zero_division=0
        )

###################################################
# MICRO / MACRO UTILITIES
###################################################

    @staticmethod
    def macro_average(values):

        return float(
            np.mean(values)
        )

    @staticmethod
    def micro_average(tp,
                      fp,
                      fn):

        return tp / (
            tp + fp + fn
        )

###################################################
# ERROR COUNTS
###################################################

    @staticmethod
    def total_errors(
            y_true,
            y_pred):

        return int(
            np.sum(
                np.asarray(y_true)
                !=
                np.asarray(y_pred)
            )
        )

    @staticmethod
    def total_correct(
            y_true,
            y_pred):

        return int(
            np.sum(
                np.asarray(y_true)
                ==
                np.asarray(y_pred)
            )
        )

###################################################
# PREVALENCE
###################################################

    @staticmethod
    def prevalence(y_true):

        y_true = np.asarray(y_true)

        return float(
            np.mean(y_true)
        )

###################################################
# PREVALENCE THRESHOLD
###################################################

    @staticmethod
    def prevalence_threshold(
            sensitivity,
            specificity):

        return (
            np.sqrt(
                1 - specificity
            )
        ) / (
            np.sqrt(
                sensitivity
            )
            +
            np.sqrt(
                1 - specificity
            )
        )

###################################################
# DIAGNOSTIC ODDS RATIO
###################################################

    @staticmethod
    def diagnostic_odds_ratio(
            y_true,
            y_pred):

        tn, fp, fn, tp = confusion_matrix(
            y_true,
            y_pred
        ).ravel()

        return (
            tp * tn
        ) / (
            fp * fn
        )

###################################################
# LIKELIHOOD RATIOS
###################################################

    @staticmethod
    def positive_likelihood_ratio(
            y_true,
            y_pred):

        sens = ClassificationMetrics.sensitivity(
            y_true,
            y_pred
        )

        spec = ClassificationMetrics.specificity(
            y_true,
            y_pred
        )

        return sens / (1 - spec)

    @staticmethod
    def negative_likelihood_ratio(
            y_true,
            y_pred):

        sens = ClassificationMetrics.sensitivity(
            y_true,
            y_pred
        )

        spec = ClassificationMetrics.specificity(
            y_true,
            y_pred
        )

        return (
            1 - sens
        ) / spec

###################################################
# FALSE DISCOVERY RATE
###################################################

    @staticmethod
    def false_discovery_rate(
            y_true,
            y_pred):

        ppv = ClassificationMetrics.positive_predictive_value(
            y_true,
            y_pred
        )

        return 1 - ppv

###################################################
# FALSE OMISSION RATE
###################################################

    @staticmethod
    def false_omission_rate(
            y_true,
            y_pred):

        npv = ClassificationMetrics.negative_predictive_value(
            y_true,
            y_pred
        )

        return 1 - npv

###################################################
# THREAT SCORE
###################################################

    @staticmethod
    def threat_score(
            y_true,
            y_pred):

        tn, fp, fn, tp = confusion_matrix(
            y_true,
            y_pred
        ).ravel()

        return tp / (
            tp + fn + fp
        )

###################################################
# MARKEDNESS
###################################################

    @staticmethod
    def markedness(
            y_true,
            y_pred):

        ppv = ClassificationMetrics.positive_predictive_value(
            y_true,
            y_pred
        )

        npv = ClassificationMetrics.negative_predictive_value(
            y_true,
            y_pred
        )

        return ppv + npv - 1

###################################################
# INFORMEDNESS
###################################################

    @staticmethod
    def informedness(
            y_true,
            y_pred):

        sens = ClassificationMetrics.sensitivity(
            y_true,
            y_pred
        )

        spec = ClassificationMetrics.specificity(
            y_true,
            y_pred
        )

        return sens + spec - 1

###################################################
# CRITICAL SUCCESS INDEX
###################################################

    @staticmethod
    def critical_success_index(
            y_true,
            y_pred):

        return ClassificationMetrics.threat_score(
            y_true,
            y_pred
        )

###################################################
# BOOKMAKER INFORMEDNESS
###################################################

    @staticmethod
    def bookmaker_informedness(
            y_true,
            y_pred):

        return ClassificationMetrics.informedness(
            y_true,
            y_pred
        )

###################################################
# DISCRIMINATION POWER
###################################################

    @staticmethod
    def discrimination_power(
            y_true,
            y_pred):

        dor = ClassificationMetrics.diagnostic_odds_ratio(
            y_true,
            y_pred
        )

        return np.log(dor)

              
