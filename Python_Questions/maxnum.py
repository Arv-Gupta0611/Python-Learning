a=int(input ('Enter the first no.'))
b=int(input ('Enter the second no.'))
c=int(input ('Enter the third no.'))
if(a>b):
    if(a>c):
        print('Max no.',a)
    else:
        print('Max no',c)
elif(a==b):
    if(a>c):
        print('Max no.',a)
    else:
        print('Max no.',c)
else:
    if(b>c):
        print('Max no.',b)
    else:
        print('Max no.',c)
