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

    def __init__(self,returns=None):
        
        if returns is None:
            self.returns = []
        else:
            self.returns = returns