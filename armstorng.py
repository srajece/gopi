
import time
n=int(input("Enter the value: "))
start=time.time()
s=0
t=n
while t>0:
    a=t%10
    s=s+a**3
    t=int(t/10)
    print(t)
time.sleep(5)
if n==s:
    print("Given number is Armstrong")
else:
    print("Given number is not Armstrong")
end=time.time()
print("Execution time: ",end-start)


#
'''
import time
n=input("enter the value: ")
start=time.time()
s=0
for i in n:
    s+=int(i)**3
if int(n)==s:
    print("Given number is Armstrong")
else:
    print("Given number is not Armstrong")
end=time.time()
print("Execution time: ",end-start)
'''
