#creating tuple
t1=()
print(t1)
#single element
t2=('hello',)
print(t2)
print(type(t2))
#homo
t3=(1,2,3,4)
print(t3)
#hetero
t4=(1,'hello',True,[1,2,30])
print(t4)
#tuple
t5=(1,3,(5,7,9))
print(t5)
#using type conversion
t6=tuple('calculus')
print(t6)