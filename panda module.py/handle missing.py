import pandas as pd

df = pd.read_excel("A:\python\panda module.py\weather.xlsx" , parse_dates=["Date"])
print(df)

print(type(df["Date"][0]))

# _________check if null_________
print(df.isnull())

# _________1 - by using fillna_________

# fillna will fill all NaN values by 0
new_df = df.fillna(0)
print("\n",new_df)

# fillna will fill all NaN values by given value , but here is we use 0 for NaN temp which means major drop in temp , which might cause of inaccurate statistic values
new_df = df.fillna({
        'Avg Temp': 0,
        'wind.Speed': 0,
        'Precipitation': 0,
        'City': 'not provided',
        'State': 'not provided',
    })
new_df
print("\n",new_df)

new_df = df.fillna(method="ffill")  # ffill - forward fill - carry forward previous value
print("\n",new_df)                       # ffill is use to find accurate statistic values  

new_df = df.fillna(method="bfill")  # bfill - backward fill - fill value by next day's value
print("\n",new_df)    
                     
new_df = df.fillna(method="bfill",axis=1)  # fill blank by next column's data 
print("\n",new_df)   

#if we provid limit ,fill will copy data only for given limited time
#df.fillna(method="bfill",limit=1) 



#_________ 2 - by using interpolate_________

new_df = df.interpolate() # average of previous and next value
print(new_df)



#_________ 3 - by using dropna_________

new_df = df.dropna() # drop all rows with NaN value
print(new_df)

df.dropna(how="all") # drop rows which have all value NaN 
#df.dropna(how="any") # drop rows which have any NaN value  

df.dropna(thresh=1)  # keep row if it have only 1 NaN value 



# _________4 - by using replace _________

import pandas as pd
import numpy as np
df = pd.read_csv("A:\python\panda module.py\stock_data.csv")
print(df)

new_df = df.replace(-1,np.NaN)  # can provide list of value also - replace([-1,-2],np.NaN)
print(new_df)

new_df = df.replace({
        "eps":"-1",
        "people":"n.a.",
    },np.NaN)
print(new_df)

#new_df = df.replace({
#        -1: np.nan,
#        'not available': 0,
#    })

new_df = df.replace({'price': '[A-Za-z]'},'', regex=True) 
print(new_df)



df = pd.DataFrame({
    'score': ['exceptional','average', 'good', 'poor', 'average', 'exceptional'],
    'student': ['rob', 'maya', 'parthiv', 'tom', 'julian', 'erica']
})
print(df)

new_df = df.replace(['poor', 'average', 'good', 'exceptional'], [1,2,3,4])
print(new_df)