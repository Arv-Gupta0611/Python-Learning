def square(num):
    return num**2
print(type(square))
print(id(square))

x=square
print(id(x))
print(x(3))

# del square
# print(square(3))

L=[1,2,3,square]
print(L[-1](4))
s={square}
print(s)