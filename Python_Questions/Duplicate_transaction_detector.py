# Problem Statement
# A banking system receives transaction IDs.
#  An ID is suspicious if it appears more than once. 
# Find the number of suspicious IDs and the total number of transactions belonging to suspicious IDs.
# Constraints
# 1 <= n <= 100; transaction IDs are integers.
# Input Format
# Line 1: n 
# Line 2: transaction IDs.
# Output Format
# Line 1: Suspicious IDs: <count> 
# Line 2: Suspicious Transactions: <count>

n=int(input())
ids=list(map(int,input().split()))
counts={}
suspicious=0
total=0
for i in ids:
    counts[i]=counts.get(i,0)+1
for key,value in counts.items():
    if value>1:
        suspicious+=1
        total+=value
print("Suspicious IDs:",suspicious)
print("Suspicious Transactions:",total)