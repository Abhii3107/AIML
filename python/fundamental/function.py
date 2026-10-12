'''
function - A block of code that perform  some specfic task.

def functionName():
    function body...1
    function body...n

'''


def hello():          # define a function
    print("Hello ")
    print("from Python :) ")
    
hello()  # cal a function , or invoke a function

#---------------------------------

def sum( a, b): #parameter
    s = a + b
    return s

ans = sum(4,5) # argument - value that we pass to function

print(ans) 
print (sum(6,4))

#---------------------------------

#default value

def add(a , b =1):  # by default b=1 , if value will not provided
    return a + b

print(add(10))
# 11

print (add(10, 2))
#12

#Note - always assign value from left to right  --------->

'''
def add(a = 1, b):
     return a+b

add(10)   -> wrong because 10 is assign to a , but b is null so it will be error
'''



