
import sys

def sys_args_test():

    if sys.argv >= 2:       ###  < ---- Right here I'm trying to say, if the user
                           ### supplies 2 arguments (0 , and 1), then execute the 
                           ### following code to assign everything after the path 
                           ### name as the 'user_number')

        users_number = sys.argv[1:]
        print ('this is the sys.argv', sys.argv)
        print( 'argument supplied, argument =', users_number)
        print ("User supplied {} arguments at run time").format(len(sys.argv))

    else:                  ### <----- Right here I'm trying to say that if no
                           ## arguements are supplied, ask the question, and then 
                           ## store that number as 'user_number'

                           ##This isn't working though, it says that even though the 
                           ##user supplied 1 argument, it is still operating the 
                           ## previous code.
    
        users_number = raw_input('Enter the number you want to play fizz buzz up to: ')
        print ('no arg supplied so we asked the question.', users_number)




### Then, with whatever we've decided is the 'user_number', use it in the following

    for user_n in users_number:
        print user_n ## <--- this is to get it out of the list.
      
        
    for n in range(int(user_n)):
        if n % 3 == 0:
            print ('fizz')

        elif n % 5 == 0:
            print ('buzz')

        else:
            print (n)
            

sys_args_test()










# But now after looking at that other fizz_Buzz program, I'm sort of thinking that the 
#"default" users_number coule be set to raw_input question, directly defined in the 
#argument position, and then after the 'main' signature section, there'd be the option 
# for the user to define it with an arguement, like the other program:

# if __name__ == '__main__':
#     limit = int(sys.argv[1])

# fizz_buzz(limit)






