# Problem Statement
# A security system classifies a number as Special if it is divisible by 3 or 5, but not by both.
#  Count the Special numbers and find the largest Special number.
# Constraints
# 1 <= n <= 100; 1 <= number <= 10000.

n=int(input())
l=list(map(int,input().split()))
m=[]
count=0
maximum=float('-inf')
for i in l:
    if(i>maximum):
        maximum=i
    a=i%3==0
    b=i%5==0
    if(a==b):
        count+=1
        m.append(i)
print("Special Numbers:",count)
print("Largest",max(m))