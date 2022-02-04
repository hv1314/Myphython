# the number which is divisible by itslef



n = 8

flag = False

if n>1:

        for i in range(2, n):

            if n%1 == 0:
                
                flag= True

                break                                       #if the flag is true means break the loop


if flag:
        print("Not a prime number", n)
else:
        print("Prime number", n)

  



            






#1. Flag used to check the default stament and we cal pull that upto our condition