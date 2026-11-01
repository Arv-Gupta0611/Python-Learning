def transform(f,L):
    output=[]
    for i in L:
        output.append(f(i))
    print(output)
l=[1,2,3,4,5]
transform(lambda x:x**2 if(x%2!=0) else x**3 ,l)