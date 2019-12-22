n=int(input("Enter the values: "))
a=n*2-1
low=0
high=a-1
array1=[[0 for i in range(a)]for j in range(a)]
for i in range(a):
    for j in range(low,high+1):
        array1[low][j]=n
    for j in range(low+1,high+1):
        array1[j][high]=n
    for j in range(high-1,low-1,-1):
        array1[high][j]=n
    for j in range(high-1,low,-1):
        array1[j][low]=n

    low+=1
    high-=1
    n-=1
    
for i in range(a):
    for j in range(a):
        print(array1[i][j],end="\t")
    print()
