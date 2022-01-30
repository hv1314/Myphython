
#single line factorial RECURSIVE

def fact(n):
  return 1 if (n==0 or n==1) else n * fact(n - 1)

num = int(input("Enter a number"))

print("The factorial of number is"+str(fact(num)) )

        
