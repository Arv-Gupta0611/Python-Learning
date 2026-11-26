# Problem Statement
# A college evaluates a batch using a list of marks.
#  A batch is called Balanced if the difference between the highest and lowest marks is at most 20.
#  Calculate the average, determine whether the batch is Balanced, and count how many students scored above the average.
# Constraints
# 1 <= n <= 100; 0 <= marks <= 100.

n=int(input())
l=list(map(int,input().split()))[:n]
maximum=float('-inf')
minimum=float('inf')
sum=0
count=0
for num in l:
    sum+=num
    if num>maximum:
        maximum=num
    if num<minimum:
        minimum=num 
difference=maximum-minimum
average=sum/len(l)
for num in l:
    if(num>average):
        count+=1
if difference>=20:
    print("Balanced")
else:
    print("Not Balanced")
print("Above Average:",count)