
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