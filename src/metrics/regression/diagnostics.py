import statsmodels.api as sm

from statsmodels.stats.diagnostic import (
    het_breuschpagan,
    het_white,
    het_goldfeldquandt
)

from scipy.stats import (
    jarque_bera,
    shapiro,
    anderson
)

def breusch_pagan_test(
        y_true,
        y_pred,
        X):
    """
    Breusch-Pagan test for heteroscedasticity.
    """

    residual = residuals(
        y_true,
        y_pred
    )

    X = sm.add_constant(X)

    statistic, pvalue, fvalue, fpvalue = \
        het_breuschpagan(
            residual,
            X
        )

    return {

        "LM Statistic": float(statistic),

        "LM p-value": float(pvalue),

        "F Statistic": float(fvalue),

        "F p-value": float(fpvalue)

    }


def white_test(
        y_true,
        y_pred,
        X):
    """
    White test for heteroscedasticity.
    """

    residual = residuals(
        y_true,
        y_pred
    )

    X = sm.add_constant(X)

    statistic, pvalue, fvalue, fpvalue = \
        het_white(
            residual,
            X
        )

    return {

        "LM Statistic": float(statistic),

        "LM p-value": float(pvalue),

        "F Statistic": float(fvalue),

        "F p-value": float(fpvalue)

          }

def goldfeld_quandt_test(
        y_true,
        y_pred,
        X):
    """
    Goldfeld-Quandt test.
    """

    residual = residuals(
        y_true,
        y_pred
    )

    statistic, pvalue, _ = \
        het_goldfeldquandt(
            residual,
            X
        )

    return {

        "Statistic": float(statistic),

        "p-value": float(pvalue)

    }


def jarque_bera_residual_test(
        y_true,
        y_pred):
    """
    Jarque-Bera normality test.
    """

    statistic, p = jarque_bera(

        residuals(
            y_true,
            y_pred
        )

    )

    return {

        "Statistic": float(statistic),

        "p-value": float(p)

    }

def shapiro_residual_test(
        y_true,
        y_pred):
    """
    Shapiro-Wilk normality test.
    """

    statistic, p = shapiro(

        residuals(
            y_true,
            y_pred
        )

    )

    return {

        "Statistic": float(statistic),

        "p-value": float(p)

          }

def anderson_residual_test(
        y_true,
        y_pred):
    """
    Anderson-Darling normality test.
    """

    result = anderson(

        residuals(
            y_true,
            y_pred
        )

    )

    return {

        "Statistic":
            float(result.statistic),

        "Critical Values":
            result.critical_values.tolist(),

        "Significance":
            result.significance_level.tolist()

    }

def residual_normality_report(
        y_true,
        y_pred):
    """
    Combined residual normality report.
    """

    return {

        "Shapiro":

        shapiro_residual_test(
            y_true,
            y_pred
        ),

        "Jarque-Bera":

        jarque_bera_residual_test(
            y_true,
            y_pred
        ),

        "Anderson":

        anderson_residual_test(
            y_true,
            y_pred
        )

    }

def residual_autocorrelation(
        y_true,
        y_pred,
        lag=1):
    """
    Residual autocorrelation.
    """

    r = residuals(
        y_true,
        y_pred
    )

    return float(

        np.corrcoef(

            r[:-lag],

            r[lag:]

        )[0, 1]

    )

def residual_rss(
        y_true,
        y_pred):
    """
    Residual Sum of Squares.
    """

    r = residuals(
        y_true,
        y_pred
    )

    return float(

        np.sum(

            r ** 2

        )

    )

def residual_tss(
        y_true):
    """
    Total Sum of Squares.
    """

    y_true = np.asarray(y_true)

    return float(

        np.sum(

            (

                y_true

                -

                np.mean(y_true)

            ) ** 2

        )

    )
