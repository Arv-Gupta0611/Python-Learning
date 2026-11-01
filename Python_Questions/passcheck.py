#4 alphabet 3 num. 2 special symbols
passw=input("enter")
alph=0
dig=0
spc=0
for c in passw:
    if(c.isalpha()):
        alph+=1
    elif(c.isalnum()):
        dig+=1
    else:
        spc+=1
if(alph>=4 and dig>=3 and spc>=2):
    print("Strong Password")
else:
    print("Not a strong password")