#!/usr/bin/env python

import sys # need sys to parse command line
import string # need .translate() to edit text in files

counter = 0 # counter for number of files with word spike
wordcount = {} # holder for word counts with respected word
wordlist = [] # list to hold words from files
countlist = [] # list holds counts of respected word
percentlist = [] # list holds percentage of word
bigramcount = [] # list hold bigrams of files

# This function takes in text and changes any special characters
# (non-alphabet/numerals) to spaces
#
def charch (text) :
    chars = "/:;~`!@#$%^&*()-_=+" # list of characters that will change
    for c in chars :
        text = text.replace(c, " ")
    return text

# This function converts from dictionary to list ( 2 lists, one list for
# the key names and 2nd list for the key values)
#
def dict2list (d) :
    list1 = [] # will hold keys
    list2 = [] # will hold values
    
    # putting wordcount into 2 lists, one for the words and one for the values
    # need to convert from dictionary to list so can sort it
    #
    for key, val in d.items() :
        list1.append(key)
        list2.append(val)

    return list1, list2
    
# This function takes in a text and counts how many times each word occurs
# and saves them in a dictionary which will be returned to main function
#
def countwords (text) :
    wc = {}
    
    # for words in the file, fp, separate and remove all whitespace
    #characters this for loop will count the number of word occurences
    #
    for i in text.split() :
        i = i.lower()
        # if word is already in wordcount dictionary, add 1 to count
        # else, add the word to dictionary and start with 1
        #
        if i in wc :
            wc[i] += 1
        else :
            wc[i] = 1

    return wc

# this function gets the bigram of each file by reading each
# line of text from file and saves each bigram as a list
# and stores each sublist into list result
#
def bigrams (text) :
    result = []
    text = text.lower()
    arr = text.split()
    for i in range(len(arr)) :
        if i < len(arr) - 1 :
            result.append([arr[i], arr[i+1]])
    print result
    return result


# reading file that contains all the file names in data_v00 directory
#
with open(sys.argv[1], "r") as datafiles :

    # each line in input file is a path to .txt file in data_v00
    #
    for openfile in datafiles :

        # remove the newline character from end of line
        #
        fp = open(openfile.rstrip("\n")).read()
        
        # checks if spike appears in current file, fp
        # 
        if "spike" in fp :
            counter = counter + 1 # holds number of files with "spike"
            fp = charch(fp)
            bigramcount.append(bigrams(fp))
            wordcount = countwords(fp)
            [wordlist, countlist] = dict2list(wordcount)

    # sorts countlist and wordlist simultaneously so that the words and counts
    # that correspond with each other are the same
    #
    countlist, wordlist = (list(t) for t in zip(*sorted(zip(countlist, wordlist))))

    # sum up the total words
    #
    wordsum = sum(countlist)

    # get the percentage of each word occurrence
    #
    for i in range(0,len(countlist)) :
        percentlist.append((float(countlist[i])/wordsum)*100)

    # get the average amount of words in each file
    #
    avg = float(wordsum/counter)

    # lists sorts from least to most, want to reverse to most to least
    #
    wordlist = list(reversed(wordlist))
    countlist = list(reversed(countlist))
    percentlist = list(reversed(percentlist))
    
    # print result!! :)
    #

    print bigramcount
#    print "-------------------------"
#    print "1-word Sequence Histogram"
#    print "-------------------------"
    
#    for i in range(0,len(wordlist)) :
#        print " %s : %d (%f %%)" % ( wordlist[i], countlist[i], percentlist[i] )


#    print "-------------------------"
#    print "A total of %d files contained the word spike." % counter

#    print "A total of %d words occurred in %d files: the average number of words per file is: %f" % (wordsum, counter, avg)
               
