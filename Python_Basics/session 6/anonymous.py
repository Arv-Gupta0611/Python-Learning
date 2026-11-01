l=[
    {'name': 'Rahul',
    'age':'45',
    'gender': 'male'
    },
    {
    'name': 'Nitish',
    'age':'33',
    'gender': 'male'
    },
    {
    'name': 'Ankita',
    'age':'50',
    'gender': 'female'
    }
]
output=map(lambda names:names['name'],l)
print(list(output))
output=map(lambda ages:ages['age'],l)
print(list(output))