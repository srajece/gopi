#some of elements in a given list
'''
a=list(input('enter the element: ').split(' '))
t=0
for i in range(0,len(a)):
    t=t + int(a[i])
print(t)
'''



#Multiply the all the elements in a list
'''
a=list(input('Enter the Elements: ').split(' '))
print(a)
t=1
for i in range(0,len(a)):
    t = t * int(a[i])
print(t)
'''


#get the largest number from list
'''
a=list(input("Enter the number: ").split(' '))
print(a)
m=0
for i in range(0,len(a)):
    if int(a[i])> m:
        m=int(a[i])
print(m)
'''


#get the smallest number from list
'''
a=list(input("Enter the number: ").split(' '))
print(a)
k=min(a)
print(k)
m=1
for i in range(0,len(a)):
    if int(a[i]) < m:
        m=int(a[i])
print(m)
'''


#
'''
a=['a','abc','xyz','aba','1221']
count=0
c=0
t=''
for i in a:
    count=len(i)
    if count>=2:
        t=i
        if t[0]==t[-1]:
            c=c+1
print('Answer is:',c)
'''


#delete the duplicate items in a list
'''
a=[10,20,30,20,10,50,60,40,80,50,40]
a=set(a)
print(a)
'''


#check a list is  empty or not
'''
a=[10,20,30,20,10,50,60,40,80,50,40]
if not a:
    print('empty')
else:
    print("List have a some values")
'''


#select the common member in the two list
a=[1,2,4,7,9,3]
b=[4,87,3,72,7]
for i in a:
    for j in b:
        if i == j:
            print(i)
print('lists have a some common elements')
