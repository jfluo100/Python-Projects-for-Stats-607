import statistics
import math
import random
#import assignment1_Data as d1Data
#crime = d1Data.get_US_crime()
#crimeRates = d1Data.get_US_crime_rates()
#crimeRatesOriginal = d1Data.get_US_crime_rates()

def equal_length(crime):
    """1.2 This function trys to know if the lists inside the crimes list are of the same length."""
    length = len(crime[0])
    for i in range(len(crime)):
        boo = length == len(crime[i])
        if boo == False:
            return(False)
            break
    return(True)
    
def get_states(crime):
    """1.3 This function creates a list of strings with the name of the states included in the crimes
list."""
    statelist = []
    for i in range(len(crime)-1):
        statelist.append(crime[i][0])
    return statelist

def equal_vc(crime):
    """1.4.1 This function sees if the total number of violent crimes is equal to the ‘Violent crime
total’ column."""
    totalvc = crime[len(crime)-1][2]
    sumvc = 0
    for i in (3,4,5,6):
        sumvc = sumvc + crime[len(crime)-1][i]
    boo = totalvc == sumvc
    return(boo)
    
def equal_pc(crime):
    """1.4.2 This function sees if the total number of property crimes is equal to the
‘Property crime total."""
    totalpc = crime[len(crime)-1][7]
    sumpc = 0
    for i in (8,9,10):
        sumpc = sumpc + crime[len(crime)-1][i]
    boo = totalpc == sumpc
    return(boo)

def equal_total(crime):
    """1.5 To show that total values equals to the sum of each state"""
    total = [0] * len(crime[0])
    total[0] = crime[len(crime)-1][0]
    for i in range(0,len(crime)-1):
        for j in range(1,len(crime[0])):
            total[j] =total[j] + crime[i][j]
    boo = total == crime[len(crime)-1]
    return(boo)
    
def get_crime_rate(crime):#=d1Data.get_US_crime()
    """1.6 This function creates an identical list to crimes with the crime rate per 100,000 population."""
    crimeRates_list = []
    for i in range(0,len(crime)):
        crimeRates = list(crime[i])
        crimeRates[2:] = list(round(100000*crimeRates[j]/crimeRates[1],1) for j in range(2,len(crime[0])))
        crimeRates_list.append(crimeRates)
    return(crimeRates_list)
    
def equal_rates(n, crime, crimeRatesOriginal):
    """1.7 To show if the two lists have the same vavlue."""
    #crimeRatesOriginal = d1Data.get_US_crime_rates()
    crimeRate = get_crime_rate(crime)
    Original_list = []
    My_list = []
    for i in range(n):
        a = random.randint(0, len(crime)-1)
        b = random.randint(0, len(crime[0])-1)
        Original_list.append(crimeRatesOriginal[a][b])
        My_list.append(crimeRate[a][b])
    boo = Original_list == My_list
    return(boo)
        
def top5_violent_states(crimeRates):
    """1.8 Creates a dictionary of top 5 states with the highest violent crime rate"""
    #crimeRates = d1Data.get_US_crime_rates()
    vr_hi = sorted(crimeRates, key = lambda a:(a[2]), reverse = True)
    vr_hi_5 = vr_hi[:][0:5]
    dic_vr = dict()
    for i in range(5):
        dic_vr[vr_hi_5[i][0]] = vr_hi_5[i][2]
    return(dic_vr)
    
def top_crime_states(n, crime, indexCrime):
    """1.9 Returns the dictionary of top n states with the
highest given crime rate."""
    #0 for Violent Crime rate
    #1 for Murder and nonnegligent manslaughter rate	
    #2 for Rape
    #3 for Robbery rate	
    #4 for Aggravated assault rate	
    #5 forProperty crime rate	
    #6 for Burglary rate	
    #7 Larceny-theft rate	
    #8 for Motor vehicle theft rate
    crime_rates = get_crime_rate(crime)
    if n <= 0 or n >= len(crime):
        print('"n" should be a positve integer that is no larger than the lenth of the list!')
        return()
    if indexCrime < 0 or indexCrime > 8:
        print('"crime" should between 0 and 8 (inclusive)')
        print('#0 for Violent Crime rate\
              \n#1 for Murder and nonnegligent manslaughter rate\
              \n#2 for Rape\
              \n#3 for Robbery rate\
              \n#4 for Aggravated assault rate\
              \n#5 for Property crime rate\
              \n#6 for Burglary rate\
              \n#7 for Larceny-theft rate\
              \n#8 for Motor vehicle theft rate'
              )
        return()
    dic_of_crimes = {0:'Violent Crime rate',
                     1:'Murder and nonnegligent manslaughter rate',
                     2:'Rape rate',
                     3:'Robbery rate',
                     4:'Aggravated assalt rate',
                     5:'Property crime rate',
                     6:'Burglary rate',
                     7:'Larceny-theft rate',
                     8:'Motor vehicle theft rate'
                     }
    print('You are looking for states with highest!', dic_of_crimes[indexCrime])
    dic_n_cr = dict()
    #sort the list by the crime give
    sorted_by_crime = sorted(crime_rates, \
                             key = lambda a:(a[2+indexCrime]), \
                             reverse = True)
    
    for i in range(n):
        dic_n_cr[sorted_by_crime[i][0]] = sorted_by_crime[i][2+indexCrime]
    return(dic_n_cr)
    
def crime_stats(index, crimeRates):
    "1.10 Returns the mean, std and var of a give crime rate"
    if index < 0 or index > 8:
        print('"crime" should between 0 and 8 (inclusive)')
        print('#0 for Violent Crime rate\
              \n#1 for Murder and nonnegligent manslaughter rate\
              \n#2 for Rape\
              \n#3 for Robbery rate\
              \n#4 for Aggravated assault rate\
              \n#5 for Property crime rate\
              \n#6 for Burglary rate\
              \n#7 for Larceny-theft rate\
              \n#8 for Motor vehicle theft rate'
              )
        return()
    dic_of_crimes = {0:'Violent Crime rate',
                     1:'Murder and nonnegligent manslaughter rate',
                     2:'Rape rate',
                     3:'Robbery rate',
                     4:'Aggravated assalt rate',
                     5:'Property crime rate',
                     6:'Burglary rate',
                     7:'Larceny-theft rate',
                     8:'Motor vehicle theft rate'
                     }
    print('You are looking for states with highest!', dic_of_crimes[index])
    lcrime = []
    #crimeRates = d1Data.get_US_crime_rates()
    for i in range(0,len(crimeRates)-1):
        lcrime.append(crimeRates[i][2+index])
    avg = statistics.mean(lcrime)
    std = math.sqrt(statistics.variance(lcrime))
    var = statistics.variance(lcrime)
    return(avg, std, var)