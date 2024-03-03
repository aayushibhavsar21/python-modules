import pandas as pd

df = pd.read_csv("panda module.py/time series analysis/aapl.csv")
print(df.head(10))
print(type(df["Date"][0]),"\n")

df = pd.read_csv("panda module.py/time series analysis/aapl.csv",parse_dates=["Date"],index_col="Date")
print(df.head(10))
print(df.index)

#________(1) Partial Date Index: Select Specific Months Data________

print(df.loc['2017-06-30'])
print(df.loc["2017-01"])
print(df.loc['2017-06'].head()) 
print(df.loc['2017-06'].Close.mean())
print(df.loc['2017'].head(2)) 

#________(2) Select Date Range________

# Sort DataFrame by index (Date)

print(df.loc['2017-01-03':'2017-01-09'])

#________ Resampling ________

print(df['Close'].resample("M").mean().head())
print(df.loc['2016-07'])


# our original dataset does not include weekends , so to add weekends and add data in it from previous date :

df = pd.read_csv("panda module.py/time series analysis/aapl.csv",parse_dates=["Date"],index_col="Date")

daily_index = pd.date_range(start="7/11/2016",end="7/30/2016",freq='D') # 'D'- calendar day frequency
print(daily_index)

print(daily_index.difference(df.index)) 
print(df["2016-07-11":"2016-07-20"].Close.mean())

print(df.asfreq('D',method='pad'))
print(df.asfreq('W',method='pad'))  # W - weekly frequency
print(df.asfreq('h',method='pad'))  # h - hourly frequency

#_____generating DatetimeIndex with periods argument_____

rng = pd.date_range('1/1/2011', periods=72, freq='H')  # when we do not know end date then we can provide period
                                                         # it will generate 72 dates
print(rng)

