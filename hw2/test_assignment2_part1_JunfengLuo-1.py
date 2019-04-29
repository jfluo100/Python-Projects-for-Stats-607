import gzip
import re
import datetime as dttm
import assignment2_JunfengLuo as a2

with gzip.open('maccdc2012_00016.txt.gz','rb') as f:
    file_content = list(item.decode() for item in f)
    
# use part of the data to speed up


#part_file = file_content#[0:40000]  
raw_data1=[line.split('Flag') for line in file_content]
raw_data2=[line[0] for line in raw_data1]
# matchObj = [re.match(r'[0-9]*\:[0-9]*\:[0-9]*', l) for l in data1]



# 1.1
t = []
ip1 = []
ip2 = []

# There are data that does not match my match. They are not wanted, anyway.
for i in raw_data2:
    try:
        #x = re.match(r'(.*) IP (.*) > (.*)', i)
        x = re.match(r'(.*) IP (.*) > ([^\s]*): (.*)$', i)
        t.append(x.group(1))
        ip1.append(x.group(2))
        ip2.append(x.group(3))
    except (AttributeError):
        pass

data = [t] + [ip1] + [ip2]

# Convert all seconds in a minute to the integer minute
# make the time start at the very first second of the minute


time_0 = dttm.datetime.strptime(t[0], '%H:%M:%S.%f')
time_1 = int(str(time_0.hour) + str(time_0.minute)) # 

T = []
for i in range(len(t)):
    T.append(dttm.datetime.strptime(t[i], '%H:%M:%S.%f'))
    
row_num = a2.get_row_number(T)

index = []
temp2 = 0

for i in range(len(t)) :
    temp1 = dttm.datetime.strptime(t[i], '%H:%M:%S.%f')
    temp_t = int(str(temp1.hour)+str(temp1.minute))
    diff_i = temp_t - time_1
    if diff_i != temp2 :
        index.append(i)
        temp2 = diff_i


# 'set' command picks out useful info
      
        
index_1 = [0] + index
ip_distinct = []
ip_nd_len = []
for i in range(len(index_1)):
    if i != len(index_1)-1:
        ip_l = ip1[index_1[i]: index_1[i+1]] + ip2[index_1[i]: index_1[i+1]]
        ip_s = set(ip_l)
        ip_distinct.append(list(ip_s))
        ip_nd_len.append(len(ip_l))
    else:
        ip_l = ip1[index_1[i]:] + ip2[index_1[i]:]
        ip_s = set(ip_l)
        ip_distinct.append(list(ip_s))
        ip_nd_len.append(len(ip_l))

### outcome of 1.1        
ip_distinct_len = [len(i) for i in ip_distinct]
print(ip_distinct_len)

    
# 1.2
### outcome of 1.2        
percent_ip = a2.percent(ip_distinct_len)
print(percent_ip)

# 1.3
#ip = ip1.copy()
#for i in ip2:
#    ip.append(i)
#
#min_len = len(ip_distinct_len)
#ip_dict = {}
#for i in ip:
#    if i in ip_dict:
#        ip_dict[i] = ip_dict[i]+1
#    else:
#        ip_dict[i] = 1


# link ip1 and ip2
for i in ip2:
    ip1.append(i)

min_len = len(ip_distinct_len)
ip_dict = {}
for i in ip1:
    if i in ip_dict:
        ip_dict[i] = ip_dict[i]+1
    else:
        ip_dict[i] = 1



### outcome of 1.3        
avg_ip = list(map(lambda x: x/min_len, list(ip_dict.values())))


# 1.4
### outcome of 1.4        
percent_avg = a2.percent(avg_ip)
print(percent_avg)