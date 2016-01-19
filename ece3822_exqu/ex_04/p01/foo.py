#!/usr/bin/env python

import sys # need to parse command line arguments

# This function takes in text and changes any special characters
# (non-alphabet/numerals) to spaces
#
def charch (text) :
    chars = ".,?/:;~`!@#$%^&*()-_=+" # list of characters that will change
    for c in chars :
        text = text.replace(c, "")
    return text
# end of function 

def main(argv) :

    values = [] # this list will contain corresponding numerical values
    
    ones = {
        'one' : 1,
        'two' : 2,
        'three' : 3,
        'four' : 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine' : 9,
        'zero' : 0
        }

    teens = {
        'eleven' : 11,
        'twelve' : 12,
        'thirteen' : 13,
        'fourteen' : 14,
        'fifteen' : 15,
        'sixteen' : 16,
        'seventeen' : 17,
        'eighteen' : 18,
        'nineteen' : 19
        }
    
    tens = {
        'ten' : 10,
        'twenty' : 20,
        'thirty' : 30,
        'forty' : 40,
        'fifty' : 50,
        'sixty' : 60,
        'seventy' : 70,
        'eighty' : 80,
        'ninety' : 90
        }

    # open foo.txt file
    #
    with open(sys.argv[1], "r") as foo :

        # loop through each line in foo.txt
        #
        for line in foo :
            # go through each word in each line
            #
            for word in line.split() :
                word.lower() # change word to lower case

                # check if word is a ones digit
                #
                if word in ones.keys() :
                    values.append(ones[word]) # append the numerical value in list
                    
                # check if word is a tens digit
                #
                elif word in tens.keys() :
                    values.append(tens[word]) # append numerical value in list

                # check if word is a teens value
                # this gets special case because these are
                # spelled differently than the other numbers
                #
                elif word in teens.keys() :
                    values.append(teens[word]) # append numerical value in list
                    
                # end of if/elif statement

                # check if word contains a hyphen because any number
                # larger than twenty are spelled out with a hyphen (or at least should be)
                #
                if "-" in word :

                    # send word with hyphen to get all special characters removed
                    # and store result to variable num
                    #
                    num = charch(word)

                    # loop through all keys in tens dict
                    #
                    for a in tens.keys() :
                        # loop through all keys in ones dict
                        #
                        for b in ones.keys() :
                            
                            # create the number as string to check against incoming word
                            #
                            checknum = str(a + b)

                            # if the strings match, add up the corresponding tens and ones
                            # dictionary value as variable v and store that value into list
                            #
                            if num == checknum :
                                v = tens[a] + ones[b] # create corresponding numerical value
                                values.append(v) # value into list
                            # end of if statement for num == checknum
                        # end of for loop for ones.keys()
                    # end of for loop for tens.keys()
                # end of if statement for if "-" in word
            # end of for loop for word in line
        # end of for loop for line in foo
    # end of while file is open as foo
                    

    # square each number stored in list
    #
    values = [i**2 for i in values]

    # sum up the numbers in values
    #
    total = sum(values)

    # print result
    #
    print total
    
#end of main function

if __name__ == "__main__" :
    main(sys.argv[0:])
# end of file
