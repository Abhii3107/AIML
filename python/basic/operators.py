'''
a+b =10

operand = a, b 
operator = + 
'''

# 1 arithmetic

a = 10
b = 5

print (a+b)
print (a-b)
print(a*b)
print(a/b)
print(a%b) #modulo -> always give reminder
print(a**b) # b power a


# 2 Relational -> True or false

A=10
B=10

print(A<B)  # op -> False
print(A>B)
print(A<=B)
print(A>=B)

print(A==B)
print(A!=B) # a kya b ke equal nhi hai  ->  != Means Not equal to   


# 3.Assignment Operators
a = 10
a += 5
print(a)  # 15

a -= 3
print(a)  # 12

a *= 2
print(a)  # 24

a /= 4
print(a)  # 6.0


# L4.ogical Operators
x = 10
y = 5

print(x > 5 and y < 10)  # True
print(x > 15 or y < 10)  # True
print(not x > 5)         # False



'''
Dry Run
You entered:
a = 10
 b = 2

Step by step:
1. a + b → 10 + 2 = 12
2. (a + b) / 2 → 12 / 2 = 6.0
3. print(average) displays 6.0

Why 6.0 instead of 6?
In Python, the / operator always returns a float (decimal number), even when the result is a whole number.

print(12 / 2)   # 6.0
print(12 // 2)  # 6

Remember: Use / for normal division and // for floor division.
'''