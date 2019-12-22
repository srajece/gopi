import re
print("Press 1 to Login , Press 2 to Sign-Up")
n=int(input("Enter Your Choice:"))
temp=' '
if n==1:
    print("Login")
    f=open('test.txt','r').read()
    un=input("Enter the Username:")
    if un!=temp:
        pw=input("Enter the Password:")
        for i in f.split(';'):
            if re.match("Username="+un+",Password="+pw,i):
                print("Login Successfully")
            else:
                print("Login failed")
    else:
        print("User Not Found")
        
elif n==2:
    print("Signup")
    un=input("Enter the Username:")
    if un!='':
        f=open("test.txt",'a')
        f.write("Username="+un+",")
        pw=input("Enter the Password:")
        f.write("Password="+pw+";")
        f.close()
    f=open("test.txt",'r')
    f=f.read()
    print(f)
    

else:
    print("Please Enter the Correct Choice")

    
