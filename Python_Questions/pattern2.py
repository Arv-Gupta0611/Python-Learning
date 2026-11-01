# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(i,end=" ")
#     print()
p=int(input('enter no. of rows '))
n=p-1
m=1
for i in range(p,0,-1):
    for j in range(n,0,-1):
        print(' ',end=' ')
    n-=1
    for k in range(m,0,-1):
        print('*',end=" ")
    m+=1
    print()
