# Problem Statement
# A monitoring system receives values over time. 
# Count how many values become a new maximum when scanning from left to right. 
# The first value always counts as a new maximum.
# Constraints
# 1 <= n <= 100; values are integers.
# Input Format
# Line 1: n 
# Line 2: values.
# Output Format
# Line 1: New Maximums: <count> 
# Line 2: Final Maximum: <value>

n=int(input())
val=list(map(int,input().split()))
maxim=val[0]
count=1
for i in range(1,len(val)):
    if val[i]>maxim:
        maxim=val[i]
        count+=1
print("New Maximumms:",count)
print("Final Maximum:",maxim)  
