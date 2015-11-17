#!/usr/bin/env python

import sys

data = []

with open(sys.argv[1]) as fp :
    for line in fp :
#        line = line.strip()
        line = line.replace(","," ")
        line = line.strip()
        data.append(line)
    m = [i.split() for i in data]

    print m

months = { 'January' : range(1,31), # 31 days
           'February' : range(32, 59), # 28 days
           'March' : range(60, 90), # 31 days
           'April' : range(91,120), # 30 days
           'May' : range(121, 151), # 31 days
           'June' : range(152, 181), # 30 days
           'July' : range(182, 212), # 31 days
           'August' : range(213, 243), # 31 days
           'September' : range(244, 273), # 30 days
           'October' : range(274, 304), # 31 days
           'November' : range(305, 334), # 30 days
           'December' : range(335, 365) } # 31 days

result = []

for dates in m :
    if dates[0] in months :
        days = months[dates[0]]
        if int(dates[1]) <= int(len(months[dates[0]])+1) :
            num = days[int(dates[1])-1]
            result = [' '.join(dates[0:2])+',', dates[2]]
            result = ' '.join(result)
#            print "%s corresponds to the integer %d." % (result, num)
        else :
            print "Invalid Input : %d is out of range of month %s" % (int(dates[1]), dates[0])
        # end of if/else statement
    else :
        print "Invalid Input : No month called %s" % dates[0]
    # end of if/else statement
# end of for loop

               
