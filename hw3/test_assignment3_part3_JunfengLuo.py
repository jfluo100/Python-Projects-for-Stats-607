import pandas as pd
#import random
import numpy as np
import statistics as stat
#import datetime as dttm
#import re
import matplotlib.pyplot as plt

tripsDF = pd.read_csv('trips.csv')

tripsPart=tripsDF#[:10000]  # use part of the data to speed up

# 3.1 --------------------------------------------------------------------
tripsPart=tripsPart[(tripsPart.pickup_latitude > 40) & 
                    (tripsPart.pickup_latitude < 41.5)]
tripsPart=tripsPart[(tripsPart.pickup_longitude > -75) & 
                    (tripsPart.pickup_longitude < -72)]
tripsPart=tripsPart[(tripsPart.passenger_count > 0) & (tripsPart.passenger_count < 5)]
tripsPart=tripsPart[tripsPart.trip_time_in_secs > 1800]

trips1 = tripsPart
# the outcome of 3.1
print(trips1)

# The subset we are interested in has 27,530 rows -----------------------------

# 3.2 --------------------------------------------------------------------

num = len(tripsPart)
avg_num_of_psgr = stat.mean(tripsPart.passenger_count[:])
avg_trip_time = stat.mean(tripsPart.trip_time_in_secs[:])
avg_trip_time_std = stat.stdev(tripsPart.trip_time_in_secs[:])

# the outcome of 3.2
tripStats = (num, avg_num_of_psgr, avg_trip_time, avg_trip_time_std)
print(tripStats)

# 3.3 --------------------------------------------------------------------

#trips1['coor'] = pd.Series(['1']*len(trips1), index=trips1.index)
##for i in range(len(trips1)):
##    trips1['coor'][i] = str(round(trips1['pickup_longitude'][i],2)) + str(round(trips1['pickup_latitude'][i],2))
long = round(trips1['pickup_longitude'],2).values
lati = round(trips1['pickup_latitude'],2).values
long1=long.astype(np.str)
lati1=lati.astype(np.str)
#for i in range(len(trips1)):
#    trips1['coor'][i] = str(lati1[i])+','+str(long1[i])
trips1['latitude'] = lati1
trips1['longtitude'] = long1
Coords = ['0'] * len(trips1)
for i in range(len(trips1)):
    Coords[i] = str(lati1[i]) + ',' + str(long1[i])
trips1['Coords'] = Coords
zipfile = pd.read_csv('zipcodes.csv')

trips2 = pd.merge(trips1, zipfile, on = 'Coords')
trips2.dropna(how = 'any')
trips2 = trips2.drop(['latitude','longtitude'], axis=1)
# the outcome of 3.3
print(trips2)

# 3.4 --------------------------------------------------------------------

trips3_temp = trips2
#trips3_temp = trips2.sort_values(by=['pickup_datetime','Zipcode'])

#Day = np.zeros(len(trips3))
#Hour = np.zeros(len(trips3))

#Day = [0]*(len(trips3))
#Hour = [0]*(len(trips3))

#for i in range(len(trips3)):
#    x = re.match(r'[0-9]+-[0-9]+-([0-9]+) ([0-9]+):[0-9]+:[0-9]+$',
#                 trips3['pickup_datetime'][i])
#    Day[i] = x.group(1)
#    Hour[i] = x.group(2)

# divide time into date and hour-min-sec
trips3_temp['Day'], trips3_temp['Hour'] = trips3_temp['pickup_datetime'].str.split(' ', 1).str
# now Day is in Y-M-D format
# pick out D by split method
trips3_temp['Day'] = trips3_temp['Day'].str.split('-', 2).str[2]
#trips3['Day'] = int(trips3['Day'])
# now time in H-M-S format
# pick out H by split method
trips3_temp['Hour'] = trips3_temp['Hour'].str.split(':', 1).str[0]
# groupby Day, Hour and Zipcode, now there are 42107 rows, each using D,H,Z as index
trips3 = pd.DataFrame(trips3_temp.groupby(['Day', 'Hour', 'Zipcode']).count().iloc[:, 0])
trips3.columns = ['Count']
trips3.reset_index(inplace = True)
#trips3['Day'].astype(int)
#trips3['Hour'].astype(int)
D = [0]*(len(trips3))
H = [0]*(len(trips3))
for i in range(len(trips3)):
    D[i] = int(trips3['Day'][i])
for i in range(len(trips3)):
    H[i] = int(trips3['Hour'][i])
# turn Day and Hour into int64
trips3['Day'] = D
trips3['Hour'] = H


#trips3['Day'] = Day
#trips3['Hour'] = Hour
#grouped = trips3.groupby(trips3['Day'])
#Day.count

# the outcome of 3.4
print(trips3)

# 3.5 --------------------------------------------------------------------

weatherfile = pd.read_csv('weather.csv')

trips4 = pd.merge(trips3, weatherfile, on = ['Day', 'Hour'])
trips4.dropna(how = 'any')

# the outcome of 3.5
print(trips4)

# 3.6 --------------------------------------------------------------------
Weekday = ['0'] * len(trips4)
trips5 = trips4
for i in range(len(trips5)):
    if trips5['Day'][i] % 7 == 1 :
        Weekday[i] = 'Tuesday'
for i in range(len(trips5)):
    if trips5['Day'][i] % 7 == 2 :
        Weekday[i] = 'Wednesday'
for i in range(len(trips5)):
    if trips5['Day'][i] % 7 == 3 :
        Weekday[i] = 'Thursday'
for i in range(len(trips5)):
    if trips5['Day'][i] % 7 == 4 :
        Weekday[i] = 'Friday'
for i in range(len(trips5)):
    if trips5['Day'][i] % 7 == 5 :
        Weekday[i] = 'Saturday'
for i in range(len(trips5)):
    if trips5['Day'][i] % 7 == 6 :
        Weekday[i] = 'Sunday'
for i in range(len(trips5)):
    if trips5['Day'][i] % 7 == 0 :
        Weekday[i] = 'Monday'



#for i in range(len(trips3)):
#    weekday = dttm.datetime(trips3_temp['pickup_datetime'][i]).strftime("%w")
#    Weekday[i] = weekday

trips5['Weekday'] = Weekday
# the outcome of 3.6
print(trips5)

# 3.7 --------------------------------------------------------------------

trips6 = trips5
trips6 = trips6.loc[trips6['Count'] >= 2]
# the outcome of 3.7
print(trips6)

#trips6_temp = trips6[['Zipcode', 'Count']].groupby('Zipcode').sum()

# 3.8 --------------------------------------------------------------------

avg_Temp = trips6[['Hour', 'Temp']].groupby('Hour').mean()

total_Count = trips6[['Hour', 'Count']].groupby('Hour').sum()

trips7 = pd.concat([avg_Temp, total_Count], axis=1)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(trips7['Count'], 'g-')
ax2.plot(trips7['Temp'], 'b-')

ax1.set_xlabel('Hour')
ax1.set_ylabel('Total Counts', color='g')
ax2.set_ylabel('Avg Temperature', color='b')

plt.show()










# below are scratches
#trips7 = pd.merge(avg_Temp, total_Count, on = 'Index')
#trips7 = pd.DataFrame(trips6.groupby('Hour')).count().iloc[:, 0])
#trips7 = trips6.groupby('Hour').sum('Count')
#plt.plot(trips7['Count'])
#plt.plot(secondary_y=True, trips7['Temp'])







