#!/usr/bin/env python

class PrimeDate :

    # constructor definition
    def __init__(self) :
        self.data = [] # holds list of sublist of dates from file
        self.prime = "" # hold prime result
        self.dateline = "" # holds date
        self.integer = 0 # corresponding integer
        self.valid = False # checks if date is valid
        self.output = "" # outputs validity
    # end of constructor

    def editline(self, line) :
        data = []
        line = line.strip()
        line = line.replace(","," ")
        data.append(line)
        self.data = [i.split() for i in data]
    # end of editline function

    def read_file(self, fp) :
        with open(fp) as datafile :
            for line in datafile :
                editline(line)
            # end of for loop
        # end of opening file
    # end of read_file function

    # dates_data = contain the month[0], day[1], and year[2] (list)
    # dates = all the days in a month (list)
    # day = the day in month (scalar int)
    #
    def validate(self, month, day, year, monthdict) :
        if month in monthdict :
            dates = monthdict[month]
            if day <= len(dates+1) :
                self.integer = dates[int(day)-1]
                self.valid = True
            else :
                self.valid = False # false if day is beyond month range
        else :
            self.valid = False # false if month is not valid
    # end of validate function

    def write_result(self, month, day, year) :
        result = [' '.join([month, day])+',',[year]]
        self.dateline = ' '.join(result)
    # end of write_result function

    def check_prime (day) :
        if (day % 2 ) == 0 :
            self.prime = "is not a prime number."
        else :
            self.prime = "is a prime number."
        # end of if/else statement
    # end of check_prime function
    
    # data : list of sublists from read_data functions
    # months : dictionary of months with their day range
    #
    def convert(self, data, months) :
        for sublist in data :
            m = sublist[0] # month
            d = sublist[1] # day
            y = sublist[2] # year
            validate(m, d, y, months)
            if self.valid == True :
                write_result(m, d, y)
                self.output = "%s corresponds to the integer %d and %s" % (self.dateline, self.integer, self.prime)
            else :
                self.output = "%s %s, %s is an invalid date." % (m, d, y)
            # end of if/else statement
        # end of for loop
    # end of convert function

# end of class PrimeDates
    
