def isevenodd(num):
    """
    This function reeeturns if a number is even or odd 
    input-Any valid Integer
    output-odd/even
    """
    if(type(num)==int):
        if num%2==0 :
                return 'even'
        else:
                return 'odd'
    else:
          return 'pagal he kya dekha function kya he'   
for i in range(1,11):
    x=isevenodd(i)
    print(i,'--',x)
