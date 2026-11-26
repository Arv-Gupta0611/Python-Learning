# Problem Statement
#  A shopping app records product IDs purchased by a customer.
#  Repeated IDs represent repeated purchases of the same product.
#  Find the number of unique products and the product appearing most frequently.
#  If there is a tie, choose the product appearing first.
# Constraints
#   1 <= n <= 100; product IDs are positive integers.
# Input Format
# Line 1: n 
# Line 2: product IDs.
# Output Format
# Line 1: Unique Products: <count> 
# Line 2: Most Frequent: <product>

n=int(input())
ids=list(map(int,input().split()))
counts = {}
for product in ids:
    counts[product] = counts.get(product, 0) + 1
# for product in ids:
#     if product in counts:
#         counts[product] += 1
#     else:
#         counts[product] = 1
unique_count = len(counts)
most_frequent = ids[0]
max_freq = 0

for product in ids:
    if counts[product] > max_freq:
        max_freq = counts[product]
        most_frequent = product

print("Unique Products:", unique_count)
print("Most Frequent:", most_frequent)
