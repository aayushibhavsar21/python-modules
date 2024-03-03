
# tshift() -> Shift the time index, using the index’s frequency
import pandas as pd
 
df = pd.read_csv("A:/python/panda module.py/time series analysis/aapl.csv",index_col='Date',parse_dates = True)
df = df[['Close']]
print(df)
print(df.index)   #-> it does not have any freq

df.index = pd.date_range(start='2017-08-15',periods=19, freq='B')
print(df.index) 

df = df.tshift(1)
print(df)