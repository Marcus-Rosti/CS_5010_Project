# -*- coding: utf-8 -*-
"""
Check if updates are needed

Created on Fri Jul 31 12:22:51 2015

@author: Nathan Harmon
"""

def update(filename):
    #returns last date and current date in unix time
    
    import csv
    #pull the last date from the file
    #reads in all the times and finds the max
    times = [] 
    with open(filename) as csvfile:
        lines = csv.reader(csvfile)
        next(lines, None) #skips the header
        for line in lines:
            times.append(int(line[0]))
    last = max(times)
    
    #get the current time
    import time
    current = int(time.time())
    
    return last, current

def gapFiller(filename):
    #Finds the largest gap in the record
    #returns the first and last date on either side of the gap, in unix time
    #Returns zeros  if nothing larger than an hour
        
    import csv
    #reads in all the times
    times = [] 
    with open(filename) as csvfile:
        lines = csv.reader(csvfile)
        next(lines, None) #skips the header
        for line in lines:
            times.append(int(line[0]))
    #sort the times
    times.sort()
    #Itterate over the loop, finding the max gap and position
    i = j = g = 0
    while i < len(times)-1:
        if times[i+1] - times[i] > g:
            j = i
            g = times[i+1]-times[i]
        i += 1
    
    #See if the gap is larger than an hour
    if g <= 3600:
        return 0, 0
    else:
        return times[j], times[j+1]