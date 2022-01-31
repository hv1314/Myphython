#in all languages armstrong number has the same method as i know:



num = int(input("Enter a number"))
sum = 0
temp=num
while temp>0 :

        r = temp%10
        sum += r*r*r
        temp //= 10

if num == sum:
        print(num,"Is a amstrong number")
else:
        print(num,"Is not a amtrong number")



