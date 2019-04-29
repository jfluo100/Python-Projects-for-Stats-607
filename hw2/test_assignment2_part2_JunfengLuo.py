import numpy as np
import matplotlib.pyplot as plt
source_data = open("adverseCountsFinal.txt")


# Q-2.1
data = np.loadtxt(source_data).astype(np.int32)


# Q-2.2
sum = np.sum(data[:,1:], axis=0)  # Years needn't be included in sums.

sum_Serious = sum[0]
sum_Death = sum[1]
sum_Non_Serious = sum[2]

# Q-2.3
# Attention that first parameter of data[] is row and second is column
sum_year = np.sum(data[:,1:], axis=1) 

# Q-2.4

# Highest for Serious Reports
#data[np.argmax(data[:,1]), 0]

print(data[np.argmax(data[:,1]), 0], 'has highest number of reports for "Serious"')

# Highest for Death Reports
#data[np.argmax(data[:,2]), 0]

print(data[np.argmax(data[:,2]), 0], 'has highest number of reports for "Death"')

# Highest for Non-Serious Reports
#data[np.argmax(data[:,3]), 0]

print(data[np.argmax(data[:,3]), 0], 'has highest number of reports for "Non-Serious"')

# Q-2.5
data_2_5 = data.copy()
max_of_year = np.argmax(data[:,1:4], axis = 1)
np.asarray(max_of_year)
dic = dict()
dic[0] = 'Serious'
dic[1] = 'Death'
dic[2] = 'Non-Serious'

print('The type of side effect that has been reported the most are:')

# using for-loop can make my output more readable but it may be prohibitted.

### outcome of 2.5
for i in range(len(data)):# for the solution without using for, look downward:
    print(2018-i, ':', dic[max_of_year[i]])
    
#not using for:
print(max_of_year, 'where 1 stands for "Serious", 2 stands for "Death", 3 stands for "Non-Serious')
    

    
# Q-2.6
data_2_6 = np.delete(data, 0, axis = 1)
sum_year = np.sum(data_2_6, axis = 1)
sum_year.shape = (51, 1)

proportion = np.round(data_2_6 / sum_year, 3)
proportion_year = np.vstack([np.asarray(['Serious', 'Death', 'Non-Serious']), proportion])

### outcome of 2.6
print(proportion_year)

# Q-2.7
plt.stackplot(data[:, 0], data[:, 1], data[:, 2], data[:, 3], labels = ['Serious', 'Death', 'Non-Serious'])
plt.legend(loc="upper left")
plt.xlabel('Year')

