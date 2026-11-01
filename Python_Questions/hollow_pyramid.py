for i in range(1,6):
    for k in range(5-i,0,-1):
        print(' ',end=" ")
    for j in range(0,2*i-1):
        if(j==0 or j==(2*i-2) or i==5):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

