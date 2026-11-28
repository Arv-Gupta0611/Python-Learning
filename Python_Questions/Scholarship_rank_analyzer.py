# Problem Statement
# Scholarship points are awarded as 3 points for marks 90+, 2 points for 75–89, 1 point for 60–74, and 0 below 60.
# Calculate total points and determine whether scholarship is earned with at least 5 points.
# Constraints
# 1 <= n <= 20; 0 <= marks <= 100.
# Input Format
# Line 1: n 
# Line 2: marks.
# Output Format
# Line 1: Total Points: <points> 
# Line 2: Scholarship: <Yes/No>

n=int(input())
marks=list(map(int,input().split()))
point=0
sch="No"
for p in marks:
    if p>90:
        point+=3
    elif 75 <= p <= 90:
        point+=2
    elif 60 <= p < 75:
        point+=1
    else:
        point+=0
if (point>=5):
    sch="Yes"
print("Total Points:",point)
print("Scholarship:",sch)