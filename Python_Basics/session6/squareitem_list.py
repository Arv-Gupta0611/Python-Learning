def transform(f,L):
    output=[]
    for i in L:
        output.append(f(i))
    print(output)
l=[1,2,3,4,5]
transform(lambda x:x**2 ,l)

ll=[1,2,3,4,5]
result=map(lambda i:i**2 ,ll)
print(list(result))