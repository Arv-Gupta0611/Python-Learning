# d={}
# print(type(d))
d1={'name': 'arv','gender':'male'}
print(d1)

d2={(1,2,3):['a','b','c'],'hello':1}
print(d2)

std={
    'college':'GLA',
    'name': 'arv',
    'gender':'male',
    'semester': 1,
    'subjects':{
        'web-dev':2,
        'maths':4,
        'physics':3,
        'ind.cert':2,
        'tech.eng':3
    }
}

std['subjects']['case-study']=2
print(std)
del std['subjects']['case-study']
print(std)


d4= dict([('name','arv'),('college','gla')])
print(d4)
print(d4['name'])
print(d4.get('college'))

#adding key values
d4['subject']='python'
print(d4)

