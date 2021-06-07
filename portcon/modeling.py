# Modelling Class:
#
# DESCRIPTION:
#   Contains various routines to model risk and expected returns
#   of a collection of assets.

import numpy as np
import pandas as pd

class Modeling:

    def __init__(self, returns):
        self.returns = returns

    def covariance(self):
    # DESCRIPTION:
    #   Computes the stationary variance-covariance matrix
    #   of a collection of assets.
    #
    # INPUTS:
    #   returns - pandas dataframe of returns. Index are dates,
    #             rows are returns at any given date, columns
    #             are the returns for any given asset.
    #             
    # OUTPUTS
    #   sigma - NxN numpy array of doubles.
    #
        return np.cov(self.returns.values)