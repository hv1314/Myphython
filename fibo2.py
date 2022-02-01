    
a = 0
b = 1
n = int(input("Enter a number"))
print (a)
   
for i in range(1, n):
            c = a + b
            a = b
            b = c
            
            print (b)


