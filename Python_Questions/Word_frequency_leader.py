# Problem Statement
# A text analyzer receives words. Find the most frequent word, ignoring case. 
# If multiple words have the same frequency, choose the word appearing first.
# Constraints
# 1 <= n <= 100; words contain only alphabetic characters.
# Input Format
# Line 1: n 
# Line 2: n words.
# Output Format
# Line 1: Unique Words: <count> 
# Line 2: Most Frequent: <word>

n=int(input())
words=list(map(str,input().split()))
counts={}
maxim=0
wrd=""
for o in words:
    counts[o.lower()]=counts.get(o,0)+1
for key,value in counts.items():
    if(value>maxim):
        wrd=key
        maxim=value
print("Unique Words:",len(counts))
print("Most Frequent:",wrd)