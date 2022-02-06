
#squaring of i and add to the sum

'''''
def sumsquare(n):
    sm =0
    for i in range (1, n+1):
        sm = sm+(i*i)       #loop form 1 to n for each "i" .. 1<=i and i<=n to find i^2
    return sm
print(sumsquare(4))'''

#this is using the formula form sum of n natural number
#       n*(n+1)*(2*n+1)//6

'''
def sumsquare(n):
    return (n*(n+1)*(2*n+1))//6
#or n =6
#print(sumsquare(n))
print(sumsquare(9))'''

#This formula is to display the sum of n even numbers

#       2*n(n+1)*(2*n+1)//3
'''
def sumsquare(n):
    return (2*n *(n+1)*(2*n+1))//3

print(sumsquare(9))
'''

#this one is for finding the odd number::

#      n*(2*n+1)*(2*n-1)//3

def sumsquare(n):
    return (n*(2*n+1)*(2*n-1))//3

print(sumsquare(8))