# Import libraries
import numpy as np
import pandas as pd
from modeling import Modeling as mdl
from assetalloc import Asset_Allocation as aa

# User Inputs
weights = np.repeat(1/7,7)
bounds = ((0,1),)*7
path2data = 'C:\\Users\\Julio\\Downloads\\'
dataFiles = ["Crypto_Returns"]

# Import Data
fullPath = path2data+dataFiles[0]+".csv"
returns = pd.read_csv(fullPath,header = 0, index_col="Date", parse_dates=True)

# Create model object
model = mdl()
sigma = model.covariance(returns)
asset_returns = model.exp_returns(returns)
print('Portfolio Expected Return:')
print(model.portfolio_risk(weights, sigma))
print('Portfolio Risk:')
print(model.portfolio_return(weights, asset_returns))

# Create asset allocation object
allocation = aa()
print("Compute return target portfolio portfolio:")
print(allocation.minimize_vol(weights,sigma,bounds,0.01,asset_returns))