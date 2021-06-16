"""
Modelling Class:

DESCRIPTION:
    Contains various methods to model risk and expected returns
    of a collection of assets. It also contains methods to compute
    portfolio risk and return.

"""

import numpy as np
import pandas as pd
from sklearn import linear_model

class Modeling:

    def __init__(
    self, 
    returns=None, 
    weights=None, 
    factors=None,
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

        if factors is None:
            self.factors = []
        else:
            self.factors = factors

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

    def factor_models(self,returns=None,factors=None, predFactors=None):
        if returns is None:
            returns = self.returns
        if factors is None:
            factors=self.factors

        regr = linear_model.LinearRegression()
        regr.fit(factors, returns)
        
        #betas = pd.DataFrame(regr.coef_,index=returns.columns,columns=factors.columns)
        #asset_returns = pd.DataFrame(regr.predict(predFactors).T,index=returns.columns)
        if predFactors is not None:
            return pd.DataFrame(regr.coef_,index=returns.columns,columns=factors.columns), pd.DataFrame(regr.predict(predFactors).T,index=returns.columns)
        else:
            return pd.DataFrame(regr.coef_,index=returns.columns,columns=factors.columns)
    
    def dcc_garch(self):
        print('Hello from dcc_garch')
    # Method under development. Trying install from:
    #   https://pypi.org/project/mgarch/
    #   Project page: https://github.com/srivastavaprashant/mgarch
    #   Sample implementation: https://openbase.com/python/mgarch    
    
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
    #   asset_risks - 2D array of doubles. Variance-covariance matrix
    #                 of the portfolio assets.
    #             
    # OUTPUTS
    #   sigmap - scalar double. Risk of the portfolio
    
        if asset_risks is None:
            asset_risks = self.asset_risks
        if weights is None:
            weights = self.weights
            
        return (weights.T @ asset_risks @ weights)**0.5

    def portfolio_sharpe(self, port_return=None, port_risk=None, risk_free_rate=None):
        
        if port_return is None:
            port_risk = self.port_return
        if port_risk is None:
            port_risk = self.port_risk
        if risk_free_rate is None:
            risk_free_rate = self.risk_free_rate

        return (port_return - risk_free_rate)/port_risk
