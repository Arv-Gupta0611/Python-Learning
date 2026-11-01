username=input('Enter username ')
if(username =='arv'):
    password=int(input('Enter Password '))
    if(password==1234):
        print('Login Successful')
    else:
        print('Wrong Password')
else:
    print('User not found')