''''
def cubesum(n):
    
    z = (n*(n+1/2))
    return (int)(z*z)

print(cubesum(9))'''

def cube(n):
    sum =0
    for i in range(1, n+1):
        sum = i*i*i
    return sum
print(cube(8))