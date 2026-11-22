def eq_ind():
    l=list(map(int,input().split(",")))
    total=0
    for i in l:
        total+=i
    left=0
    for i in range(len(l)):
        right=total-left-l[i]
        if left==right:
            return i
        left+=l[i]
    return -1
print(eq_ind())