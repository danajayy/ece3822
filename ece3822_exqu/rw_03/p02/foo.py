#!/usr/bin/env python 

# rework for exam 3 problem 2

import sys # import to parse command line arguments
import os # to go through the directory tree
import csv # to create, read, and write .csv files
import fcntl # to lock files

# Start of main()
#
def main(argv):

    home = os.path.expanduser('~') # find home directory
    fname = "foosum.csv" # name of file that contains previous sum value

    # Generate file path from file name and home directory
    #
    fpath = "%s/%s" % (home,fname) 

    # Check if the file exists using if/else statement
    #
    if os.path.isfile(fpath): 

        foosum = open(fpath, 'rb') # if file exists, open it
        
        # lock foosum so only one user can access it at a time,
        # additionally it will not block on lock acquisition 
        #
        fcntl.flock(foosum, fcntl.LOCK_EX | fcntl.LOCK_NB)

        foofile = csv.reader(foosum) # read foosum file 

        # 1st row contains previous sum, read file and assign
        # the first line to prevsum
        #
        for row in foofile:
            prevsum = float(row[0])
        # end of for loop

        # Unlock the file before closing it 
        #
        fcntl.flock(foosum, fcntl.LOCK_UN)

        foosum.close() # close foosum.csv file

    else:

        # if file doesn't exist, means 1st time program running
        # create foosum file to store sum
        #
        foosum = open(fpath, 'wb')
        
        # lock foosum so only one user can access it at a time, 
        # it will not block on lock acquisition 
        #
        fcntl.flock(foosum, fcntl.LOCK_EX | fcntl.LOCK_NB)

        foowriter = csv.writer(foosum) # foowriter is object for opened file foosum
        foowriter.writerow([0]) # initialize file by writing 0 in 1st line
        prevsum = 0 # initialize prevsum to 0
        fcntl.flock(foosum, fcntl.LOCK_UN) # unlock file
        foosum.close() # close foosum.csv file
    
    # end if/else statement


    args = sys.argv # store command line arguments in args
    args.pop(0) # remove 0th index from list because that's program name

    # Execute the code within the 'try' statement
    #
    try:
        
        # Type-cast the input arguments as floats
        #
        args = [float(i) for i in args]
        
        argsum = sum(args) # sum up the arg values

        # display sum of args
        #
        print("The sum of the input arguments is %.3f") % argsum
    
    # If the user did not enter valid input arguments then output a slightly snarky 
    # error message
    #
    except:
        print("Invalid input(s). Please enter numerical values.")

    # end of try/except statement

    totalsum = argsum + prevsum # add new sum to previous sum

    print("Your sum is %.3f") % totalsum # display new sum value

    # open file to store new prev. sum, open file object is foosum
    # open file for write access
    #
    foosum = open(fpath, 'wb')
            
    # lock foosum so that only one user can access it at a time, 
    # it will not block on lock acquisition 
    #
    fcntl.flock(foosum, fcntl.LOCK_EX | fcntl.LOCK_NB)

    foowriter = csv.writer(foosum) # foowriter is object for opened file foosum
    foowriter.writerow([totalsum]) # store new sum on first line of foowriter (overwrite old sum)
    fcntl.flock(foosum, fcntl.LOCK_UN) # unlock file
    foosum.close() # close foosum.csv file
    
# end of main function

# Begin gracefully, THIS STATEMENT MUST BE LAST
#
if __name__ == "__main__":
    main(sys.argv[0:])

#
# EOF
