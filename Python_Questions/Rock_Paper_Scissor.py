import random
r=int(input("Enter How many round "))
player=0
computer=0
totp=0
totc=0
while r>0:
    plyr_choice=input("Your Choice ")
    comp_choice=random.choice(["rock","paper","scissor"])
    print("You - ",plyr_choice," Computer - ",comp_choice)
    plyr_choice=plyr_choice.lower()
    if(plyr_choice!="rock" and plyr_choice!="paper" and plyr_choice!="scissor"):
        print("Invalid Input")
        continue
    if(plyr_choice=="rock"):
        if(comp_choice=="paper"):
            computer+=1
        elif(comp_choice=="scissor"):
            player+=1
    elif(plyr_choice=="paper"):
        if(comp_choice=="scissor"):
            computer+=1
        elif(comp_choice=="rock"):
            player+=1
    elif(plyr_choice=="scissor"):
        if(comp_choice=="rock"):
            computer+=1
        elif(comp_choice=="paper"):
            player+=1
    r-=1
    totp+=player
    totc+=computer
    print(f"You {player} Computer {computer}")
    player=0
    computer=0    
print("Final Score ")
print(f"You: {totp} | Computer: {totc}")
if totp>totc :
    print("You win the game ")
elif totp<totc :
    print("Computer win the game ")
else:
    print("It's a Draw ")
 