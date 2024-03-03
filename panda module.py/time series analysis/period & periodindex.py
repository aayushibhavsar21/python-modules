import pandas as pd

# yearly period
y = pd.Period('2016')
print(y)              # ->it will create period object 
print(dir(y))

print(y.start_time , y.end_time , y.is_leap_year)


# monthly period
m = pd.Period('2017-12')
print(m)
print(m.start_time)
print(m.end_time)
print(m+1)



# hourly period
h = pd.Period('2017-08-15 23:00:00',freq='H')
print(h)
print(h+1)
print(h-6)

#Achieve same results using pandas offsets hour
print(h+pd.offsets.Hour(1))

d = pd.Period('2016-02-28', freq='D')
print(d)

print(d.start_time)
print(d.end_time)

print(d+1)
# by providing specific freq we can generate any time period  



# Quarterly Period

q1= pd.Period('2017Q1', freq='Q-JAN')   # freq -> jan -2017 is end of year, so Quarterly Periods will be : feb-apr 2016 , may -jul 2016 , aug-oct 2016 , nov 2016 - jan 2017 
q2= pd.Period('2018Q3', freq='Q-JAN')   # freq -> jan -2017 is end of year, so Quarterly Periods will start from feb-2016
                #  |-> number of quater
print(q1)
print(q1+1)

print((q1+2).start_time)
print((q1+2).end_time)

# convert one freq into other 
print(q1.asfreq('M',how='start'))
print(q1.asfreq('M',how='end'))

print(f"difference between {q1} and {q2} in quaters : {q2-q1}") 



# period index 

print(pd.period_range('2011', '2017', freq='q'))

r = pd.period_range('2011', '2017', freq='Q-JAN')
print(r)

#for i in range(25):
#    print(r[i].start_time)


idx = pd.period_range('2011',periods=10,freq='q')
import numpy as np
ps = pd.Series(np.random.randn(len(idx)), idx)
print(ps)
print(ps['2011'],ps['2011':'2013'])

# converting into datetime index
pst = ps.to_timestamp()
print(pst)

print(pst.index)

#converting date time index back to period index
ps = pst.to_period()
print(ps)



import pandas as pd 
df = pd.read_csv("A:/python/panda module.py/time series analysis/wmt.csv")
print(df,"\n")

df.set_index("Line Item",inplace=True)

df = df.T       #  or df.transpose() -> traspose of the   
print(df,"\n")

print(df.index) #-> object type

df.index = pd.PeriodIndex(df.index, freq="Q-JAN")

df['Start Date'] = df.index.map (lambda x: x.start_time)

df['End Date'] = df.index.map (lambda x: x.end_time)
df['End Date'] = df['End Date'].dt.date
print(df)


