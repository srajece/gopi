#
'''
n=int(input("Enter the value: "))
for i in range(1,n+1):
    for i in range(1,i+1):
        print("*",end="")
    print()
'''

#
'''
n=int(input("Enter the value: "))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*",end="")
    print()
'''
#
'''
n=int(input("Enter the value: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
 '''

#
'''
n=int(input("Enter the value: "))
for i in range(0,n):
    for j in range(n,i,-1):
        print(j,end="")
    print()
'''

#
'''
n=int(input("Enter the value: "))
for i in range(0,n):
    for j in range(n-i,0,-1):
        print(j,end="");
    print()
'''

#
'''
n=int(input("Enter the number: "))
n1=1
for i in range(1,n+1):
    for j in range(0,i):
        print(n1,end="")
        n1+=1
    print()
'''

#
'''
n=int(input("Enter the number: "))
n1=1
k=1
for i in range(1,n+1):
    for j in range(0,k): #(0,i*2-1)
        print(n1,end="")
        n1+=1
    k+=2
    print()
'''

#
'''
n=int(input("Enter the value: "))
for i in range(1,n+1):
    for j in range(i,n+1):
        print(" ",end="")
    for j in range(0,i*2-1):
        print("*",end="")
    print()
'''

#
'''
n=int(input("Enter the value: "))
for i in range(1,n+1):
    for j in range(i,n+1):
        print(" ",end="")
    for j in range(0,i):
        print("* ",end="")
    print()
'''

#
'''
n=int(input("Enter the value: "))
for i in range(1,n+1):
    for j in range(1,n*2-i):
        print(j,end="")
    print()
'''

#
'''
n=int(input("Enter the value: "))
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
    print()
'''

#
'''
n=int(input("Enter the value: "))
for i in range(1,n+1):
    for j in range(0,i):
        print(format(2**j,"5d"),end="")
    print()

'''
