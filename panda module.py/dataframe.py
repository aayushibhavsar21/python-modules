import pandas as pd

# _________1st method for creating dataframe ( can also use csv file  syntax:- df = pd.read_csv(file_path))_________

df = pd.read_excel(r"panda module.py\weather.xlsx") 
print(df.info())   # Provide all kind of info like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement etc.

print(f"\n{df},\n{df.shape},\n{df.head(2)},\n{df.tail(2)},\n{df[2:5]}")

print(df["Date"])  # or df.Date (df.column_name to print any column )  
print(type(df["Date"]),"\n")

print(df[["Date","Avg Temp","Wind.Speed"]],"\n")

print(df[df['State']=='Alaska'])
value = df['State'][(df['State'] == 'Alabama') | (df['State'] == 'Alaska')].value_counts()
print( value )
print(df['State'].nunique())

print(df[df["Avg Temp"]>=45])
print(df[df["Avg Temp"]==df["Avg Temp"].max()])
print(df[["Date","Avg Temp"]][df["Avg Temp"]==df["Avg Temp"].max()],"\n")

print("max temperature in avg temp:",df["Avg Temp"].max())
print("mean of temperature:",df["Avg Temp"].mean())
print("std of temperature:",df["Avg Temp"].std(),"\n") # standard deviation

print(df.describe(),"\n") # print statistic properties
print(type(df["Precipitation"][0]))

df.set_index("Precipitation",inplace=True) # inplace is use to make changes in original data set otherwise it will make other copy of original data
print(df.loc[1.24])
df.reset_index(inplace=True)

#to delete any column :
#df.drop([column names],axis=1)


# _________2nd method : can make dataset using dictionary_________

weather_data={
    "day":["1/2/2003","4/5/2006","7/8/2009"],
    "temp":[23,20,27],
    'windspeed':[6,7,8],
    "event":["rain","sunny","snow"]
}

dictionary_df = pd.DataFrame(weather_data)
print(dictionary_df,dictionary_df.shape)



#_________ 3rd method : can make dataframe using tuples_________

weather_data = [
    ('1/1/2017',32,6,'Rain'),
    ('1/2/2017',35,7,'Sunny'),
    ('1/3/2017',28,2,'Snow')
]
tuple_df = pd.DataFrame(data=weather_data, columns=['day','temperature','windspeed','event'])
print(tuple_df)



# _________4th method : Using list of dictionaries_________

weather_data = [
    {'day': '1/6/2017', 'temperature': 32, 'windspeed': 3, 'event': 'Rain'},
    {'day': '9/2/2012', 'temperature': 25, 'windspeed': 7, 'event': 'Sunny'},
    {'day': '2/7/2019', 'temperature': 28, 'windspeed': 2, 'event': 'Snow'}, 
]
Dlist_df = pd.DataFrame(data=weather_data, columns=['day','temperature','windspeed','event'])
print(Dlist_df)



# to write 2 dataset in diffrent sheets in 1 file  
with pd.ExcelWriter('weather_merged.xlsx') as writer:
    tuple_df.to_excel(writer, sheet_name="weather1")
    Dlist_df.to_excel(writer, sheet_name="weather2")