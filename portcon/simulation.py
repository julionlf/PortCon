# Import libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from portcon.modeling import Modeling as mdl
from portcon.assetalloc import Asset_Allocation as aa

class Simulation:

    def __init__(self,weights=None,
    returns=None,
    principal=None,
    target_returns=None,
    weights_init = None, 
    sigma = None, 
    asset_bounds = None, 
    risk_free_rate = None,
    asset_returns = None
    ):

        if weights is None:
            self.weights = []
        else:
            self.weights = weights
        
        if returns is None:
            self.returns = []
        else:
            self.returns = returns
        
        if principal is None:
            self.principal = []
        else:
            self.principal = principal
        
        if target_returns is None:
            self.target_returns = np.arange(0,0.2,0.01)
        else:
            self.target_returns = target_returns
        
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
        
        if risk_free_rate is None:
            self.risk_free_rate = []
        else:
            self.risk_free_rate = risk_free_rate                                                                    
        
        if asset_returns is None:
            self.asset_returns = []
        else:
            self.asset_returns = asset_returns        

    def backtest(self,weights=None,returns=None,principal=None):

        if weights is None:
            weights = self.weights
        if returns is None:
            returns = self.returns
        if principal is None:
            principal = self.principal     

        if principal is None:
            return (returns @ weights + 1).cumprod()
        else:
            return principal*((returns @ weights + 1).cumprod())

    def effFrontier(self,
    target_returns=None,
    weights_init = None, 
    sigma = None, 
    asset_bounds = None, 
    risk_free_rate = None,
    asset_returns = None,
    make_plot = False):

        if target_returns is None:
            target_returns = np.arange(0,0.2,0.01)
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

        # Initialize risks array        
        target_port_risks = np.zeros(target_returns.shape[0])

        # Compute risks for all target returns
        a = 0
        for target_return in target_returns:
            target_weights = pd.DataFrame(aa().minimize_vol(weights_init,sigma,asset_bounds,target_return,asset_returns).x,
                index=asset_returns.index.values,columns=None)
            target_port_risks[a] = mdl().portfolio_risk(target_weights,sigma)[0][0]
            a=a+1
            
        # Plot the frontier
        if make_plot is True:    
            plt.plot(target_port_risks,target_returns)
        return target_port_risks
                
                 

