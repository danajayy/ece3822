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


    def editline (self, line) :
        line = line.replace(","," ") # remove the comma
        line = line.strip() # remove any whitespace from line
    # end of editline function
    
    def read_data(self, fp) :
        temp = [] # temporarily stores data in file, fp

        with open(fp) as dates :
            for line in dates :
                dateline = editline(line)
                temp.append(dateline) 
        self.data = [i.split() for i in temp]
    # end of read_data function
    
    def check_prime (self, num) :
        if (num % 2 ) == 0 :
            result = "not a prime number."
        else :
            result = "a prime number."
        self.prime = result
        # end of if/else statement
    # end of function
    
    def convert (self, data, months) :
        if data[0] in months :
            days = months[[data[0]]
            if int(data[1]) <= len(months[data[0]]+1) :
                num = days[int(data[1])-1]
                check_prime(num)
                mdy = [' '.join(data[0:2]+',', data[2]]
                mdy = ' '.join(result)
                self.output = '%s corresponds to integer %d and is %s' % (mdy, num, self.prime)
            else :
                print "Invalid Input : %d is out of range of month %s" % ( int(dates[1]), data[0] )
            # end of if/else statement
        else :
            print "Invalid Input : No month called %s" % data[0]
        # end of if statement
    # end of convert function function
# end of class
                
        
