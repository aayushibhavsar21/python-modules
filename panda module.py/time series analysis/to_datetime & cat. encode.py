import pandas as pd

print(pd.to_datetime('01/05/2017'),"\n",pd.to_datetime('2017-01-05'),"\n",pd.to_datetime('Jan 5, 2017'),"\n")
print(pd.to_datetime('2017.01.05'),"\n",pd.to_datetime('2017/01/05'),"\n",pd.to_datetime('20170105'))

print(pd.to_datetime('01/05/2017  2:30:00 PM'),"\n",pd.to_datetime('2017-01-05 14:30:00'),"\n",pd.to_datetime('Jan 5, 2017'),"\n")

print(pd.to_datetime('5-1-2016'))  # it will convert as 1st may rather than 5th jan
print(pd.to_datetime('5-1-2016', dayfirst=True))

#can provide our own custom format
print(pd.to_datetime('2017$01$05', format='%Y$%m$%d'))
print(pd.to_datetime('2017#01#05', format='%Y#%m#%d'))

print(pd.to_datetime(['2017-01-05', 'Jan 6, 2017', 'abc'], errors='ignore'))
print(pd.to_datetime(['2017-01-05', 'Jan 6, 2017', 'abc'], errors='coerce'))


# Epoch
# Epoch or Unix time means number of seconds that have passed since Jan 1, 1970 00:00:00 UTC time

current_epoch = 1501324478
print(pd.to_datetime(current_epoch, unit='s'))
print(pd.to_datetime(current_epoch*1000, unit='ms'))

t = pd.to_datetime([current_epoch], unit='s')
print(t)

print(t.view('int64'))  # will givw output in neno seconds



#_______categorical encoding_______

import pandas as pd

df = pd.read_excel("A:/python/panda module.py/survey.xls")
print(df)
print(df['Sex'].unique() , df['Sex'].nunique())  # -> unique values of sex column , number of unique values in sex column

x = df['Sex'].map({'Male':1,'Female':0})  # -> by map we can access max 2 values
df.insert(loc=3,column='gender',value=x)
print(df)

#to map more than 2 values:
print(df['Nationality'].unique() , df['Nationality'].nunique())  
print(pd.get_dummies(data=df , columns = ['Nationality'] , drop_first=True))  # base on other 3 values we can estimate value of first
