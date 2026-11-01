a=0
b=1
print(a,b,end=" ")
for i in range(3,11):
    print(a+b,end=" ")
    temp=a+b
    a=b
    b=temp