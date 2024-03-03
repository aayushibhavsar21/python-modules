import pandas as pd

df = pd.read_csv("A:\python\panda module.py\weather_by_cities.csv")
print(df)



#_________ join data using group by_________

g = df.groupby("city")
for city, data in g:
    print("city:",city)
    print("data:\n",data)  
    print("\n")

# to get individual data frame:
    #g.get_group('city_name')

print(g.max())  # firstly we have divided our data frame in different group based on city 
# performed analysis and now combining it using g.max(). this process is called split apply combine.

print(g["temperature"].mean())
print(g["windspeed"].mean())

# Print the descriptive statistics for each group
print(g.describe())

# plot city data
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("A:\python\panda module.py\weather_by_cities.csv")
print(df)
g = df.groupby("city")

for city,city_data in g:
    plt.plot(city_data['day'], city_data['temperature'], label=f'{city} Temperature')
    plt.plot(city_data['day'], city_data['windspeed'], label=f'{city} Windspeed')
    plt.legend()
    plt.xlabel('Day')
    plt.ylabel('Value')
    plt.title(f'{city} Temperature and Windspeed Changes by City')
    
plt.show()



# _________join data frame using concatenate _________
    
import pandas as pd
india_weather = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
    "humidity": [80, 60, 78]
})
print(india_weather,"\n")

us_weather = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
    "humidity": [68, 65, 75]
})
print(us_weather,"\n")

# concate data row wise

df = pd.concat([india_weather, us_weather])
print(df,"\n")

df = pd.concat([india_weather, us_weather],ignore_index=True)
print(df,"\n")

df = pd.concat([india_weather, us_weather], keys=["india", "us"])
print(df,"\n")

print(df.loc["india"],"\n",df.loc["us"])

# concate data column wise

temperature_df = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
})
print(temperature_df)

windspeed_df = pd.DataFrame({
    "city": ["delhi","mumbai"],
    "windspeed": [7,12],
})
print(windspeed_df)

df = pd.concat([temperature_df,windspeed_df],axis=1)
print(df)


temperature_df = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
}, index=[0,1,2])
print(temperature_df)

windspeed_df = pd.DataFrame({
    "city": ["delhi","mumbai"],
    "windspeed": [7,12],
}, index=[1,0])
print(windspeed_df)
#index is used, so during concatenation, rows with the same index get concatenated.
 
df = pd.concat([temperature_df,windspeed_df],axis=1)
print(df)


s = pd.Series(["Humid","Dry","Rain"], name="event")
print(s)

df = pd.concat([temperature_df,s],axis=1)
print(df)



# _________join data frame using merge _________

import pandas as pd 

temperature_df = pd.DataFrame({
    "city": ["mumbai","delhi","banglore","pune"],
    "temperature": [32,45,30,39],
})
print(temperature_df,"\n")

windspeed_df = pd.DataFrame({
    "city": ["delhi","banglore","mumbai","ahemdabad"],
    "windspeed": [7,12,21,24],
})
print(windspeed_df,"\n")

df = pd.merge(temperature_df,windspeed_df,on="city") # it use inner join by default
print(df,"\n")

df = pd.merge(temperature_df,windspeed_df,on="city",how="outer")
print(df,"\n")
df = pd.merge(temperature_df,windspeed_df,on="city",how="outer",indicator=True)
print(df,"\n")

df = pd.merge(temperature_df,windspeed_df,on="city",how="left")
print(df,"\n")

df = pd.merge(temperature_df,windspeed_df,on="city",how="right")
print(df,"\n")


df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando", "baltimore"],
    "temperature": [21,14,35,38],
    "humidity": [65,68,71, 75]
})
print(df1,"\n")

df2 = pd.DataFrame({
    "city": ["chicago","new york","san diego"],
    "temperature": [21,14,35],
    "humidity": [65,68,71]
})
print(df2,"\n")

df3= pd.merge(df1,df2,on="city")
print(df3,"\n")

df3= pd.merge(df1,df2,on="city",how="outer", suffixes=('_first','_second'))
print(df3,"\n")



# _________join data frame using join _________

import pandas as pd 

df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
})
df1.set_index('city',inplace=True)
print(df1)

df2 = pd.DataFrame({
    "city": ["chicago","new york","orlando"],
    "humidity": [65,68,75],
})
df2.set_index('city',inplace=True)
print(df2)

print(df1.join(df2,lsuffix='_l', rsuffix='_r'))