email=input('Enter your email:')
password=input('Enter your password:')
if(email=='arv.v.gupta@gmail.com' and password =='123456789'):
    print('Welcome Boss')
elif(email=='arv.v.gupta@gmail.com' and password !='123456789'):
    print('Boss you are entering wrong password please try again')
    password=input('Enter your password again:')
    if(password=='123456789'):
        print('Welcome Boss')
    else:
        print('Boss eat almonds and then come back to try again later')
elif(email!='arv.v.gupta@gmail.com' and password =='123456789'):    
    print('You are not authorized to access boss account \nPassword has been compromised \nLocking account to master password\nCalling police immediately!')
    
else:
    print('You are not authorized to access boss account Calling police immediately!')    