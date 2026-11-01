password = input("Enter the password: ")
if("@"in password):
    if(password[-2:].isdigit()):
        print("Strong Password")
    else:
        print("Weak Password")
else:
    print("Weak Password") 