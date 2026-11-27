# Problem Statement
# A password satisfies four rules:
#  at least 8 characters,
#  at least one digit,
#  at least one uppercase letter,
#  and at least one lowercase letter.
#  Count satisfied rules and classify it as Strong (4), Medium (2 or 3), or Weak (0 or 1).
# Constraints
# Password contains no spaces; length <= 50.
# Input Format
# One line containing the password.
# Output Format
# Line 1: Rules Satisfied: <count> 
# Line 2: Strength: <classification>

password =input()
alph=0
dig=0
upp=0
low=0
strong=0
for ch in password:
    if ch.isalpha():
        alph+=1
    if ch.isdigit():
        dig+=1
    if ch.isupper():
        upp+=1
    if ch.islower():
        low+=1
if(len(password)>=8):
    strong+=1
if(dig>=1):
    strong+=1
if(upp>=1):
    strong+=1
if(low>=1):
    strong+=1

if(strong>=4):
    print("Rule Satisfied: ",strong)
    print("Strong")
elif(2<=strong<=3):
    print("Rule Satisfied: ",strong)
    print("Medium")
else:
    print("Rule Satisfied: ",strong)
    print("Weak")