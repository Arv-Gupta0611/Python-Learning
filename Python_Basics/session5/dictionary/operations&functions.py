#iterations
d={'name': 'arv','college':'gla'}
d2={'name': 'arv','college':'gla university'}
for i in d:
    print(i,'--',d[i])
#Functions
print(d.items())
print(d.keys())
print(d.values())
d3=d.update(d2)
print(d)