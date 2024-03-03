import pandas as pd
 
df = pd.read_csv("panda module.py/time series analysis/appl_no_date.csv")
print(df,"\n")

# if we have dataset which does not include dates , so to add dates in that data set we can use given method:
 
rng = pd.date_range(start="6/1/2016",end="7/13/2016",freq='B')  # -> generate dates , 'B' - bussiness days (does not include weekends )
df.set_index(rng, inplace=True)  #-> appending rng with our dataframe df , inplace = to make changes in original data rather than make copy of it 
print(df)

#'B' frequency also include holidays which are not a bussiness days.

#_____Custom Business Day_____

# 1) by using US calendar

from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay

us_cal = CustomBusinessDay(calendar=USFederalHolidayCalendar())
rng = pd.date_range(start="7/1/2017",end="8/15/2017", freq=us_cal)
print(rng)

df.set_index(rng,inplace=True)
print(df)



# 2) By using Abstract Holiday Calendar

from pandas.tseries.holiday import AbstractHolidayCalendar,nearest_workday,Holiday
from pandas.tseries.offsets import CustomBusinessDay

class MyCalendar(AbstractHolidayCalendar):
    rules = [
        Holiday('new year',month=11 , day=11,observance=nearest_workday),
    ]
# observance=nearest_workday -> if holiday comes on weekend then panadas will update it on nearest bussiness day 

my_cal = CustomBusinessDay(calendar=MyCalendar())

rng = pd.date_range(start="11/1/2017",end='11/24/2017',freq=my_cal)
print(rng)



# 3) Weekend in egypt is Friday and Saturday

import pandas as pd
from pandas.tseries.offsets import CustomBusinessDay

egypt_weekdays = "Sun Mon Tue Wed Thu"

b = CustomBusinessDay(weekmask=egypt_weekdays)
print(pd.date_range(start="7/1/2017",periods=20,freq=b))


b = CustomBusinessDay(holidays=['2017-07-04', '2017-07-10'], weekmask=egypt_weekdays)
print(pd.date_range(start="7/1/2017",periods=20,freq=b))


from datetime import date, datetime
dt = datetime(2017,7,9)
print(dt)

print(dt + 1*b) 

