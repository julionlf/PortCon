# Import libraries
import numpy as np
import pandas as pd
from modeling import Modeling as mdl

# User Inputs
weights = np.repeat(1/7,7)
path2data = 'C:\\Users\\Julio\\Downloads\\'
dataFiles = ["Crypto_Returns"]

# Import Data
fullPath = path2data+dataFiles[0]+".csv"
returns = pd.read_csv(fullPath,header = 0, index_col="Date", parse_dates=True)

# Create model object
model = mdl()
print('Portfolio Expected Return:')
print(model.portfolio_return(model.exp_returns(returns),weights))
print('Portfolio Risk:')
print(model.covariance(returns).shape)
#print(model.portfolio_risk(model.covariance(returns),weights))