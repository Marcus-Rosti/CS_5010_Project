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
