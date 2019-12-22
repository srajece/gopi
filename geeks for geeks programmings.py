'''
from collections import ChainMap
a={'name':'Raj','mail':'srajece','mobno':'9876554321'}
address={'city':'chennai','state':'tamilnadu','pin':'600001'}
c=ChainMap(a,address)
print(c.maps)
print(c['state'])
'''

''''
from collections import ChainMap
a={'name':'Raj','mail':'srajece','address':{'city':'chennai',
    'state':'tamilnadu','pin':'600001'},'mobno':'9876554321'}
b=a['address']
c=ChainMap(a,b)
print(c.maps)
print(c['state'])
'''
