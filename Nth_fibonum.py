#to find the nth postion of the fibonacci number ::
#Eg: if the number is 5  and the postion is 6 means

#in the fibonaci series 




# Python Program to find position of n\'th multiple
# of a number k in Fibonacci Series
def findPosition(k, n):
    f1 = 0
    f2 = 1
    i =2;
    while i!=0:
        f3 = f1 + f2;
        f1 = f2;
        f2 = f3;
 
        if f2%k == 0:
            return n*i
 
        i+=1
         
    return
 
 
# Multiple no.
n = 5;
# Number of whose multiple we are finding
k = 4;
 
print("Position of n\'th multiple of k in"
                "Fibonacci Series is", findPosition(k,n));





#THIS PROGRAM ISNOT RUNNING IF WE CHANGE THE VARIABLES INSIDE OF THIS BUT I HAD UNDERSTOOD THE ALGORITH OF nth multiple position of number in the fibonacii series::