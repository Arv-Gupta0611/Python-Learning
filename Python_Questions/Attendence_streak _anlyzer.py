# Problem Statement
# An attendance record uses 1 for present and 0 for absent. 
# Find the longest continuous attendance streak and determine whether the student achieved at least 5 consecutive present days.
# Constraints
# 1 <= n <= 100; values are only 0 or 1.
# Input Format
# Line 1: n 
# Line 2: attendance values.
# Output Format
# Line 1: Longest Streak: <value> 
# Line 2: Eligible: <Yes/No>

n=int(input())
attend=list(map(int,input().split()))
streak=1
maxst=0
acv="No"
for i in range(0,n-1):
    if(attend[i]==attend[i+1]):
        streak+=1
    else:
        maxst=max(maxst,streak)
        streak=1
maxst=max(maxst,streak)
if(streak>=5):
    acv="Yes"
print("Longest Streak:",maxst)
print("Eligible:",acv)