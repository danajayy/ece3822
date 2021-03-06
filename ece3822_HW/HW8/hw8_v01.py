#!/usr/bin/env python

import sys # need sys to parse command line

counter = 0 # counter for number of files with word spike
wordcount = {} # empty variable to hold word count

# reading file that contains all the file names in data_v00 directory
#
with open(sys.argv[1], "r") as datafiles :

    # each line in input file is a path to .txt file in data_v00
    #
    for openfile in datafiles :

        # remove the newline character from end of line
        #
        fp = open(openfile.rstrip("\n")).read()
        
        # checks if spike appears in current file (fp)
        # 
        if "spike" in fp :#open(fp).read() :
            counter = counter + 1 # if so, add 1 to counter
            for i in fp.split() :
                if i in wordcount :
                    wordcount[i] += 1
                else :
                    wordcount[i] = 1
                
    # print result!! :)
    #
    print "A total of %d files contain the word spike." % counter
    for words in wordcount :
        print "%s : %d" % (words, wordcount[words])
               
