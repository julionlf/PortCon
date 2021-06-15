"""
Get Returns Class:

DESCRIPTION:
    Contains various methods to convert returns to a specific
    frequency period. For example: daily to monthly daily to 
    yearly, monthly to quarterly, etc...

"""

import numpy as np
import pandas as pd

class Get_Returns:

    def __init__(self,returns=None,freq=None):
        
        if returns is None:
            self.returns = []
        else:
            self.returns = returns
        
        if freq is None:
            self.freq = []
        else:
            self.freq = freq

    def compound(self,returns=None):
        
        if returns is None:
            returns = self.returns
        
        return (returns + 1).prod() - 1

    def get_price_data(self,tickers):
        print("Hello from get_prices")