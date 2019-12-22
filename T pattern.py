# pattern T
'''
print("T in star pattern")
n=int(input("Enter the Value: "))
for i in range(0,1):
    for j in range(0,n):
        print("*",end="")
    print()
for i in range(1,n):
    for j in range(int(n/2)):
        print(" ",end="")
    print("*")
'''

# pattern R
print("R in star pattern")
#row=int(input("Enter the Row value: "))
#col=row-2
for i in range(7):
    for j in range(5):
        if (i==0 and ((j!=0) and (j!=4))) or (i>0 and (j==0 or (i<3 and j==4))) or (i==3):
            print("*",end="")
        else:
            print(" ",end="")
        
    
    print()
    
