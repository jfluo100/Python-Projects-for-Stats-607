# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 20:34:45 2018

@author: lj
"""
import math


def percent(data):
    """
    This function is used to compute the 10th, 25th, 75th and 90th percentile
    Input:
        data: list
    Output:
        percent_data: list    
    """
    sort_data = sorted(data)
    percent_data = [sort_data[math.floor(i*len(sort_data))] for i in [0.10, 0.25, 0.75, 0.90]]
    return percent_data

# discarted former function
def get_row_number(row):
    # It prints the row number of the first line in each min
    num = [0]
    for i in range(1,len(row)):
        if row[i].minute != row[i-1].minute:
            num.append(i)
        else:
            pass
    return num

#def percentiles(data, length, percentile):
    