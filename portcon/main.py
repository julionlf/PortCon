# Import libraries
import numpy as np
import pandas as pd
from modeling import Modeling as mdl

# User Inputs
weights = np.repeat(1/4,6)
path2data = 'C:\\Users\\Julio\\Downloads\\'
dataFiles = ["Crypto_Returns"]

# Import Data
fullPath = path2data+dataFiles[0]+".csv"
returns = pd.read_csv(fullPath,header = 0, index_col="Date", parse_dates=True)

# Create model object
model = mdl()
print(model.portfolio_return(model.exp_returns(returns),weights))


# Print Stationary Covariance Matrix
#print(model.covariance())

# Print Stationary Exp. Returns Vector
#print(model.exp_returns())