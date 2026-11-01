j=5
while(j>0):
    password = int(input('Enter Password '))
    if(password==12345):
        print('Login Sucessful')
        break
    else:
        j-=1
        print(j,' Attempts Left')
        if(j==0):
            print('Account is now Locked\nPlease Contact the admin')


