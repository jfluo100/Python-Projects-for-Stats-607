import pandas as pd
#from pandas import to_datetime
import random
import numpy as np

## Part II, 2.1
dates = pd.date_range('20180101', periods=365)
col_names=['Year','Month','Day','Weekday','Value']
Num = range(1,366)
Year = [2018] * 365
Month = []
Day = []

for i in range(31):
    Month.append('January')
    Day.append(i+1)
    
for i in range(28):
    Month.append('February')
    Day.append(i+1)

for i in range(31):
    Month.append('March')
    Day.append(i+1)
    
for i in range(30):
    Month.append('April')
    Day.append(i+1)
    
for i in range(31):
    Month.append('May')
    Day.append(i+1)
    
for i in range(30):
    Month.append('June')
    Day.append(i+1)
    
for i in range(31):
    Month.append('July')
    Day.append(i+1)
    
for i in range(31):
    Month.append('August')
    Day.append(i+1)
    
for i in range(30):
    Month.append('September')
    Day.append(i+1)
    
for i in range(31):
    Month.append('October')
    Day.append(i+1)
    
for i in range(30):
    Month.append('November')
    Day.append(i+1)
    
for i in range(31):
    Month.append('December')
    Day.append(i+1)

# 2018/1/1 is Monday, brutal loops are used here:
Weekday = []
for i in range(52):
    Weekday.append('Monday')
    Weekday.append('Tuesday')
    Weekday.append('Wednesday')
    Weekday.append('Thursday')
    Weekday.append('Friday')
    Weekday.append('Saturday')
    Weekday.append('Sunday')
# 365 = 52 * 7 + 1, the last day would be monday
Weekday.append('Monday')

Value = []
for i in range(365):
    Value.append(random.randint(0,100))
# Here I do not know if 0 and/or 100 could be included, it does not really matter.

data1 = {'Year': Year, 'Month': Month, 'Day': Day, 'Weekday': Weekday, 'Value': Value}

# outcome of 2.1
dailyValues1 = pd.DataFrame(index = dates, columns = col_names, data = data1) 
print(dailyValues1)

###############################################################################
###############################################################################


## Part II, 2.2
MonthIndex = {'January','February','March','April',
              'May','June','July','August',
              'September','October','November','December'}
DayIndex = range(1,32)

## Set up 'value' matrix  ----------------------------------------------------
value = np.empty((12,31))

for j in range(0,31):
    value[:,j] = [Value[j],Value[j+31],Value[j+59],Value[j+90],
          Value[j+120],Value[j+151],Value[j+181],Value[j+212],
          Value[j+243],Value[j+273],Value[j+304],Value[j+334]]

# Here, days like Feb 29 are given value, now replace them with NaNs
value[1,28:32] = np.nan # Feb
value[3,30:32] = np.nan # April
value[5,30:32] = np.nan # June
value[7,30:32] = np.nan # August
value[10,30:32] = np.nan # November
## Set up completed! ----------------------------------------------------------

# outcome of 2.2
dailyValues2 = pd.DataFrame(index = MonthIndex, columns = DayIndex, data = value) 
print(dailyValues2)







