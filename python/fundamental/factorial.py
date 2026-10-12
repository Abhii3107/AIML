# 5- 1*2*3*4*5 

def calc_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i

    return fact

n = int(input("enter n:"))
print(calc_factorial(n))