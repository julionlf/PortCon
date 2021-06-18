#import numpy as np
#import pandas as pd

class Simulation:

    def __init__(self,weights=None,returns=None,principal=None):
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
    
    def backtest(self,weights=None,returns=None,principal=None):

        if weights is None:
            weights = self.weights
        if returns is None:
            returns = self.returns
        if principal is None:
            principal = self.principal

        if principal is None:
            return ((returns @ weights)+1).cumprod()
        else:
            return principal*((returns @ weights)+1).cumprod()
