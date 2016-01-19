#!/usr/bin/env python

import sys # need sys to parse command line arguments

# this function takes a text file or list and counts
# the frequency of each word/item in file/list
#
def getcount (orig_list) :
    wc = [] # holds the items
    freq = [] # holds frequency of items
    for item in orig_list :
        if item in wc :
            i = wc.index(item)
            freq[i] = freq[i] + 1
        else :
            wc.append(item)
            freq.append(1)
        # end of if statement
    return wc, freq
    # end of for loop
# end of function 

def main(argv) :

    x = len(sys.argv) # get total number of arguments from command line
    wordlist = [] # list to hold words from files
    countlist = [] # list to hold frequency of respected word
    counter = 0 # hold how many words appear in both files

    # loop through all files from command line
    #
    for i in range(1, x) :

        # if first time, start the wordlist and countlist
        #
        if i == 1 :
            fp = open(sys.argv[i]).read() # open and read file
            text = fp.split() # remove all white space from text
            [wordlist, countlist] = getcount(text) # send to getcount function
            
        # if not the first time, need to append all read in text files to
        # wordlist and countlist
        #
        else :
            tempword = [] # temporary list to contain read in file's words
            tempcount = [] # temporary list to contain frequency of words
            fp = open(sys.argv[i]).read() # open and read file
            text = fp.split()
            [tempword, tempcount] = getcount(text) # send argument to getcount function

            for item in tempword :
                if item in wordlist:
                      counter = counter + 1
                # end of if statement
            # end of for loop
                      
        # end of if/else statement
    # end of for loop statement

    print counter
            

# end of main function

if __name__ == "__main__" :
    main(sys.argv[0:])
# end of file
        
