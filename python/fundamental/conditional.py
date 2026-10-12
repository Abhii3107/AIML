# if ,#else

age  = 20

if age >= 18:
   print("eligible for vote")  # why ther eis gap in starting - inductetion , mtlb an ye if ke condition maia aaege
   print("both statememnt will printed if condition will justify")
else:
    print("you are not eligible for voting")  
    
#elif -> else if

color = input("enter a color")
if color == "red":
    print("stop")
    
elif color =="yellow":  #elif is always writen with if , -> agar if conditioon false hui , then this will execute and we can write multiple elif and check multiple elif
    print("go slow")
    
elif color =="green":
    print("GO")

else:
    print("wrong color is written")
    
    
    
    
   


''' 

Question
<13 = child 
 13-18 = teenage 
 18+  = adult

'''

# age = int(input("give age: "))

# if (age <13):
#     print("child")
# elif (age >= 13 and age <18 ):
#     print("teenager")
# else:
#     print("adult")

# ------------------------
# odd or even

num = int(input ("give us number :"))
if (num % 2 == 0):
    print("it is even number")
else:
    print("it is odd one")
