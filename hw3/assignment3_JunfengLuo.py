import os
import math
import gzip
###############################################################################
# convert to float
def myfloat(x):
    try:
        return float(x)
    except:
        return float('nan')
#```
#Input:
#    x:str
#    
#Output:
#    out:float
#```
###############################################################################
# read each line (discarted)
def read_line(f):
    try:
        return f.readline()
    except:
        return ""
#```
#Input:
#    f:file
#    
#Output:
#    out:line
#```
###############################################################################
# divide them
def do_parse_file(filepath, onlyTraffic = False):
    allBridges = []
    f = gzip.open(filepath, 'r')
    while True:
        line = ''
        try:
            line = f.readline().decode()
        except:
            continue
        if line == None or len(line) == 0:
            break
        #print(line)
        #only Highway Bridge: Item 5a = 1; Item 49> = 6.1 meters; Item 112 = Y; and Item 42a = 1 or 4 or 5 or 6 or 7 or 8.
        item5a = myfloat(line[18:19])
        item49 = myfloat(line[222:228])
        item112 = line[373:374]
        item42a = myfloat(line[199:200])
        notHightWayCnt = 0
        if item5a != 1 or item49 < 6.1 or item112 != 'Y' or item42a not in (1, 4, 5, 6, 7, 8):
            notHightWayCnt = notHightWayCnt + 1
            continue
            
        #print("item5a, item49, item112, item42a:", item5a, item49, item112, item42a)
        #structure number, state, year built, year reconstructed, structure length, average daily traffic
        params = []
        if not onlyTraffic:
            params.append(line[3:18])
            params.append(line[0:3])
            params.append(line[156:160])
            params.append(line[361:365])
            params.append(myfloat(line[222:228]))
            params.append(myfloat(line[164:170]))
        else:
            params.append(line[3:18])
            params.append(myfloat(line[164:170]))
        allBridges.append(params)
        #print("Params:", params)
    #print("item5a, item49, item112, item42a:", item5a, item49, item112, item42a, ", notHightWayCnt:", notHightWayCnt)
    #print(allBridges)
    return allBridges
#```
#Input:
#    filepath:str
#    
#Output:
#    out:list
#```
###############################################################################
###############################################################################
# read the file is a hard job (discarded)
#def readitplz(filepath, year):
#    L = []
#    whichYear_path = os.path.join(filepath, str(year))
#    files = os.listdir(whichYear_path)
#    for file in files:
#        path = os.path.join(whichYear_path, file)
#        with gzip.open(filepath, 'rt') as f:
#            if not onlyTraffic:
#                params.append(line[3:18])
#                params.append(line[0:3])
#                params.append(line[156:160])
#                params.append(line[361:365])
#                params.append(myfloat(line[222:228]))
#                params.append(myfloat(line[164:170]))
#            else:
#                params.append(line[3:18])
#                params.append(myfloat(line[164:170]))
#                allBridges.append(L)
#        #print("Params:", params)
#    return allBridges
#```
#Input:
#    filepath:str
#    
#Output:
#    out:list
#```
###############################################################################
###############################################################################







## core answers are starting from here

# for 1.1
def get_most_bridges_state(datas):
    maxCnt = - 1
    maxStateCode = ''
    for k in datas.keys():
        if datas[k] > maxCnt:
            maxCnt = datas[k]
            maxStateCode = k
    return maxStateCode
#```
#Input:
#    datas:dict
#    
#Output:
#    out:str ( convert it to float later ! )
#```
###############################################################################
# for 1.2
def get_short_long_state(avgLenBridges):
    if len(avgLenBridges) == 0:
        return ()
    #get one item as initial value
    for k in avgLenBridges.keys():
        firstKey = k
        break
    longSate = firstKey
    shortState = firstKey
    longValue = avgLenBridges[firstKey]
    shortValue = avgLenBridges[firstKey]
    for k in avgLenBridges.keys():
        if avgLenBridges[k] > longValue:
            longValue = avgLenBridges[k]
            longSate = k
        if avgLenBridges[k] < shortValue:
            shortValue = avgLenBridges[k]
            shortState = k
    return tuple([shortState, longSate])
