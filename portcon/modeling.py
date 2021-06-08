"""
Modelling Class:

DESCRIPTION:
    Contains various methods to model risk and expected returns
    of a collection of assets. It also contains methods to compute
    portfolio risk and return.

"""

import numpy as np
import pandas as pd

class Modeling:

    def __init__(self, returns=None, weights=None, asset_returns=None):
        if returns is None:
            self.returns = []
        else:
            self.returns = returns

        if weights is None:
            self.weights = []
        else:
            self.weights = weights

        if asset_returns is None:
            self.asset_returns = []
        else:
            self.asset_returns = asset_returns

    def covariance(self,returns=None):  
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

            if returns is None:
                return np.cov(self.returns.values)
            else:
                return np.cov(returns.values)
            

    def exp_returns(self, returns=None):
    # DESCRIPTION:
    #   Computes the stationary expected returns vector
    #   of a collection of assets.
    #
    # INPUTS:
    #   returns - pandas dataframe of returns. Index are dates,
    #             rows are returns at any given date, columns
    #             are the returns for any given asset.
    #             
    # OUTPUTS
    #   r - Nx1 numpy array of doubles.
    
        if returns is None:
            return np.average(self.returns.values,axis=0)
        else:
            return np.average(returns.values,axis=0)

    def portfolio_return(self, asset_returns=None, weights=None):
    # DESCRIPTION:
    #   Computes the expected return of a portfolio of assets.
    #
    # INPUTS:
    #   weights - 1D numpy array of doubles between 0 and 1, that 
    #             add up to 1. These are the weights allocated to
    #             each asset in the portfolio.
    #   exp_returns - expected return of each assset in the portfolio
    #             
    # OUTPUTS
    #   rp - scalar double. Expected return of the portfolio
    
        if asset_returns is None:
            asset_returns = self.asset_returns
        if weights is None:
            weights = self.weights
            
        return weights.T @ asset_returns