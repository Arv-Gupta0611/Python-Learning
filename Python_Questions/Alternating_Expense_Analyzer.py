# Problem Statement
# A company records daily expenses. Expenses at odd positions are added and expenses at even positions are subtracted,
#  using 1-based positions. Calculate the final balance and classify it as Positive, Negative or Zero.
# Constraints
# 1 <= n <= 100; 1 <= expense <= 10000
# Input Format
# Line 1: n 
# Line 2: n expenses.
# Output Format
# Line 1: Balance: <value> 
# Line 2: Status: <Positive/Negative/Zero>

n=int(input())
exp=list(map(int,input().split()))
balance=0
for i in range(0,n):
    a=i+1
    if(a%2!=0):
        balance+=exp[i]
    else:
        balance-=exp[i]
print("Balance:",balance)
if balance > 0:
    print("Positive")
elif balance < 0:
    print("Negative")
else:
    print("Zero")