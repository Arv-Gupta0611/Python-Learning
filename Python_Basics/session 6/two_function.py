def func_a():
    print("inside func_a")
def func_b(z):
    print("inside func_b")
    return z()
func_b(func_a)
