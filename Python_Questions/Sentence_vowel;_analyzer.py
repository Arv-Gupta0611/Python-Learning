# Problem Statement
# A language-learning application analyzes a sentence. 
# Count the vowels and determine which vowel occurs most frequently. In case of a tie, choose the vowel in the order a, e, i, o, u.
# Constraints
# Sentence length <= 200; lowercase English letters and spaces.
# Input Format
# One line containing the sentence.
# Output Format
# Line 1: Vowels: <count> 
# Line 2: Most Frequent: <vowel>

sent=input().lower()
l=["a","e","i","o","u"]
a=sent.count("a")
e=sent.count("e")
i=sent.count("i")
o=sent.count("o")
u=sent.count("u")
vow=a+e+i+o+u
character=[]
for ch in sent:
    if ch in l:
        character.append(ch)
counts={}
for i in character:
    counts[i]=counts.get(i,0)+1

maximum=0
most="None"
for ch in l:
    if counts.get(ch,0)>maximum:
        maximum=counts.get(ch,0)
        most=ch
print("Vowels:",vow)
print("Most Frequent:",most)