s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1|s2)
print(s1&s2)
print(s1-s2)
print(s2-s1)
print(s1^s2)
print(1 not in s1)
print(4 in s1 and 4 in s2)
for i in s1:
    print(i)
print('length',len(s1))
print(sum(s1))
print(min(s1))
print(max(s1))
print(sorted(s1, reverse=True))       #return in List variable
print(s1.union(s2))
print(s1.update(s2))
ss=s1.update(s2)
print(ss)
print(s1)
print(s2)
print(s1.intersection(s2))
print(s1.intersection_update(s2))
print(s1)
print(s2)
print(s1.symmetric_difference(s2))
print(s1.symmetric_difference_update(s2))
print(s1)
print(s2)
print(s1.isdisjoint(s2))
s3={4,5}
print(s3.issubset(s1))    ##checks if set in parameter 
                           # contain elements of another set
print(s3.issubset(s2))
print(s3.issuperset(s1))    ##checks if set in parameter 
print(s1.issuperset(s3))     # is contained in another set
s8={1,2,3}
s9=s8.copy()
print(s8)
print(s9)

#frozzenset 
fs=frozenset((1,2,6,9,5,8))
print(fs)
## All operations will work 
## Functions Works 

#Set Comprehension
num={i**2 for i in range(1,11) if i%2!=0 }
print(num)
