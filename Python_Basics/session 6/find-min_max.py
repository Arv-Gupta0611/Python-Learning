import functools
l=[33,53,62,34,59,22]
print(functools.reduce(lambda x,y:x if x<y else y,l))
print(functools.reduce(lambda x,y:x if x>y else y,l))
