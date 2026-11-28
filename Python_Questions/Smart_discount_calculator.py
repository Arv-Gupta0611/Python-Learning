# Problem Statement
# An online store applies 0% discount below ₹1000, 10% for ₹1000–₹4999, 20% for ₹5000–₹9999 and 30% for ₹10000+.
# Members receive an additional 5% discount after the first discount.
# Constraints
# 1 <= amount <= 1000000; membership is Yes or No.
# Input Format
# One line: amount membership.
# Output Format
# Line 1: Discount: <amount> 
# Line 2: Final Bill: <amount>

amount,membership=input().split()
amount=int(amount)
discount=0
if amount>=10000:
    disc=0.30*amount
elif 5000<=amount<10000:
    disc=0.20*amount
elif 1000<=amount<5000:
    disc=0.10*amount
else:
    disc=0
remaining = amount - disc
if(membership=="Yes"):
    disc+=(0.05*remaining)
print("Discount:",disc)
print("Final Bill:",amount-disc)