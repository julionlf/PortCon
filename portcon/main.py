# Import libraries
import numpy as np
import pandas as pd
from modeling import Modeling as mdl
from assetalloc import Asset_Allocation as aa

# User Inputs
#weights = np.repeat(1/2,2)
#bounds = ((0,1),)*2
#path2data = 'C:\\Users\\Julio\\Projects\\Finance_Data\\data\\'
#dataFiles = ['ind30_m_vw_rets']

# Import Data
#returns = pd.read_csv(fullPath,header = 0, index_col=0, parse_dates=True)/100
#returns.index = pd.to_datetime(returns.index, format ="%Y%m").to_period("M")
#returns.columns = returns.columns.str.strip()
#returns = returns[["Games","Steel"]]

# User Inputs Crypto
weights = np.repeat(1/7,7)
bounds = ((0,1),)*7
path2data = 'C:\\Users\\Julio\\Downloads\\'
dataFiles = ["Crypto_Returns"]
fullPath = path2data+dataFiles[0]+".csv"

# Import Crypto Data
returns = pd.read_csv(fullPath,header = 0, index_col="Date", parse_dates=True)
print("Raw data import:")
print(returns.head())
print("Converting daily returns to monthly returns data import:")
print(returns.resample('M'))

# Create model objectcs
model = mdl()
sigma = model.covariance(returns)
asset_returns = model.exp_returns(returns)
print('Portfolio Risk')
print(model.portfolio_risk(weights, sigma))
print('Portfolio  Expected Return:')
print(model.portfolio_return(weights, asset_returns))
print("Asset Returns:")
print(asset_returns)

# Create asset allocation object
allocation = aa()
print("Compute return target portfolio:")
print(allocation.minimize_vol(weights,sigma,bounds,0.01,asset_returns))
print("Compute MSR Portfolio:")
print(allocation.msr(weights,sigma,bounds,0.0003,asset_returns))
print("Compute GMV Portfolio:")
gmv_weights = allocation.gmv(weights,sigma,bounds)
print(gmv_weights)
for asset in returns.columns:
    print(asset)