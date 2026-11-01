import random
jackpot=random.randint(1,100)
guess = int(input('guess a number between 1 and 100:'))
counter=1
while(guess!=jackpot):
    if(guess<jackpot):
        print('Galat guess higher number try again')
    elif(guess>jackpot):
        print('Galat guess lower number try again')    
    guess = int(input('guess number again :'))
    counter+=1
else:   
    print(f'Congratulations you guessed the right number in {counter} attempts')  