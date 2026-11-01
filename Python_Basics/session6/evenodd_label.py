# def transform(f,L):
#     for i in L:
#         print(i,'-->',f(i))
# l=[33,53,62,34,59,22]
# transform(lambda x:'even' if(x%2==0) else 'odd' ,l)

ll=[33,53,62,34,59,22]
result=map(lambda i:'even' if(i%2==0) else 'odd',ll)
print(list(result))
