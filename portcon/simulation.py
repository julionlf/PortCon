# Import libraries
import numpy as np
import pandas as pd
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
    asset_returns = None):

        if target_returns is None:
            target_returns = self.target_returns
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
        
        print(target_returns)
        for target_return in target_returns:
            print(target_return)
            target_weights = pd.DataFrame(aa().minimize_vol(weights_init,sigma,asset_bounds,target_return,asset_returns).x,
                index=asset_returns.columns.values,columns=None)
            target_port_return = mdl().portfolio_return(target_weights,asset_returns)[0]
            target_port_risk = mdl().portfolio_risk(target_weights,sigma)[0][0]
            print("Return: "+target_port_return + ", Risk: " + target_port_risk)
                
                 

