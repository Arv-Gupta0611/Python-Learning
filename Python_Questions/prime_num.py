for i in range(1,151):
    count=0
    for j in range(1,i+1):
        if i%j ==0:
            count+=1
    if count==2:
        print(i,end=' ')


for l in range(1,151):
    flag=False
    for  m in range(2,l):
        if l%m ==0:
            flag=True
            break
    if not flag:
        print(l,end=' ')
