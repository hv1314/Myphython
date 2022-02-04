#to find the nth postion of the fibonacci number ::
#Eg: if the number is 5  and the postion is 6 means

#in the fibonaci series 




def fibo(k,n):

        a=0
        b=1
        i=2
        while i!=0:
            c=a+b
            a=b
            b=c

        if b%k==0:

            return n *i
            
        i+=1

        return


print(fibo(4,5))
