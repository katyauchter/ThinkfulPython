
# Write two functions.

#     Write one function that determines if one
#      number is evenly divisible by another and 
#      returns true or false

#     Write another function that prints out the 
#     number/fizz/buzz/fizzbuzz as appropriate while 
#     iterating over an upper limit. This function should 
#     call the first one to test for each case 
#     (divisible by 5, 3, 15, etc.). 
#        <--- I don't really 
#       understand what this question is asking me to do.
#       for function 2


def is_even(n):
    if n % 2 == 0:  # Here I missed the point, that 2 numbers need to be involved, not just mod 2.
        return True

def fizz_buzz():

    for i in range(is_even(n)) # <--- This is probably wrong
        if n % 5 == 0:
            print ('fizz')
        elif n % 3 == 0:
            print ('buzz')
        else: 
            n % 15 == 0:
            print('fizzbuzz')

if __name__ == '__main__':


    # Provide a main routine. 
    # Use if __name__ == '__main__': to run this 
    # function from the command line. 
    # For the main routine, you should use sys.argv 
    # to get user supplied upper limit.

    # ---> I don't understand how to do this.


    # Provide default arguments. 
    # Your fizz buzz function should provide a default 
    # value for the limit parameter.


#Demo answer -- analyze and find questions:

import sys
 
    def _is_divisible(a, b):
""" Is a evenly divisible by b ? """
        return a % b == 0  # I would've never thought to 'return' this.  What other ways can this be done?
                            # The directions say the return should be True, or False,
                            # So I guess I took that too literally? 
                            # Write a function that only returns values that are even.

                            #I'd've done more of this
                            # def is_even(a,b):
                            #       if a / b == True:
                            #           return a
                            #       else:
                            #           return None

        # So this is taking even numbers, and only allowing
        # Even numbers to be used in the next function, correct?
        # I feel like this was not clearly worded in the prompt.
 
    def fizz_buzz(limit=100):           ## are there more examples 
                                        ## we can do where the argument is fixed ?
                                        ## This is difficult for me to understand.
                                        ## Why not just put it as (limit), and then define 
                                        ## what it is outside the funtion 'limit = 100'
""" Do fizz buzz up to limit number """
 
        for val in range(1, limit+1):  # when setting the 'range' it is indicated with a ','
                                       # not a ':' correct? - this means something else but I don't remember what.
           
            if _is_divisible(val, 15): #<--- wait I don't think I get this. But I don't get it in the prompt either.
                                       # is this saying, if the number produced by the first function is divisible by 15,
                                       # print fizzbuzz?   oh wait, I see,  the first function isn't being used to filter out
                                       # any numbers at all, it's only being used to decide if it a number is infact divisible
                                       # by the second amount, 3, 5, or 15.
                                       # This was not clear in the way the prompt was given for me!, but clear now.
                print "fizz-buzz"
 
            elif _is_divisible(val, 5):
                print "buzz"
 
            elif _is_divisible(val, 3):
                print "fizz"
 
            else:
                print val
 
if __name__ == '__main__':
    limit = int(sys.argv[1]) #<------------is this allowing the user to set the limit
                             # and then if they don't set the limit, then it just goes to default?
                             # - the first argument in sys.argv (or sys.argv[0] is the filename, and the second
                             # is the user supplied variable, correct?)

                            # I could use this for my other fizz buzz function no?
fizz_buzz(limit)




