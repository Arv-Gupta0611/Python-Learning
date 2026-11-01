for i in range(5,0,-1):
    for j in range(0,5-i):
        print(' ',end=" ")
    for k in range(1,2*i):
        if(k==1 or k==(2*i-1) or i==5):
            print('*',end=" ")
        else:
            print(' ',end=" ")
        
    print()