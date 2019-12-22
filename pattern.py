#pattern

'''
n=int(input("Enter the value: "))
for i in range(1,n+1):
    for j in range(0,i):
        print("*",end="")
    print()
for i in range(1,n):
    for j in range(0,n-i):
        print("*",end="")
    print()
'''

'''
//output

*
**
***
****
*****
****
***
**
*

'''

#
'''
n=int(input("Enter the value: "))
for i in range(1,n+1):
    for j in range(0,n-i):
        print(" ",end="")
    for j in range(0,i):
        print("*",end="")
    print()
for i in range(1,n):
    for j in range(0,i):
        print(" ",end="")
    for j in range(0,n-i):
        print("*",end="")
    print()
'''

'''
//output

    *
   **
  ***
 ****
*****
 ****
  ***
   **
    *
'''

#
'''
n=int(input("Enter the value: "))
for i in range(1,n+1):
    for j in range(0,n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("* ",end="")
    print()
for i in range(1,n):
    for j in range(0,i):
        print(" ",end="")
    for j in range(0,n-i):
        print("* ",end="")
    print()
'''

'''
//output

Enter the value: 5

    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 

'''

#
'''
a=100
def function():
    global a
    print(a)
    a=50
    print("after")
function()
print(a)
'''

#
'''
#
import math
k=1
n=int(input("Enter the value: "))
for i in range(1,n+1):
    for j in range(0,n-i):
        print(" ",end="")
    for j in range(0,math.ceil(i/2)):
        print("* ",end="")
    print()
for i in range(1,n):
    for j in range(1,i+1):
        print(" ",end="")
    for j in range(0,):
        print("* ",end="")
    print()

'''
