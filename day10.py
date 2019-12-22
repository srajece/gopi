#Leap Year
'''
y=int(input("Enter the Year: "))
if y%4==0:
    if y%100==0:
        if y%400==0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Not a Leap Year")
else:
    print("Not a Leap Year")
'''

#prime number
'''
a=[]
sum1=0
for i in range(1,100):
    if i>1:
        for j in range(1,i):
            if j>1:
                if i%j==0:
                    break
        else:
            a.append(i)
            if sum1<50:
                sum1=sum1+i
                if sum1< 50:
                    k=sum1
print(k,a)
'''

#
'''
a=list(input("Enter the string: ").split(" "))
b=[]

print("Task One: ",a)
for i in a:
    for j in i:
       b.append(j)
print(b)
print("".join(b))
'''

#
'''
v=['a','e','i','o','u']
a=list(input("Enter the String: ")
print(a)
for i in a:
    for j in i:
        if j in v:
            j=chr(ord(j)+1)
            print(('').join(j),end="")
            
        else:
            print(('').join(j),end="")
    print(end=" ")
'''

#
'''
n=input("Enter the String: ").split()
print(n)
n[0],n[-1]=n[-1],n[0]
print(n)
print(" ".join(n))
'''

#
'''
s="abcd"
n=int(input())
print(s[n::]+s[0:n])
'''

