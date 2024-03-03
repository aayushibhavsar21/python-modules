import pandas as pd
 
df = pd.read_csv("A:/python/panda module.py/time series analysis/aapl.csv",index_col='Date',parse_dates = True)
print(df.index)   # -> dtype='datetime64[ns] -> naive

#Two types of datetimes in python
#    1.Naive (no timezone awareness)
#    2.Timezone aware datetime 

# When you have datetime data that doesn't have an associated time zone (timezone-naive), you can use tz_localize to specify the time zone
df = df.tz_localize(tz='US/Eastern')
print(df.index)   # ->  dtype='datetime64[ns, US/Eastern] -> Timezone aware datetime 

# if datetime objects already have an associated time zone, then it converts them to another time zone.
df = df.tz_convert('Europe/Berlin')
print(df)



from pytz import all_timezones
print (all_timezones)

london = pd.date_range('3/6/2012 00:09:00', periods=10, freq='h',tz='Europe/London')
print(london)                                                   # |-> this will use all pytz timezone

td = pd.date_range('3/6/2012 00:00', periods=10, freq='h',tz='dateutil/Europe/London')
print(td)                                                # |-> this will use all the timezone available in OS       



#using range function to generate time series
rng = pd.date_range(start="2017-08-22 09:00:00",periods=10, freq='30min')
s = pd.Series(range(10),index=rng)
print(s)

b = s.tz_localize(tz="Europe/Berlin")
print(b)

m = s.tz_localize(tz="Asia/Calcutta")
print(m)

#It will first convert individual timezones to UTC and then align datetimes to perform addition/subtraction etc. operations
print(b + m)



# shifting

print(df.shift(1))  # -> use to shift prices by 1 day
print(df.shift(-1)) 

df['Prev Day Close'] = df['Close'].shift(1)
print(df)

df['Price Change'] = df['Close'] - df['Prev Day Close']
print(df)

df['5 day return'] =  (df['Close'] - df['Close'].shift(5))*100/df['Close'].shift(5)
print(df)

df = df[['Close']]
print(df)

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