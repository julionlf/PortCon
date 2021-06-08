"""
Asset Allocation Class:

DESCRIPTION:
    Contains various methods to diversify portfolio weights.

"""

import numpy as np
import pandas as pd
from scipy.optimize import minimize

class Asset_Allocation:

    def __init__(self, weights_init=None, portfolio_return=None, portfolio_risk=None):
        if weights_init is None:
            self.weights_init = []
        else:
            self.weights_init = weights_init
        if portfolio_return is None:
            self.portfolio_return = []
        else:
            self.portfolio_return = portfolio_return            
        if portfolio_risk is None:
            self.portfolio_risk = []
        else:
            self.portfolio_risk = portfolio_risk

        print("Hi")

    def gmv(self, weights_init = None):
    # DESCRIPTION:
    #   Computes the portfolio weights of a Global Minimum Variance
    #   portfolio.
    #
    # INPUTS:
    #   weights_init - 1D numpy array of doubles between 0 and 1,
    #                  that add up to 1. The entries are the portfolio
    #                  initial guess of portfolio weights.
    #             
    # OUTPUTS
    #   weights - 1D numpy array of doubles between 0 and 1,
    #             that add up to 1. The entries are the portfolio
    #             weights for a global minimum variance portfolio.

            if weights_init is None:
                weights_init = self.weights_init            