#!/usr/bin/env python

import sys # need sys to parse command line

counter = 0 # counter for number of files with word spike

# reading file that contains all the file names in data_v00 directory
#
with open(sys.argv[1], "r") as datafiles :

    # each line in input file is a path to .txt file in data_v00
    #
    for openfile in datafiles :

        # remove the newline character from end of line
        #
        fp = openfile.rstrip("\n")

        # checks if spike appears in current file (fp)
        # 
        if "spike" in open(fp).read() :
            counter = counter + 1 # if so, add 1 to counter 

    # print result!! :)
    #
    print "A total of %d files contain the word spike." % counter
               
