#!/usr/bin/env python

# defining class PrimeDates
#
class PrimeDates :

    # constructor definition
    #
    def __init__(self) :
        self.data = []
        self.output = ""
    # end of constructor

    def read_data(self, fp) :
        temp = [] # temporarily stores data in file, fp

        # open fp and refer to is as dates
        #
        with open(fp) as dates :

            # loop through each line in dates
            #
            for line in dates :
                line = line.replace(","," ") # remove the comma  
                line = line.strip() # remove any whitespace from line

                # each date stored in own index in temp list
                #
                temp.append(line) 

        # each date is broken up in sublist, so data is a list
        # of sublist of each component of the dates
        #
        self.data = [i.split() for i in temp]

    # this functions takes in the read data and converts
    # the day to its corresponding day of the year and checks if
    # the number is prime; will output to stdout
    #
    def convert (self, data, months) :

        # first loop gets the dates saved in sublists of list data
        # each sublist is length of 3, values saved in sublist:
        #    0th index : month
        #    1st index : day
        #    2nd index : year
        #
        for dates in data :
            if dates[0] in months :
                days = months[[dates[0]]
                if int(dates[1]) <= len(months[dates[0]]+1) :
                    num = days[int(dates[1])-1]
                        if (num % 2 ) == 0 :
                              prime = "not a prime number."
                        else :
                              prime = "a prime number."
                    result = [' '.join(dates[0:2]+',', dates[2]]
                    result = ' '.join(result)
                              self.output = '%s corresponds to integer %d and is %s' % (result, num, prime)
                else :
                    print "Invalid Input : %d is out of range of month %s" % ( int(dates[1]), dates[0] )
                else :
                    print "Invalid Input : No month called %s" % dates[0]
                # end of if statement
                    
        
        


    # end of numop function
                
        
