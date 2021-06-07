# Import libraries
import numpy as np
import pandas as pd
from modeling import Modeling as mdl

#import datetime

# User Inputs
path2data = 'C:\\Users\\Julio\\Downloads\\'
dataFiles = ["Crypto_Returns"]
startYear = 2020
startMonth = 4
startDay = 5
endYear = 2021
endMonth = 4
endDay = 4

# Process data
#startDate = datetime.date(startYear,startMonth,startDay)
#endDate = datetime.date(endYear,endMonth,endDay)
fullPath = path2data+dataFiles[0]+".csv"
returns = pd.read_csv(fullPath,header = 0, index_col="Date", parse_dates=True)
#assetData.fillna(0)
#print(assetData.head())
#returns = assetData["Adj Close"].pct_change()
#returns = returns.dropna()

#sigma = np.cov(assetData.values)
model = mdl(returns)
print(model.covariance())
#sigma = mdl.Modeling.covariance(assetData.values)
#print(sigma)

#for i in range(1,13,1):
#    currDate = (startDate + pd.offsets.DateOffset(months=i)).date()
#    print(returns[currDate])