#```
#Input:
#    filepath:dic
#    
#Output:
#    out:tupe
#```
###############################################################################
# for 1.3
def get_avg_rebuild_year(datas):
    totalDuration = 0
    bridgeCnt = 0
    for i in range(len(datas)):
        # skip this bridge which rebuild time is 0000
        if datas[i][3] == '0000':
            continue
        firstbuild = myfloat(datas[i][2])
        rebuild = myfloat(datas[i][3])
        if math.isnan(firstbuild) or math.isnan(rebuild) or rebuild <= firstbuild:
            continue
        
        totalDuration = totalDuration  + (rebuild - firstbuild)
        bridgeCnt = bridgeCnt  + 1
    if bridgeCnt > 0:
        return (totalDuration / bridgeCnt)
    else:
        return 0
     #```
#Input:
#    filepath:list
#    
#Output:
#    out:float
#```
###############################################################################   
# for 1.4
#get average percentage change in average daily traffice from 2000 to 2010

def get_avg_perchg_traffic(datas):
    everyYearAvg = []
    yearAry = []
    #get every year's average daily traffic
    for year in datas.keys():
        yearData = datas[year]
        thisYearTotal = 0
        thisYearCnt = 0
        for i in range(len(yearData)):
            #skip this bridge if the average traffic is not valid
            if math.isnan(yearData[i][1]):
                continue
            thisYearTotal = thisYearTotal + yearData[i][1]
            thisYearCnt = thisYearCnt + 1
        if thisYearCnt > 0:
            everyYearAvg.append(thisYearTotal / thisYearCnt)
            yearAry.append(year)
    totalPerChg = 0
    #print("everyYearAvg:", everyYearAvg)
    #print("yearAry:", yearAry)
    for i in range(len(everyYearAvg) - 1):
        totalPerChg = totalPerChg  + ((everyYearAvg[i + 1] - everyYearAvg[i]) / everyYearAvg[i])
    if len(everyYearAvg) - 1 > 0:
        return totalPerChg / (len(everyYearAvg) - 1)
#```
#Input:
#    filepath:dict
#    
#Output:
#    out:float
#```
###############################################################################
# for 1.5
def get_pro_inc_traffic(datas):
    #get every bridges's average daily traffic in each year, key is year
    #allAvg = {"struct#":[year1 traffic, year2 traffic]}
    allAvg = {}
    for year in datas.keys():
        yearData = datas[year]
        #thisYearAvg = {"struct#":[total_avg, count]...}
        thisYearAvg = {}
        for i in range(len(yearData)):
            structNo = yearData[i][0]
            #skip this bridge if the average traffice is not valid
            if math.isnan(yearData[i][1]):
                continue
            if structNo not in thisYearAvg.keys():
                thisYearAvg[structNo] = [yearData[i][1], 1]
            else:
                thisYearAvg[structNo][0] = thisYearAvg[structNo][0] + yearData[i][1]
                thisYearAvg[structNo][1] = thisYearAvg[structNo][1] + 1
        for k in thisYearAvg.keys():
            avg = (thisYearAvg[k][0] / thisYearAvg[k][1])
            if k in allAvg.keys():
                allAvg[k].append(avg)
            else:
                allAvg[k] = [avg]
    #count bridge count which saw increased traffic
    incCnt = 0
    for k in allAvg.keys():
        isInc = True
        everyYearData = allAvg[k]
        if everyYearData == None:
            continue;
        for i in range(len(everyYearData) - 1):
            if everyYearData[i] > everyYearData[i + 1]:
                isInc = False
                break;
        if isInc:
            incCnt = incCnt + 1
    return (incCnt / len(allAvg)) if len(allAvg) > 0 else 0
#```
#Input:
#    filepath:dict
#    
#Output:
#    out:float
#```
###############################################################################
# for 1.6
def get_avg_rebuild_year_group_sate(datas):
    allAvg = {}
    curState = datas[0][1]
    totalDuration = 0
    bridgeCnt = 0
    for i in range(len(datas)):
        if bridgeCnt>0 and (curState != datas[i][1] or i == (len(datas) - 1)):
            allAvg[curState] = (totalDuration / bridgeCnt)
            totalDuration = 0
            bridgeCnt = 0
            curState = datas[i][1]
        else:
            #skip this bridge which rebuild time is 0000
            if datas[i][3] == '0000':
                continue
            firstbuild = myfloat(datas[i][2])
            rebuild = myfloat(datas[i][3])
            if math.isnan(firstbuild) or math.isnan(rebuild) or rebuild <= firstbuild:
                continue
            
            totalDuration = totalDuration + (rebuild - firstbuild)
            bridgeCnt = bridgeCnt + 1
    return allAvg
