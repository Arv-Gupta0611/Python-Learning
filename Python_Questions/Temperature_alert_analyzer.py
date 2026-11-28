# Problem Statement
# A weather station records temperatures.
# A day is an alert day if its temperature is at least 5 degrees above the average temperature. 
# Count alert days and find the highest temperature.
# Constraints
# 1 <= n <= 100; -50 <= temperature <= 60.
# Input Format
# Line 1: n 
# Line 2: temperatures.
# Output Format
# Line 1: Alert Days: <count> 
# Line 2: Highest Temperature: <value>

n=int(input())
temp=list(map(int,input().split()))
total=sum(temp)
avg=total/n
count=0
maxim=float("-inf")
for i in temp:
    if(i>avg+5):
        count+=1
    if(i>maxim):
        maxim=i
print("Alert Days:",count)
print("Highest Temperature:",maxim)