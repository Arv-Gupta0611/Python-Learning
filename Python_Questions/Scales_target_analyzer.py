# Problem Statement
# A salesperson has a monthly target. Given daily sales,
#  determine whether the target was achieved and calculate the percentage of the target completed.
# Constraints
# 1 <= n <= 31; sales and target are non-negative.
# Input Format
# Line 1: target 
# Line 2: daily sales.
# Output Format
# Line 1: Total Sales: <value> 
# Line 2: Achievement: <Yes/No>, Percentage: <percentage>

target=int(input())
sales=list(map(int,input().split()))
total=sum(sales)
length=len(sales)
acv="NO"
if total>target:
    acv="Yes"
perc=(total / target)*100
print(f"Total Sales:{total}")
print(f"Achievment:{acv},Percentage:{perc:.2f}%")