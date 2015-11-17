#!/usr/bin/env python

# defining class PrimeDates
#
class PrimeDates :

    # constructor definition
    #
    def __init__(self) :
        self.data = []
        self.prime = ""
        self.output = ""
    # end of constructor

    # this function edits line by removing whitespace and comma in date
    #
    def editline (self, line) :
        line = line.replace(","," ") # remove the comma
        line = line.strip() # remove any whitespace from line
    # end of editline function
    
    # this function takes in the input file, reads it, organizes each line
    # (which are the dates) and puts the components of the date into a sublist,
    # and these sublists are loaded into temp list, which is sent to self.data
    #
    def read_data(self, fp) :
        temp = [] # temporarily stores data in file, fp

        # open fp and refer to is as dates
        #
        with open(fp) as dates :

            # loop through each line in dates
            #
            for line in dates :
                dateline = editline(line)
                # each date stored in own index in temp list
                #
                temp.append(dateline) 

        # each date is broken up in sublist, so data is a list
        # of sublist of each component of the dates
        #
        self.data = [i.split() for i in temp]
    # end of read_data function
    

    # this function checks if day of month
    # is a prime number and returns that it is
    #
    def check_prime (self, num) :
        if (num % 2 ) == 0 :
            result = "not a prime number."
        else :
            result = "a prime number."
        self.prime = result
        # end of if/else statement
    # end of function
    
    # this functions takes in the read data and converts
    # the day to its corresponding day of the year and checks if
    # the number is prime; will output to stdout
    # data : list
    # months : dictionary
    #
    def convert (self, data, months) :

        # check if month (stored in dates[0]) appears in months dictionary
        #
        if dates[0] in months :
            
            # days of the month (accessed by key value in) stored in days
            #
            days = months[[dates[0]]

            # if day of month falls within length of month, the day is valid
            # if not, output error message
            #
            if int(dates[1]) <= len(months[dates[0]]+1) :

                # access the list of days stored in months dictionary
                # num is the day of month (since lists start indexing at 0, need
                # to access the index [day-1]
                #
                num = days[int(dates[1])-1]
                check_prime(num)

                # construct the date again for output
                #
                mdy = [' '.join(dates[0:2]+',', dates[2]]
                mdy = ' '.join(result)
                
                # if month and day is valid, send result to self.output
                #
                self.output = '%s corresponds to integer %d and is %s' % (mdy, num, self.prime)
            else :
                print "Invalid Input : %d is out of range of month %s" % ( int(dates[1]), dates[0] )
            # end of if/else statement
        else :
            print "Invalid Input : No month called %s" % dates[0]
        # end of if statement
    # end of convert function function
# end of class
                
        
