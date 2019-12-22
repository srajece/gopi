# fibonoci

n=int(input("Enter the value: "))
a=0
b=1
ans=[1]
if n<0:
    print("Please enter positive number")
elif n==0:
    print("Please enter natural number")
else:
    for i in range(n):
        c=a+b
        a=b
        b=c
        ans.append(b)
print(ans)


#

