'''
s="{a[for apple],b[for ball}"
dict1={'a':'1','b':'2'}
t=s.maketrans(dict1)
print(s.translate(t))
'''

'''
s="{a[for apple],b[for ball}"
a='abpf'
b='1234'
t=s.maketrans(a,b)
print(t)
'''

s="{a[for apple],b[for ball}"
a='abpf'
b='1234'
c="{[]},"
t=s.maketrans(a,b,c)
print(s.translate(t))
