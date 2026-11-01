balance=100000
pin=int(input('Enter your pin '))
if(pin==1234):
    amount=int(input('Enter withdrawl amount'))
    if(amount>0):
        if(amount<=balance):
            print('Sucessful Withdrawl')
            print('Withdrawl amount: ',amount)
            print('Remaining Balance: ',(balance-amount))
        else:
            print('Insufficient Balance ')
    else:
        print('Invalid Amount ')
else:
    print('Wrong Pin')
