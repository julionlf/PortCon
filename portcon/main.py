# Import libraries
from operator import index
import numpy as np
import pandas as pd
from get_returns import Get_Returns as gr
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
path2data = 'C:\\Users\\Julio\\Downloads\\'
dataFiles = ["Crypto_Returns"]
fullPath = path2data+dataFiles[0]+".csv"
risk_free_rate = 0

# Import Crypto Data
returns = pd.read_csv(fullPath,header = 0, index_col="Date", parse_dates=True)
gr = gr()
print("Raw data import:")
print(returns.head())
print('\n')

# Create equal weights vector
noAssets = returns.shape[1]
weights = np.repeat(1/noAssets,noAssets)
bounds = ((0,1),)*noAssets

# Compute compunded monthly returns from daily data
print("Compute compunded return per month:")
returns = returns.resample('M').apply(gr.compound).to_period('M')
print(returns)
print('\n')

# Create model objectcs
model = mdl()
sigma = model.covariance(returns)
asset_returns = model.exp_returns(returns)

# Compute equally weighted portfolio risk and return
print("Stationary Expected Returns of each asset:")
print(asset_returns)
print('\n')

print('Equal Weights Portfolio Risk')
print(model.portfolio_risk(weights, sigma))
print('\n')

print('Equal Weights Portfolio Expected Return:')
print(model.portfolio_return(weights, asset_returns))
print('\n')

# Create asset allocation object
allocation = aa()

# Compute Portfolios
print("Compute target return portfolio:")
target_weights = pd.DataFrame(allocation.minimize_vol(weights,sigma,bounds,0.1,asset_returns).x,
 index=returns.columns.values,columns=None)
target_port_return = model.portfolio_return(target_weights,asset_returns)
target_port_risk = model.portfolio_risk(target_weights,sigma) 
print((target_weights*100).round(2))
print("Portfolio expected return: " + str((target_port_return.values*100).round(2)))
print("Portfolio risk: " + str((target_port_risk.values*100).round(2)))
print("Portfolio Sharpe: " + str(model.portfolio_sharpe(target_port_return,target_port_risk,risk_free_rate)))
print('\n')

print("Compute MSR Portfolio:")
msr_weights = pd.DataFrame(allocation.msr(weights,sigma,bounds,0.0003,asset_returns).x,
 index=returns.columns.values)
msr_return = model.portfolio_return(msr_weights,asset_returns)
msr_risk = model.portfolio_risk(msr_weights,sigma) 
print((msr_weights*100).round(2))
print("Portfolio expected return: " + str((msr_return.values*100).round(2)))
print("Portfolio risk: " + str((msr_risk.values*100).round(2)))
print("Portfolio Sharpe: " + str(model.portfolio_sharpe(msr_return,msr_risk,risk_free_rate)))
print('\n')

print("Compute GMV Portfolio:")
gmv_weights = pd.DataFrame(allocation.gmv(weights,sigma,bounds).x,
index=returns.columns.values)
gmv_return = model.portfolio_return(gmv_weights,asset_returns)
gmv_risk = model.portfolio_risk(gmv_weights,sigma)
print((gmv_weights*100).round(2))
print("Portfolio expected return: " + str((gmv_return.values*100).round(2)))
print("Portfolio risk: " + str((gmv_risk.values*100).round(2)))
print("Portfolio Sharpe: " + str(model.portfolio_sharpe(gmv_return,gmv_risk,risk_free_rate)))
print('\n')