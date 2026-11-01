n=int(input("Enter no. of rows you want = "))
for i in range(0,n):
    for sp in range(1,n-i):
        print(" ", end=" ")
    for pr in range(0,2*i+1):
        print("*", end=" ")
    print()