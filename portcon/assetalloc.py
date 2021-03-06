"""
Asset Allocation Class:

DESCRIPTION:
    Contains various methods to diversify portfolio weights.

"""
import numpy as np
import pandas as pd
from scipy.optimize import minimize
from portcon.modeling import Modeling as mdl

class Asset_Allocation:

    def __init__(self, 
    weights_init=None, 
    sigma = None, 
    asset_bounds=None,
    target_return = None, 
    asset_returns=None,
    risk_free_rate=None,
    target_risk=None
    ):
        
        if weights_init is None:
            self.weights_init = []
        else:
            self.weights_init = weights_init
        
        if sigma is None:
            self.sigma = []
        else:
            self.sigma = sigma
        
        if asset_bounds is None:
            self.asset_bounds = []
        else:
            self.asset_bounds = asset_bounds        
        
        if target_return is None:
            self.target_return = []
        else:
            self.target_return = target_return
        
        if asset_returns is None:
            self.asset_returns = []
        else:
            self.asset_returns = asset_returns

        if risk_free_rate is None:
            self.risk_free_rate = []
        else:
            self.risk_free_rate = risk_free_rate

        if target_risk is None:
            self.target_risk = []
        else:
            self.target_risk = target_risk                        

    def minimize_vol(self,
    weights_init = None, 
    sigma = None, 
    asset_bounds = None, 
    target_return = None,
    asset_returns = None):

    # DESCRIPTION:
    #   Computes the portfolio weights of a portfolio targeting some
    #   return by minimizing the volatility.
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
            if sigma is None:
                sigma = self.sigma                
            if asset_bounds is None:
                asset_bounds = self.asset_bounds
            if target_return is None:
                target_return = self.target_return
            if asset_returns is None:
                asset_returns = self.asset_returns                

            # Set the optimization constraints
            return_is_target = {
                'type': 'eq',
                'args': (asset_returns,),
                'fun': lambda weights, asset_returns: target_return - mdl().portfolio_return(asset_returns,weights)
            }
            weights_sum_to_1 = {
                'type':'eq',
                'fun': lambda weights: np.sum(weights)-1
            }

            # Call the solver
            return minimize(mdl().portfolio_risk, weights_init,
            args=(sigma,), method="SLSQP",
            options={'disp': False},
            constraints=(return_is_target, weights_sum_to_1),
            bounds=asset_bounds)

    def msr(self,
    weights_init = None, 
    sigma = None, 
    asset_bounds = None, 
    risk_free_rate = None,
    asset_returns = None):

    # DESCRIPTION:
    #   Computes the portfolio weights of a portfolio targeting some
    #   return by minimizing the volatility.
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
            if sigma is None:
                sigma = self.sigma                
            if asset_bounds is None:
                asset_bounds = self.asset_bounds
            if risk_free_rate is None:
                risk_free_rate = self.risk_free_rate
            if asset_returns is None:
                asset_returns = self.asset_returns                

            # Set the optimization constraints
            weights_sum_to_1 = {
                'type':'eq',
                'fun': lambda weights: np.sum(weights)-1
            }

            # Define the objective function: Maximum Sharpe Ratio
            def sharpe_ratio(weights, risk_free_rate,asset_returns,sigma):                
                return -(mdl().portfolio_return(weights,asset_returns) - risk_free_rate)/mdl().portfolio_risk(weights,sigma)

            # Call the solver
            return minimize(sharpe_ratio, weights_init,
            args=(risk_free_rate,asset_returns,sigma,), method="SLSQP",
            options={'disp': False},
            constraints=(weights_sum_to_1),
            bounds=asset_bounds)

    def gmv(self,
    weights_init = None, 
    sigma = None, 
    asset_bounds = None,
    risk_free_rate = None,
    asset_returns = None
    ):

    # DESCRIPTION:
    #   Computes the portfolio weights of a portfolio targeting some
    #   return by minimizing the volatility.
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
            if sigma is None:
                sigma = self.sigma                
            if asset_bounds is None:
                asset_bounds = self.asset_bounds
            if risk_free_rate is None:
                risk_free_rate = self.risk_free_rate
            if asset_returns is None:
                asset_returns = self.asset_returns                

            # Set the optimization constraints
            weights_sum_to_1 = {
                'type':'eq',
                'fun': lambda weights: np.sum(weights)-1
            }

            # Define the objective function: Maximum Sharpe Ratio
            def port_risk(weights,sigma):                
                return mdl().portfolio_risk(weights,sigma)

            # Call the solver
            return minimize(port_risk, weights_init,
            args=(sigma,), method="SLSQP",
            options={'disp': False},
            constraints=(weights_sum_to_1),
            bounds=asset_bounds)

    def trp(self,
    weights_init = None, 
    sigma = None, 
    asset_bounds = None,
    target_risk = None
    ):

    # DESCRIPTION:
    #   Computes the portfolio weights of a portfolio targeting some
    #   return by minimizing the volatility.
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
            if sigma is None:
                sigma = self.sigma                
            if asset_bounds is None:
                asset_bounds = self.asset_bounds
            if target_risk is None:
                target_risk = self.target_risk   

            # Set the optimization constraints
            weights_sum_to_1 = {
                'type':'eq',
                'fun': lambda weights: np.sum(weights)-1
            }

            # Define the objective function: Maximum Sharpe Ratio
            def msd_risk(weights,target_risk,sigma):
                w_contribs = mdl.risk_contribution([],weights,sigma)                
                return ((w_contribs-target_risk)**2).sum()

            # Call the solver
            return minimize(msd_risk, weights_init,
            args=(target_risk,sigma,), method="SLSQP",
            options={'disp': False},
            constraints=(weights_sum_to_1),
            bounds=asset_bounds)            

    def erp(self,
    weights_init = None, 
    sigma = None, 
    asset_bounds = None
    ):

    # DESCRIPTION:
    #   Computes the portfolio weights of a portfolio targeting some
    #   return by minimizing the volatility.
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
            if sigma is None:
                sigma = self.sigma                
            if asset_bounds is None:
                asset_bounds = self.asset_bounds

            n = sigma.shape[0]
            
            # Call the solver
            return self.trp(weights_init,sigma,asset_bounds,np.repeat(1/n,n))

    def custom(self,
        weights_init=None,
        sigma=None,
        asset_bounds=None,
        alpha=None):

            if weights_init is None:
                weights_init = self.weights_init
            if sigma is None:
                sigma = self.sigma                
            if asset_bounds is None:
                asset_bounds = self.asset_bounds
            if alpha is None:
                alpha = 0.5

            n = sigma.shape[0]
            target_risk = np.repeat(1/n,n)            
            # Set the optimization constraints
            weights_sum_to_1 = {
                'type':'eq',
                'fun': lambda weights: np.sum(weights)-1
            }

            # Define the objective function: Maximum Sharpe Ratio
            def obj(weights,target_risk,sigma,alpha):
                w_contribs = mdl().risk_contribution(weights,sigma)
                port_risk=mdl().portfolio_risk(weights,sigma)
                risk_contribs = ((w_contribs-target_risk)**2).sum()
                return alpha*risk_contribs + (1-alpha)*port_risk

            # Call the solver
            return minimize(obj, weights_init,
            args=(target_risk,sigma,alpha,), method="SLSQP",
            options={'disp': False},
            constraints=(weights_sum_to_1),
            bounds=asset_bounds)     
