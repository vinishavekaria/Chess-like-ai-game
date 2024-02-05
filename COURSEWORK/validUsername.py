validUsername= input("Enter a username: ")#asks user to input a valid username 

digit = False
lower = False
upper = False
symbol = False
length = False

for character in validUsername:
    if character in "qwertyuiopasdfghjklzxcvbnm":
        lower = True
    elif character in "QWERTYUIOPASDFGHJKLZXCVBNM":
        upper = True
    elif character in "0123456789":
        digit = True
    elif character in "!£$%^&*()-_;:'@#":
        symbol = True

if lower == True:
    print("username has a lowercase letter")
else:
    print("Must contain a lowercase letter")
if upper == True:
    print("username has an uppercase letter")
else:
    print("Must contain a uppercase letter")
if digit == True:
    print("username has a number")
else:
    print("Must contain a digit")
if symbol == True:
    print("username has a symbol")

if len(validUsername)<=15 and len(validUsername)>=5: #checks length of username
    print("valid username length")
else:
    print("must be between 5 and 15 characters")

if digit and lower and upper == True:#checks if username contains all requirements
    print("valid username")
else:
    print("invalid username")
