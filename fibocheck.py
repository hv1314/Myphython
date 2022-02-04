#to check whether the given number is fibonacci number or not::

#to check the number of fibo we have to use the formulae::
        #  (5*n^2+4) or (5*n^2-4)

#we have check the given number is perfect square or not!!
import math
from tkinter.tix import Tree
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x




def isFibonacci(n):
 
    # n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perferct square
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

a = int(input("enter the number = "))

for i in range(0, a):

    if (isFibonacci(a)==True):
        print(i,"Its is a fibo" )
    else:
        print(i,"not a fibo")


    


   





 

      