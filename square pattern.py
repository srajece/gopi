# Square Pattern

n=int(input("Enter the Value: "))
box=int((n+1)/2)
low=0
high=n-1
c=1
array1=[[0 for i in range(n)]for j in range(n)]
for i in range(box):
    for j in range(low,high+1):
        array1[low][j]=c
        c+=1
    for j in range(low+1,high+1):
        array1[j][high]=c
        c+=1
    for j in range(high-1,low-1,-1):
        array1[high][j]=c
        c+=1
    for j in range(high-1,low,-1):
        array1[j][low]=c
        c+=1
    low+=1
    high-=1

for i in range(n):
    for j in range(n):
        print(array1[i][j],end="\t")
    print()
   
