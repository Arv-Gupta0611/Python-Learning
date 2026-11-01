for i in range(1,6):
    for k in range(5-i,0,-1):
        print(' ',end=" ")
    for j in range(0,2*i-1):
        if(j==0 or j==(2*i-2)):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
for i in range(4,0,-1):
    for j in range(0,5-i):
        print(' ',end=" ")
    for k in range(1,2*i):
        if(k==1 or k==(2*i-1)):
            print('*',end=" ")
        else:
            print(' ',end=" ")
        
    print()
