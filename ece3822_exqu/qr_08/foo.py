#!/usr/bin/env python

# using the sys library to be able to parse command line information
#
import sys

# while opening the file sent in from the 2nd argument on command line
# it isn't the 1st argument because the 1st argument is the name of the
# python script; and the arguments are indexed starting with 0
# the read info is stored in variable f
#
with open(sys.argv[1], "r") as f :
        
        # declaring an empty list to hold the read info
        #
        x = []

        # a for loop that goes through each line in variable f
        #
        for line in f :

                # split the line in f at the :
                # result of split is that key name and key value are stored
                # as separate string values in a list
                #
                listedline = line.strip().split(':')

                # append the 1-index of listedline into x, which holds the value
                # since the value is a string type, convert to float type
                # because there are decimal values in the file
                #
                x.append(float(listedline[1]))

        # print that result yo, by summin' up them values using the sum function
        # convert to int because you wanted "27," not "27.0"
        #
        print int(sum(x))

