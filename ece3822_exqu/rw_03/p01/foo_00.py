#!/usr/bin/env python

# rework for exam 3 problem 1

class Vehicle :

    # constructor method definition to initialize
    # the variables
    #
    def __init__(self) :
        self.manufacturer = ""
        self.model = ""
        self.width = -1
        self.length = -1
        self.data = [] # store entire data from file
        self.temp = [] # temp holds line of data from file
    # end of constructor

    # this method takes each line from file and removes
    # '=' and ',' characters, replaces them with spaces
    # and removes white space and stores each line from
    # file into a list, where each string on line is in
    # separate index; all data stored in self.data list
    #
    def editline(self, line) :
        line = line.replace(",", " ") # replace , with space
        line = line.replace("=", " ") # replace = with space
        line = line.strip() # remove all white space
        self.temp.append(line) # append each component of that line in a list
        self.data = [i.split() for i in self.temp]  # append that list into a larger list to hold entire data of file
        # each vehicle data in own index of large list
        # each vehicle in own sublist
    # end of editline method

    # reads in file fp and names it datafile
    # calls editline method to clean up entries
    # in order to properly display data
    #
    def read_file(self, fp) :
        with open(fp) as datafile : # open file and known as datafile
            for line in datafile: # loop through each line in file
                self.editline(line) # send each line of data to editline method
            # end of for loop
        # end of with statement
    # end of read_file method

    # takes in class' data list and assigns each index
    # to its corresponding variable and then calls the
    # debug method to print data to stdout
    #
    def change_vals(self, data) :

        # for each sublist in data, assign corresponding value
        # to its variable from sublist
        # each sublist contains 1 type of vehicle's data
        #
        for carinfo in data :
            self.manufacturer = carinfo[1]
            self.model = carinfo[2]
            self.width = carinfo[3]
            self.length = carinfo[4]
            self.debug()
        # end of for loop
    # end of change_vals method

    # prints out data from file to stdout
    #
    def debug(self) :
        print "Vehicle:"
        print ("\tManufacturer: %s") % self.manufacturer
        print ("\tModel : %s") % self.model
        print ("\tWidth : %s") % self.width
        print ("\tLength : %s") % self.length
    # end of debug method

# end of Vehicle Class

        
