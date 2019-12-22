fs=input("Enter the First String: ").lower()
ss=input("Enter the Second String: ").lower()
fs=list(fs)
ss=list(ss)
print(fs,ss)
for i in range(len(fs)):
    for i in fs:
        for j in ss:
            print(i,j)
            if i == j:
                fs.remove(i)
                ss.remove(j)
                print(fs,ss)
                break
t=fs+ss
print(t)
ans='flames'
for i in range(len(ans)):
    if (len(t) > len(ans)):
        c=ans[(len(t)%len(ans)):]+ans[:(len(t)%len(ans)-1)]
        ans=c
        print(c)
    elif (len(t)==len(ans)):
        c=ans[:len(t)-1]
        ans=c
        print(c)
    else:
        c=ans[len(ans)-1]
        ans=c
        print(c)
        
        
