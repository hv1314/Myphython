#this program is for rotation the last two numbers with first two numbers the array numbers..

#First program without any predefined value and algorithms..

#input as d and n
#using temp[] method
def rotation(arr, n, d):
    temp = []
    i= 0
    while (i<d):
        temp.append(arr[i])
        i = i +1
    i = 0
    while(d<n):
        arr[i]=arr[d]
        i = i+1
        d = d+1
        #have to call the array what is going to be printed arr[:]
    arr[:] = arr[: i]+temp
        #because of looping we have to retrun the value
    return arr
#driver function's
arr = [1,2,3,4,5,6,7]
print("After the rotation : ", end= ' ' )
#printing the function statements..
print(rotation(arr, len(arr), 2)) #declaring 2 because as per the given array the value of d is 2::


