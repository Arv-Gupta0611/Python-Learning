squares={i:i**2 for i in range(1,6)}
print(squares)
dist={'delhi':1045,'kolkata':6742}
print({key:value*2 for (key,value) in dist.items()})
# Using zip
days=['Sunday','Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday']
tempC=[30.5,43.8,22.9,40.2,36.3,35.8,29.8]
d9={i:j for (i,j) in zip(days,tempC)}
print(d9)
print({i:{j:i*j for j in range(1,11)} for i in range(2,5)})