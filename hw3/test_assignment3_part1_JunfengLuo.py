#import os
#import math
#import gzip
import assignment3_JunfengLuo as a3



#if __name__ == '__main__':
L = [[], [], []] # compute L as required
allStateDatas = []
rootDir = "."
for i in [0, 1, 2]:
    allStateDatas_temp, stateCount = a3.parse_file_by_folder(rootDir, 2000 + i*5, onlyTraffic = False)
    L[i] = allStateDatas_temp
    allStateDatas = allStateDatas + allStateDatas_temp # Combine 3 years together

stateWithMostBridges = float(a3.get_most_bridges_state(stateCount)) # outcome of 1.1
avgLenBridges = a3.get_avg_len(allStateDatas) # outcome of 1.2
shortLongStates = a3.get_short_long_state(avgLenBridges) # outcome of 1.3
avgRebuild = a3.get_avg_rebuild_year(allStateDatas) # outcome of 1.4

#save every year's data in dictionary
batchYearData = {}
for i in [0, 5, 10]:
    if i == 5:
        continue
    allStateDatasnew, stateCount = a3.parse_file_by_folder(rootDir, 2000 + i, onlyTraffic = True)
    batchYearData["%d"%(2000 + i)] = allStateDatasnew
propIncTraffice = a3.get_pro_inc_traffic(batchYearData) # outcome of 1.5
avgPercentChange = a3.get_avg_perchg_traffic(batchYearData) # outcome of 1.6

# outcome of 1.1 - - Texas is the state with most bridges
print("stateWithMostBridges:", stateWithMostBridges)
# outcome of 1.2
print("avgLenBridges:", avgLenBridges)
# outcome of 1.3 - - Nebraska and D.C.
print("shortLongStates:", shortLongStates)
# outcome of 1.4
print("avgRebuild:", avgRebuild)
# outcome of 1.5
print("propIncTraffice:", propIncTraffice)
# outcome of 1.6
print("avgPercentChange:", avgPercentChange)










#rootDir = "E:\\um607hw\\pro3"
#allStateDatas, stateCount = parse_file(rootDir, 2000, False)
#print(stateCount)
