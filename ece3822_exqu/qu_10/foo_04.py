#!/usr/bin/env python

class PrimeDates :

    # constructor definition
    def __init__(self) :
        self.temp = [] # temporary data holder
        self.d = 0 # day
        self.m = "" # month
        self.y = 0 # year
        self.data = [] # holds list of sublist of dates from file
        self.prime = "" # hold prime result
        self.integer = 0 # corresponding integer
        self.valid = False # checks if date is valid
        self.output = "" # outputs validity
        self.months = { 'January' : range(1,31), # 31 days
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
    # end of constructor

    
    # edits line by removing comma and whitespace
    #
    def editline(self, line) :
        line = line.replace(",", " ") # replace the comma to space
        line = line.strip() # remove all spaces in line
        self.temp.append(line) # load line into temp list holder
        self.data = [i.split() for i in self.temp] # store components of date as indices in list
    # end of editline function

    
    # reads file fp line by line and sends to editline
    #
    def read_file(self, fp) :
        with open(fp) as datafile : # open file fp and call it datafile
            for line in datafile : # for each line in datafile
                self.editline(line) # send to editline to get modified
            # end of for loop
        # end of opening file
    # end of read_file function

    
    # check if corresponding integet is prime
    #
    def check_prime (self, day) :
        if (day % 2)  == 0  : # if modulus is 2, means it is even number (not prime)
            self.prime = "is not a prime number."
        else :
            self.prime = "is a prime number." # if not, it is a prime number
        # end of if/else statement
    # end of check_prime function  

    
    # checks if the month and day input are valid dates
    #
    def validate(self, month, day, year, monthdict) :
        if month in monthdict : # if month is in month dictionary (valid)
            dates = monthdict[month] # get the range of days in month
            length = len(monthdict[month]) # get length of month

            # if the day is outside range, it is not valid day
            # if valid, get the associated integer for that day
            #
            if day <= length+1 : 
                self.integer = dates[day-1] # get corresponding integer stored in list in months dictionary
                self.prime = self.check_prime(self.integer) # check if integer is prime
                self.valid = True # if everything is valid, make true
            else :
                self.valid = False # false if day invalid
        else :
            self.valid = False # false if month is not valid
    # end of validate function

    
    # data : list of sublists from read_data functions
    # months : dictionary of months with their day range
    #
    def convert(self, data) :
        # for all sublists in data (sublists hold month, day, and year for each data)
        # validate that the date is correct and if so, output the results
        #
        for sublist in data :
            self.m = sublist[0] # month
            self.d = int(sublist[1]) # day
            self.y = int(sublist[2]) # year
            self.validate(self.m, self.d, self.y, self.months)
            if self.valid == True :
                self.output = "%s %s, %s corresponds to the integer %d and %s" % (self.m, self.d, self.y, self.integer, self.prime)
                print self.output
            else :
                self.output = "%s %s, %s is an invalid date." % (self.m, self.d, self.y)
                print self.output
            # end of if/else statement
        # end of for loop
    # end of convert function

# end of class PrimeDates
    
