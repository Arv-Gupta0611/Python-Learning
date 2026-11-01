def f():
    def x(a,b):
        return a+b
    return x
val=f()(6,4)
print(val)