#```
#Input:
#    filepath:list
#    
#Output:
#    out:float
#```
###############################################################################
def get_avg_len(datas):
    allAvg = {}
    if len(datas) == 0:
        return {}
    curState = datas[0][1]
    totalLen = 0
    bridgeCnt = 0
    for i in range(len(datas)):
        if bridgeCnt>0 and (curState != datas[i][1] or i == (len(datas) - 1)):
            allAvg[curState] = (totalLen / bridgeCnt)
            totalLen = 0
            bridgeCnt = 0
            curState = datas[i][1]
        else:
            #skip this bridge if the length is not valid
            if math.isnan(datas[i][4]):
                continue
            totalLen = totalLen + datas[i][4]
            bridgeCnt = bridgeCnt + 1
    return allAvg
#```
#Input:
#    filepath:list
#    
#Output:
#    out:dict
#```
###############################################################################
def parse_file_by_folder(rootDir, year, onlyTraffic = False):
    allStateDatas = []
    stateCount = {}
    fullPath = '%s%s%d'%(rootDir, os.sep, year)
    if not os.path.exists(fullPath):
        print("Please confirm exists folder: %s"%(fullPath))
        return
    for root, sub_dirs, files in os.walk(fullPath):
        print ('root: %s, files:'%(root), files)
        for f in files:
            #only read *.gz file
            if '.gz' not in f:
                continue
            stateData = do_parse_file(root  + os.sep  + f, onlyTraffic)
            allStateDatas = allStateDatas + stateData
            if len(stateData) > 0:
                stateCode = stateData[0][1]
                stateCount[stateCode] = len(stateData)
    return allStateDatas, stateCount
#```
#Input:
#    filepath:str
#    
#Output:
#    out:list
#```
###############################################################################
#def parse_file(rootDir, year, onlyTraffic = False): # Ture or false here matters
#    allStateDatas = []
#    stateCount = {}
#    for root, sub_dirs, files in os.walk('%s\\%d'%(rootDir, year)):
#        print ('root: %s, files:'%(root), files)
#        for f in files:
#            stateData = do_parse_file(root  + "\\"  + f, onlyTraffic)
#            allStateDatas = allStateDatas + stateData
#            if len(stateData) > 0:
#                stateCode = stateData[0][1]
#                stateCount[stateCode] = len(stateData)
#    return allStateDatas, stateCount
#```
#Input:
#    filepath:str
#    
#Output:
#    out:list
#```
###############################################################################
###############################################################################
    
# Jesus help me read this file plz
#def parse_file_by_zipfile(zipPath, onlyTraffic = False):
#    allStateDatas = []
#    stateCount = {}
#    if not os.path.exists(zipPath):
#        print("Please confirm exist zip file: %s"%(zipPath))
#        return
#    z = zipfile.ZipFile(zipPath, "r")
#    print("parse file", zipPath, z.namelist())
#    for filename in z.namelist():
#        f = z.open(filename)
#        stateData = do_parse_file('', onlyTraffic, zipFile = f)
#        allStateDatas = allStateDatas + stateData
#        if len(stateData) > 0:
#            stateCode = stateData[0][1]
#            stateCount[stateCode] = len(stateData)
#    z.close()
#    return allStateDatas, stateCount
#```
#Input:
#    zipPath:str
#    
#Output:
#    out:list, list
#```
###############################################################################
#def parse_file_by_folder(rootDir, year, onlyTraffic = False):
#    allStateDatas = []
#    stateCount = {}
#    fullPath = '%s%s%d'%(rootDir, os.sep, year)
#    if not os.path.exists(fullPath):
#        print("Please confirm exists folder: %s"%(fullPath))
#        return
#    for root, sub_dirs, files in os.walk(fullPath):
#        print ('root: %s, files:'%(root), files)
#        for f in files:
#            #only read *.gz file
#            if '.gz' not in f:
#                continue
#            stateData = do_parse_file(root  + os.sep  + f, onlyTraffic)
#            allStateDatas = allStateDatas + stateData
#            if len(stateData) > 0:
#                stateCode = stateData[0][1]
#                stateCount[stateCode] = len(stateData)
#    return allStateDatas, stateCount
#```
#Input:
#    rootDir:str
#    year:str
#Output:
#    out:list, list
#```
###############################################################################
###############################################################################