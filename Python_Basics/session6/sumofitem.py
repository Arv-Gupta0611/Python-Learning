import functools
l=[1,2,3,4,5]
output=functools.reduce(lambda x,y:x+y ,l)
print(output)