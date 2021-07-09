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

    def __init__(self, returns=None, weights=None, factors=None, asset_returns=None, sigma=None):

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

        if sigma is None:
            self.sigma = []
        else:
            self.sigma = sigma            

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
    
    def dcc_garch(self,
        returns=None,
        periods=1,
        arma_alpha=0,arma_beta=0,
        garch_alpha=1,garch_beta=1,
        dcc_garch_alpha=1,dcc_garch_beta=1
    ):

        if returns is None:
            returns = self.returns

        # Prep interface with R
        import rpy2.robjects as robjects
        from rpy2.robjects import pandas2ri
        pandas2ri.activate()

        # Defining the R script and loading the instance in Python
        r = robjects.r
        r['source']('portcon\\dcc_garch.R')

        # Load DCC-GARCH function
        dcc_garch_function = robjects.globalenv["dcc_garch"]

        # Convert pandas returns df to R df
        returns_r = pandas2ri.py2rpy(returns)

        # Estimate covariance matrix using DCC-Garch
        sigma = dcc_garch_function(returns_r,periods,
        arma_alpha,arma_beta,               # ARMA model memory and stochastic parameters
        garch_alpha,garch_beta,             # GARCH model memory and stochastic parameters
        dcc_garch_alpha,dcc_garch_beta)     # DCC model memory and stochastic parameters

        # Relabel the columns and indeces
        sigma.columns = returns.columns.values
        sigma.index = returns.columns.values

        return sigma
    
    def risk_contribution(self,weights=None,sigma=None):
        if weights is None:
            weights = self.weights
        if sigma is None:
            sigma = self.sigma

        #port_risk = self.portfolio_risk(weights,sigma)
        port_risk = weights.T @ sigma @ weights
        marginal_contribution = sigma @ weights
        return np.multiply(marginal_contribution,weights)/(port_risk)

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

    def portfolio_risk(self, weights=None, sigma=None):
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
    
        if weights is None:
            weights = self.weights        
        if sigma is None:
            sigma = self.sigma
            
        return (weights.T @ sigma @ weights)**0.5

    def portfolio_sharpe(self, port_return=None, port_risk=None, risk_free_rate=None):
        
        if port_return is None:
            port_risk = self.port_return
        if port_risk is None:
            port_risk = self.port_risk
        if risk_free_rate is None:
            risk_free_rate = self.risk_free_rate

        return (port_return - risk_free_rate)/port_risk
