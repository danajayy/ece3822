#!/usr/bin/env python

import sys # need sys to parse command line

# variables needed for this program
#
counter = 0 # counter for number of files with word spike
wordcount = {} # holder for word counts with respected word
wordlist = [] # list to hold words from files
countlist = [] # list holds counts of respected word
percentlist = [] # list holds percentage of word
bigram = [] # gets bigrams from text file
bigramdic = {} # holds occurrence of each bigram
bicount = [] # holds frequency(value) of bigram from bigramdic
biwords = [] # holds bigram(key) from bigramdic
bipercent = [] # hold percentage of bigram frequency

# This function takes in text and changes any special characters
# (non-alphabet/numerals) to spaces
#
def charch (text) :
    chars = ".,?/:;~`!@#$%^&*()-_=+" # list of characters that will change
    for c in chars :
        text = text.replace(c, " ")
    return text
# end of function

def dict2list (dic) :
    keylist = []
    vallist = []
    for key, val in dic.items() :
        keylist.append(key)
        vallist.append(val)
    #end of for loop
    return keylist, vallist
# end of function

def getpercent (lst, listsum) :
    temp = []
    for i in range(0,len(lst)-1) :
        temp.append((float(lst[i])/listsum)*100)
    # end of for loop
    return temp
# end of function

# reading file that contains all the file names in data_v00 directory
#
with open(sys.argv[1], "r") as datafiles :

    # each line in input file is a path to .txt file in data_v00
    #
    for openfile in datafiles :
        c = c + 1
        # remove the newline character from end of line
        #
        fp = open(openfile.rstrip("\n")).read()

        # checks if spike appears in current file, fp
        # 
        if "spike" in fp :
            counter = counter + 1 # if so, add 1 to counter
            fp = charch(fp)

            # remove all white space from text file
            text = fp.split()

            # create bigram of words from text and save bigrams as sublists
            # into bigram list
            #
            for i in range(len(text)) :
                if i < len(text) - 1 :
                    bigram.append([text[i].lower(), text[i+1].lower()])
                # end of if statement
            # end of for loop

            # count frequency of bigrams from bigram and save into bicount
            # sublists must be turned into tuples since lists are mutable
            # and key values in dictionaries must be immutable, tuples
            # are immutable
            #
            for i in bigram :
                i = tuple(i)
                if i in bicount :
                    bigramdic[i] += 1
                else :
                    bigramdic[i] = 1
                # end of if statement
            # end of for loop

            # loop will count the number of word occurences 
            #
            for word in text :
                # if word is already in wordcount dictionary, add 1 to count
                # else, add the word to dictionary and start with 1
                #
                if word in wordcount :
                    wordcount[word] += 1
                else :
                    wordcount[word] = 1
                # end of if statement
            # end of for loop
        # end of if statement (that checks if file contains "spike")
    # end of for loop (for loop that loops through files)

    [wordlist, countlist] = dict2list(wordcount)
    [biwords, bicount] = dict2list(bigramdic)
    
    # sorts countlist and wordlist simultaneously so that the words and counts
    # that correspond with each other are the same
    #
    countlist, wordlist = (list(t) for t in zip(*sorted(zip(countlist, wordlist))))

    wordsum = sum(countlist) # sum of total words
    bigramsum = sum(bicount) # sum of total bigrams
    
    avg = float(wordsum/counter) # get avg amt words per file
    biavg = float(bigramsum/counter) # get avg amt bigrams per file

    # calculating the percentage of 
    percentlist = getpercent(countlist, wordsum)
    bipercent = getpercent(bicount, bigramsum)

    # lists sorts from least to most, want to reverse to most to least
    #
    wordlist = list(reversed(wordlist))
    countlist = list(reversed(countlist))
    percentlist = list(reversed(percentlist))
    
    # print result!! :)
    #
    
    print "-------------------------\n"
    print "1-word Sequence Histogram\n"
    print "-------------------------\n"

    for i in range(0,len(wordlist)-1) :
        print " %s : %d (%f %%)" % ( wordlist[i], countlist[i], percentlist[i] )

    print "\n"
    print "-------------------------\n"
    print "2-word Sequence Histogram\n"
    print "-------------------------\n"
    
    for i in range(0, len(bicount)-1) :
        print "%s : %d (%f %%)" % (biwords[i], bicount[i], bipercent[i])

    print "\n"
    print "-------------------------\n"
    print "A total of %d files contained the word spike.\n" % counter
    print "A total of %d words occurred in %d files: the average number of words per file is: %f" % (wordsum, counter, avg)
    print "A total of %d bigrams occurred in %d files: the average number of bigrams per file is %f\n" % (bigramsum, counter, biavg)

    print "Time elapsed: %f" % (toc-tic)
