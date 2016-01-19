#!/usr/bin/env python

# rework for exam 3 problem 1

from foo_00 import * # import all classes and their methods
import sys # need this to parse command line

def main(argv) :

    cars = Vehicle() # instantiating
    cars.read_file(sys.argv[1]) # read file
    cars.change_vals(cars.data) # assign data to variables

# end of main function

if __name__ == "__main__" :
    main(sys.argv[0:])
# end of file
        
