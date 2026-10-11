
ans = 10 +20.0  # type conversion - implicit
print (type(ans)) 
# <class 'float'>

ans= int(10 + 20.0) #type casting - explicitly
print(type(ans))
# <class 'int'>

# -------------------------------------------------------------


"""
Python: Type Conversion and Type Casting

1. TYPE CONVERSION
- Type conversion means changing one data type into another.
- Python automatically converts data types in some operations.
- It is called Implicit Type Conversion.

Example:
"""

a = 10
b = 2.5

result = a + b

print(result)       # 12.5
print(type(result)) # <class 'float'>


"""
2. TYPE CASTING
- Type casting means manually converting one data type into another.
- It is called Explicit Type Conversion.
- Python provides built-in functions for type casting.

Example:
"""

a = "10"
b = int(a)

print(b)        # 10
print(type(b))  # <class 'int'>


"""
3. COMMON TYPE CASTING FUNCTIONS

int()   - Converts to integer
float() - Converts to float
str()   - Converts to string
bool()  - Converts to boolean
list()  - Converts to list
tuple() - Converts to tuple
set()   - Converts to set
"""


"""
4. IMPORTANT EXAMPLES
"""

# Integer to Float
print(float(10))        # 10.0

# Float to Integer
print(int(5.8))         # 5 (decimal part removed)

# String to Integer
print(int("25"))        # 25

# String to Float
print(float("3.14"))    # 3.14

# Integer to String
print(str(100))         # 100

# Boolean Conversion
print(bool(0))          # False
print(bool(1))          # True
print(bool(""))         # False
print(bool("hello"))    # True

# List, Tuple, and Set
print(list("abc"))      # ['a', 'b', 'c']
print(tuple([1, 2]))    # (1, 2)
print(set([1, 1, 2]))   # {1, 2}


"""
5. IMPORTANT POINTS TO REMEMBER

- Implicit conversion = Automatic conversion.
- Explicit conversion = Manual conversion.
- int(5.8) returns 5, not 6.
- int("hello") raises ValueError.
- Zero and empty strings are falsy values.
- Non-zero numbers and non-empty strings are truthy values.

QUICK REVISION

int()   = Integer
float() = Decimal number
str()   = String
bool()  = True or False
"""
