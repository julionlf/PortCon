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

    def __init__(
    self, returns=None, 
    weights=None, 
    asset_returns=None, 
    asset_risks=None):

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

        if asset_risks is None:
            self.asset_risks = []
        else:
            self.asset_risks = asset_risks

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
                return self.returns.cov()
            else:
                return returns.cov()
            

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
            return self.returns.mean()
        else:
            return returns.mean()

    def portfolio_return(self, weights=None, asset_returns=None):
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

    def portfolio_risk(self, weights=None, asset_risks=None):
    # DESCRIPTION:
    #   Computes the risk of a portfolio of assets.
    #
    # INPUTS:
    #   weights - 1D numpy array of doubles between 0 and 1, that 
    #             add up to 1. These are the weights allocated to
    #             each asset in the portfolio.
    #   asset_risks - 2D array od doubles. Variance-covariance matrix
    #                 of the portfolio assets.
    #             
    # OUTPUTS
    #   sigmap - scalar double. Risk of the portfolio
    
        if asset_risks is None:
            asset_risks = self.asset_risks
        if weights is None:
            weights = self.weights
            
        return (weights.T @ asset_risks @ weights)**0.5