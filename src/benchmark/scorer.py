"""
Composite scoring.
"""

class CompositeScore:

    def __init__(self,
                 rmse_weight=0.35,
                 mae_weight=0.25,
                 r2_weight=0.40):

        self.rmse_weight = rmse_weight
        self.mae_weight = mae_weight
        self.r2_weight = r2_weight

    def score(self, rmse, mae, r2):

        return (
            self.rmse_weight*(1/(1+rmse))
            +
            self.mae_weight*(1/(1+mae))
            +
            self.r2_weight*r2
        )
