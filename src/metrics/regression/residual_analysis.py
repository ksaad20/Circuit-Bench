from scipy.stats import skew, kurtosis
from statsmodels.stats.stattools import durbin_watson

def residuals(
        y_true,
        y_pred):
    """
    Compute residuals.
    """

    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    return y_true - y_pred

def absolute_residuals(
        y_true,
        y_pred):
    """
    Absolute residuals.
    """

    return np.abs(

        residuals(

            y_true,

            y_pred

        )

    )


def squared_residuals(
        y_true,
        y_pred):
    """
    Squared residuals.
    """

    return residuals(

        y_true,

        y_pred

    ) ** 2


def residual_mean(
        y_true,
        y_pred):
    """
    Mean residual.
    """

    return float(

        np.mean(

            residuals(

                y_true,

                y_pred

            )

        )

    )


def residual_variance(
        y_true,
        y_pred):
    """
    Residual variance.
    """

    return float(

        np.var(

            residuals(

                y_true,

                y_pred

            ),

            ddof=1

        )

    )


def residual_standard_deviation(
        y_true,
        y_pred):
    """
    Residual standard deviation.
    """

    return float(

        np.std(

            residuals(

                y_true,

                y_pred

            ),

            ddof=1

        )

    )


def standardized_residuals(
        y_true,
        y_pred):
    """
    Standardized residuals.
    """

    r = residuals(

        y_true,

        y_pred

    )

    return (

        r -

        np.mean(r)

    ) / np.std(

        r,

        ddof=1

    )



def studentized_residuals(
        y_true,
        y_pred):
    """
    Approximate studentized residuals.
    """

    r = residuals(

        y_true,

        y_pred

    )

    mse = np.mean(

        r ** 2

    )

    return r / np.sqrt(mse)


def residual_skewness(
        y_true,
        y_pred):
    """
    Residual skewness.
    """

    return float(

        skew(

            residuals(

                y_true,

                y_pred

            )

        )

    )


def residual_kurtosis(
        y_true,
        y_pred):
    """
    Residual kurtosis.
    """

    return float(

        kurtosis(

            residuals(

                y_true,

                y_pred

            )

        )

    )


def durbin_watson_statistic(
        y_true,
        y_pred):
    """
    Durbin-Watson statistic.
    """

    return float(

        durbin_watson(

            residuals(

                y_true,

                y_pred

            )

        )

    )


def residual_range(
        y_true,
        y_pred):
    """
    Range of residuals.
    """

    r = residuals(

        y_true,

        y_pred

    )

    return float(

        np.max(r)

        -

        np.min(r)

    )


def residual_median(
        y_true,
        y_pred):
    """
    Median residual.
    """

    return float(

        np.median(

            residuals(

                y_true,

                y_pred

            )

        )

    )


def residual_iqr(
        y_true,
        y_pred):
    """
    Interquartile range of residuals.
    """

    r = residuals(

        y_true,

        y_pred

    )

    q1 = np.percentile(r, 25)

    q3 = np.percentile(r, 75)

    return float(

        q3 - q1

    )


def residual_summary(
        y_true,
        y_pred):
    """
    Summary statistics of residuals.
    """

    return {

        "Mean":

        residual_mean(

            y_true,

            y_pred

        ),

        "Median":

        residual_median(

            y_true,

            y_pred

        ),

        "Variance":

        residual_variance(

            y_true,

            y_pred

        ),

        "Std":

        residual_standard_deviation(

            y_true,

            y_pred

        ),

        "Skewness":

        residual_skewness(

            y_true,

            y_pred

        ),

        "Kurtosis":

        residual_kurtosis(

            y_true,

            y_pred

        ),

        "Durbin-Watson":

        durbin_watson_statistic(

            y_true,

            y_pred

        )

    }


