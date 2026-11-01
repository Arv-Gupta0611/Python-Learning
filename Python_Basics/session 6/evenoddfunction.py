def is_even(num):   #parameter
    """
    this function returns the given no. is even or not
    Input - any valid integer
    output - even?odd
    """
    if(type(num) == int):
        if(num%2==0):
            return "even"
        else:
            return "odd"
    else:
        return "pagal he kya"
for i in range(1,11):
    x=is_even(i)    #argument
    print(i,x)