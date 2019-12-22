#pattern 1 using while
'''
i=1
while(i<=5):
    print('*'*i)
    i=i+1
'''

#pattern 1 using for
''''
n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()
'''
    
#patern 2 using for
'''
n=int(input("Enter the number: "))
for i in range(n,0,-1):
    for j in range(i):
        print('*',end=" ")
    print()
'''

#pattern 3 using for
'''
n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
'''

#pattern 4 using for
'''
n=int(input("Enter the number: "))
for i in range(n,0,-1):
    for j in range(i):
        print(i,end=" ")
    print()
'''

#pattern 5 using for
'''
n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(n+1-i,0,-1):
        print(j,end=" ")
    print()
'''

#pattern 6 using for
'''
n=int(input("Enter the number: "))
a=0
for i in range(n,0,-1):
    for j in range(i):
        a+=1
        print(a,end=" ")
    print()
'''

#patter 7 using for
'''
n=int(input("Enter the number: "))
a=0
k=1
for i in range(1,n+1):
    for j in range(k):
        a+=1
        print(a,end=" ")
    k+=2    
    print()
'''

#pattern 8 using for
'''
n=int(input("Enter the number: "))
a=0
for i in range(1,n+1):
    for j in range(i):
        a+=1
        print(a,end=" ")
    print()
'''
