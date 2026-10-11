#  a+b / 2

a = int (input ("value of a : "))
b = int(input ("value of b : "))

average = (a + b) / 2
print (average)


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

