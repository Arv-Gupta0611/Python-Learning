# def multiply(a=1,b=1):
#     return a*b
# print(multiply(2,3))

def multiply(*args):
    """
    This function calculate the multiplication of all the arguments
    """
    product=1
    for i in args:
        product=product*i
    print(args)     #all arguments stored in a tuple
    return product
print(multiply(1,2,3,4,5,6))

print(multiply.__doc__) # Prints the documentation