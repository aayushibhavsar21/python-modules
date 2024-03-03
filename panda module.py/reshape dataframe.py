# reshaping our original table in a convenient way so can do analysis easily.


# _________By using pivot / pivot_table method_________

import pandas as pd

df = pd.read_csv("A:\python\panda module.py\weather_by_cities.csv")
print(df,"\n")

print(df.pivot(index='city',columns='day'),"\n")
print(df.pivot(index='city',columns='day',values="temperature"),"\n")
print(df.pivot(index='city',columns='day',values="windspeed"),"\n")

print(df.pivot(index='day',columns='city'),"\n")
#print(df.pivot(index='temperature',columns='day'),"\n")

print(df.pivot_table(index='city', values=['temperature', 'windspeed'],columns='day'))



data = {
    'date': ['5/1/2017', '5/1/2017', '5/2/2017', '5/2/2017', '5/1/2017', '5/1/2017', '5/2/2017', '5/2/2017'],
    'city': ['new york', 'new york', 'new york', 'new york', 'mumbai', 'mumbai', 'mumbai', 'mumbai'],
    'temperature': [65, 61, 70, 72, 75, 78, 82, 80],
    'humidity': [56, 54, 60, 62, 80, 83, 85, 26]
}

df = pd.DataFrame(data)
print(df)
print(df.pivot_table(index="city",columns="date"))

df['date'] = pd.to_datetime(df['date'])
print(df.pivot_table(index=pd.Grouper(freq='M',key='date'),columns='city'))



# _________By using melted method_________

import pandas as pd

data = {
    'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'chicago': [32, 30, 28, 22, 30, 20, 25],
    'chennai': [75, 77, 75, 82, 83, 81, 77],
    'berlin': [41, 43, 45, 38, 30, 45, 47]
}
df = pd.DataFrame(data)

melted = pd.melt(df, id_vars=["day"])
print(melted)
melted = pd.melt(df, id_vars=["day"], var_name='city', value_name='temperature')
print(melted)
print(melted[melted["city"]=="chicago"])



# _________By using stacking / unstacking method_________

import pandas as pd

df = pd.read_csv("A:\python\panda module.py\stock_data.csv") 
print(df)
stacked_df = df.stack()
print(stacked_df)
print(stacked_df.unstack())



# _________by generating crosstab_________
 
import pandas as pd

df = pd.read_excel("A:\python\panda module.py\survey.xls")
print(df,"\n")
 
     #pd.crosstab(    x-axis    ,    y-axis    )
print(pd.crosstab(df.Nationality,df.Handedness))
# it shows frequency (no. of occurrence) of variable (on y axis)

print(pd.crosstab(df.Sex,df.Handedness,margins=True))
print(pd.crosstab(df.Sex, [df.Handedness,df.Nationality], margins=True))
print(pd.crosstab([df.Nationality, df.Sex], [df.Handedness], margins=True))

print(pd.crosstab(df.Sex, df.Handedness, normalize='index'))
# it gives the percentage of variable (on y axis)

import numpy as np
print(pd.crosstab(df.Sex, df.Handedness, values=df.Age, aggfunc=np.average)) 
print(pd.crosstab(df.Sex, df.Handedness, values=df.Age, aggfunc=np.max)) 



#_________ how to reduce memory usage in paqndas _________
  #https://pythonspeed.com/articles/pandas-load-less-data/
