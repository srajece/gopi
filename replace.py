'''a=input("Enter t-he string")
b=a.replace("plus","+").replace("mul","*").replace("minus","-").replace("div","/")
print(eval(b))'''

'''name=input("Enter the String: ")
DOB=input("Enter DOB: ")
print("Hiii...{n} {d} {i:.3f} Welcome to BITA".format(n=name,d=DOB,i=6.66666666))'''

'''print('/{:<10}/{:^10}/{:>12}'.format("welcome","to","BITA"))'''

'''a=[]
c=0
for i in range(1001):
    if i%3==0 or i%5==0:
        a.append(i)
        c+=1
print(a)
print(c)
print(len(a))
print(max(a))
print(min(a))'''

'''v=['a','e','i','o','u']'''

'''a=[1,[2,3,4],[5,6,7]]
print(a[1])
print(a[1][2])'''

'''a=[[i for i in range(3)]for j in range(3)]
print(a)'''

'''a=[i for i in range(1001) if not i%3  or not i%5]
print(a)'''

'''a=[1,2,3,4]
b=[1,'jghj',6]
a.extend(b)
print(a)
a.append(b)
print(a)'''

'''l=[9,6,42,30]
for i in l:
    for j in i:
        if i>j==0:
            t=i
            i=j
            j=t
    print(t)

'''


c=['Ford','BMW','Volvo']
b=c.sort()
print(b)

