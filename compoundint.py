#COMPOUND INTREST


p = int(input("Enter the principle"))
n = int(input("Enter the number of years"))
r = float(input("Enter the rate of intrest"))

ci=p*(pow((1+r/100),n))


print(float(ci))
