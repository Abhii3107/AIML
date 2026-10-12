''''
* Nesting -> condition under conditional 

if ():
    if():

'''

# Q -> username - Abhay , pass - 1234 , then login otherwise not

username  = input( "please enter your username : ")
password =int(input("enter password: "))

if (username == "Abhay" and password == 123):   
    print("Successful login")
else:
    if (username != "Abhay"):         # if username write username wrong and password correct
       print("wrong username")
    else:
        print("wrong password")


