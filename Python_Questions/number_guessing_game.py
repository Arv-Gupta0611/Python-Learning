import random
flag=True
while flag==True :
    num=random.randint(1,100)
    for i in range(1,8):
        guess=int(input("Enter Your Guess "))
        if(1<=guess<=100):
            if(guess==num):
                print("You guess right in ",i," attempts.")
                print("You wanted to play again yes/no ")
                reattempt=input()
                break
            else:
                if(guess>num):
                    print("Guess lower number ")
                elif(guess<num):
                    print("Guess higher number")
                continue
        else:
            print("Please enter the valid number for range ")
    if reattempt=="yes":
        flag=True
    else:
        flag=False
print("Goodbye")