# select only special character in given input
'''
a=input("Enter the statement with special character and numerics: ")
for i in a:
    if i.isalpha()==False:
        if i.isdigit()==False:
            print(i,end="")
'''

# select only alphabet in given input
'''
a=input("Enter the statement with special character and numerics: ").split(" ")
for i in a:
    for j in i:
        if j.isalpha():
            print(j,end="")
    print()
'''

'''
a=input("Enter the statement with special character and numerics: ")
for i in a:
    if i.isalpha():
        print(i,end="")
'''

#select only digit in given input
'''
a=input("Enter the statement with special character and numerics: ")
for i in a:
    if i.isdigit():
        print(i,end="")
'''

# Give the target and multiply then check the number palindrome then print the highest 
'''
i=int(input("Enter the target number: "))
t=0
for n1 in range(i):
    for n2 in range(i):
        p=str(n1*n2)
        r=p[::-1]
        if(r==p):
            if(int(t)<int(p)):
                t=p
                a,b=n1,n2
print(a,b,t)
'''
        
