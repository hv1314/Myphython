#first define the function for imaginary i and j and temp




def rotation(arr, d, n):
    for i in range (gcd(d,n)):
   
#creating the temp value for storing the i value
        temp = arr[i]
    #now define the numbers inside the arr i ..,,

        j = i 

    while 1:
        k = j+d
# the k  function has been defined for the sum : and checking
        if k >= n:
             k = k-n
        if k == i:
            break
#and now declare the array transform

        arr[j]= arr[k]
        #and also the numbers inside the array
        j = k
        #now place the temp in coorect position
        arr[j] = temp
    
#now define the functions to create the array

def printarr(arr, size):
    for i in range(size):
        print("%d" % arr[i], end=" ")

#now define the main """""GDC""""" function that we declared in the top:

def gcd(a,b):
    if b == 0:
        return a
    else:
        return  gcd(b, a%b)

#now declare the driver fucntions
#1. The arry 
arr = [1,2,3,4,5,6,7,8,9,10,11,12]
#2. Call the main function
rotation(arr, 3, 12)
#3.Print the array function
printarr(arr, 12)
print("\n""Juggling algorithm has executed successfully")