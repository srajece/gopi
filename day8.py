# access the Global Declaration in function
'''
c=1
def func():
    c+=1
    print(c)
a=func()

# UnboundLocalError: local variable 'c' referenced before assignment
'''

'''
c=1
def func():
    global c
    c+=1
    print(c)
a=func()
'''

# lamda
'''
def fun(n):
    return (lambda x:x+n)
    
a=fun(5)
print(a(3))
'''

#file
'''
f=open("E:/BITA/python/Day 8 (07.09.19)/test.txt",'a')
f.write("delhi")
f.close()
f=open("E:/BITA/python/Day 8 (07.09.19)/test.txt",'r')
print(f.read())
'''

#pattern
'''
n=int(input("Enter the value: "))
for i in range(1,n+1):
    for j in range(i-1,n):
        print(" ",end="")
    
    for j in range(1,((i*2-1)+1)):
        print("*",end="")
    print()
'''
