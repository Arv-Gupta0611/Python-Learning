# Problem Statement
# Each delivery is represented as priority:distance. High has priority score 3, Medium 2 and Low 1.
#  A delivery is Urgent if its priority score is at least 2 and its distance is greater than 20 km.
#  Count urgent deliveries and find their maximum distance.
# Constraints
# 1 <= n <= 100; distance > 0; priority is High, Medium or Low.
# Input Format
# Line 1: n 
# Line 2: n priority:distance values.
# Output Format
# Line 1: Urgent Deliveries: <count> 
# Line 2: Maximum Urgent Distance: <distance>
# Test Case 1
# Input
# 4 
# High:30 Medium:15 Low:40 High:25
# Output
# Urgent Deliveries: 2 
# Maximum Urgent Distance: 30
# Explanation
# High:30 and High:25 are urgent. Medium:15 is too short and Low:40 has insufficient priority.


n=int(input())
sentence=input()
l={"High":3,"Medium":2,"Low":1}
urg_del=0
maxim=0
data=sentence.split()
for item in data:
    key,value=item.split(":")
    if(l[key]>=2 and int(value)>20):
        urg_del+=1
        if(int(value)>maxim):
            maxim=int(value)
print("Urgent Deliveries:",urg_del)
print("Maximum Urgent Distance:",maxim)