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
        
        # declaring an empty dictionary to hold the read info
        #
        x = {}

        # a for loop that goes through each line in variable f
        #
        for line in f :

                # split the line in f at the =
                # result of split is that key name and key value are stored
                # as separate string values in a list
                #
                linestrip = line.strip().split('=')

                # env. variable is stored in 0th element, assign to keyval
                #
                keyval = linestrip[0]

                # apparently not all env. vars have a value to it, so have
                # to take care of case when there is no value...
                #
                if len(linestrip) < 2 :
                        val = ' ' # make value empty for env. var w/o value
                else:
                        val = linestrip[1] # env. var has value, assign to val

                # load dictionary
                #
                x[keyval] = val

        # let's print it!! :) hopefully this works...
        #
        print x


