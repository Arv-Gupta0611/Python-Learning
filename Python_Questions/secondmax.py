def sec_max(l):
    max=float("-inf")
    secmax=float("-inf")
    for i in range(0,len(l)):
        if(max<l[i]):
            max=l[i]
    for i in l:
        if i>secmax and i<max:
            secmax=i
    return max,secmax

a=list(map(int,input().split()))
g,h=sec_max(a)
print("Max",g)
print("Second Max",h)