units=int(input('enter no.of units '))
bill=0
if(units<=100):
    bill=2*units
    print('Electricity Bill ',bill)
elif(units<=200):
    units=units-100
    bill=2*100+3*units
    print('Electricity Bill ',bill)
else:
    units=units-200
    bill=2*100+3*100+5*units
    print('Electricity Bill ',bill)