#iter
'''
a=[1,2,3]
my=iter(a)
print(next(my))
print(next(my))
print(next(my))
'''

#
from collections import ChainMap
dict1={'name':'Raj','mail':'srajece',
   'address':{'city':'chennai',
    'state':'tamilnadu','pin':'600001'},
       'mobno':'9876554321'}


|'''
print(dict1['address']['state'])
print(len(dict1))
print(dict1['name'])
print(dict1.get('name'))
print(dict1.keys())
'''

'''
for i in dict1:
    print(dict1[i])
'''

'''
*output
Raj
srajece
{'city': 'chennai', 'state': 'tamilnadu', 'pin': '600001'}
9876554321
'''

'''
for i in dict1.values():
    print(i)
'''

'''
*output
Raj
srajece
{'city': 'chennai', 'state': 'tamilnadu', 'pin': '600001'}
9876554321
'''

'''
x=('k','h','d')
y=0
dict2=dict.fromkeys(x,y)
print(dict2)
'''

'''
car={ "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x=car.items()
print(x)
'''

'''
car={ "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)
'''

'''
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"model": "White"})
print(car)
'''
