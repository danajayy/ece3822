#!/usr/bin/env python

from foo_04 import *
import sys

def main (argv) :

    # save the ranges of the months in a dictionary
    #
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

    x = PrimeDates()

    # reading in data from file
    #
    primedates.read_file(sys.argv[1])

    # manipulate data, get results and output
    #
    primedates.convert(x.data)
    
# end of main function

