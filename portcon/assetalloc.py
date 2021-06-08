"""
Asset Allocation Class:

DESCRIPTION:
    Contains various methods to diversify portfolio weights.

"""

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from modeling import Modeling as mdl

class Asset_Allocation:

    def __init__(self, 
    weights_init=None, 
    sigma = None, 
    asset_bounds=None,
    target_return = None, 
    asset_returns=None, 
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

            # Initialize model object
            model = mdl()

            # Set the optimization constraints
            return_is_target = {
                'type': 'eq',
                'args': (asset_returns,),
                'fun': lambda weights, asset_returns: target_return - model.portfolio_return(asset_returns,weights)
            }
            weights_sum_to_1 = {
                'type':'eq',
                'fun': lambda weights: np.sum(weights)-1
            }

            model = mdl()

            # Call the solver
            return minimize(model.portfolio_risk, weights_init,
            args=(sigma,), method="SLSQP",
            options={'disp': False},
            constraints=(return_is_target, weights_sum_to_1),
            bounds=asset_bounds)