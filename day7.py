#palindrome using function
'''
def palin(i):
    t=0
    for n1 in range(i):
        for n2 in range(i):
            p=str(n1*n2)
            r=p[::-1]
            if(r==p):
                if(int(t)<int(p)):
                    t=p
                    a,b=n1,n2
    print(a,b,t)
i=int(input("Enter the value: "))
palin(i)
'''

#primenumber series using function
'''
def prime(sn,en):
    a=[]
    c=0
    for n in range(sn,en):
        if n>1:
            for dn in range(1,n):
                if(dn>1):
                    if(n%dn==0):
                        break
            else:
                a.append(n)
                c+=1
                if c==10001:
                    break
    print(a[-1])
    print(c)
sn=int(input("Enter the starting number: "))
en=int(input("Enter the ending number: "))
prime(sn,en)
'''

#class
'''
class calc:
    print("Hai...")
    def add(self,a,b):
        c=a+b
        return c
    def sub(self,a,b):
        c=a-b
        return c
    print("Hello...")
a=calc()
print(a.add(5,3))
print(a.sub(5,3))
print("Bye...")
'''

#classes
'''
class Calc:
    print("Hai...")
    def add(self,a,b):
        c=a+b
        return c
    def sub(self,a,b):
        c=a-b
        return c
    print("Hello...")
class NewCalc(Calc):
    def mul(self,a,b):
        c=a*b
        return c
    def div(self,a,b):
        c=a/b
        return c
    
a=NewCalc()
print(a.add(5,3))
print(a.sub(5,3))
print(a.mul(5,3))
print(a.div(5,3))
print("Bye...")
'''

# multiple classes
'''
class Calc:
    print("Hai...")
    def add(self,a,b):
        c=a+b
        return c
    def sub(self,a,b):
        c=a-b
        return c
    print("Hello...")
class NewCalc():
    def mul(self,a,b):
        c=a*b
        return c
    def div(self,a,b):
        c=a/b
        return c
class Modern(Calc,NewCalc):
    def sqr(self,a):
        c=a**a
        return c
a=Modern()
print(a.add(5,3))
print(a.sub(5,3))
print(a.mul(5,3))
print(a.div(5,3))
print(a.sqr(3))
print("Bye...")
'''

#Multilevel
'''
class Calc:
    print("Hai...")
    def add(self,a,b):
        c=a+b
        return c
    def sub(self,a,b):
        c=a-b
        return c
    print("Hello...")
class NewCalc(Calc):
    def mul(self,a,b):
        c=a*b
        return c
    def div(self,a,b):
        c=a/b
        return c
class Modern(NewCalc):
    def sqr(self,a):
        c=a**a
        return c
    def mod(self,a,b):
        c=a%b
        return c
a=Modern()
print("Addition",a.add(5,3))
print("Subraction:",a.sub(5,3))
print("Multiplication:",a.mul(5,3))
print("Divition:",a.div(5,3))
print("Square:",a.sqr(3))
print("Modulas:",a.mod(5,3))
print("Bye...")
'''

#__init__
'''
class Cal:
        def __init__(self,a,b):
            self.a=a
            self.b=b
        def add(self):
            c=self.a+self.b
            print (c)
        def sub(self):
            c=self.a-self.b
            print (c)
a=Cal(10,2)
a.add()
'''

#

class Management:
  
  '''
    def __init__(self,u,p):
        self.u=u
        self.p=p'''
  def authenticate(self,u,p):
    self.u=u
        self.p=p
        if (self.u=="Karthi" and self.p=="Karthi@123"):
            print("Successfully Authenticate")
            return True
        else:
            print("login failed")
            return False
class Student(Management):
    def __init__(self,u,p,m,st):
        self.m=m
        self.st=st
        loginstatus=super(Student,self).authenticate(u,p)
        if loginstatus:
            self.display()
    def display(self):
        print(self.m)
        print(self.st)
a=Student("Karthi","Karthi@123",[85,67,93,88,46],10)


#
'''
class Base:
    def __init__(self,w,b):
        self.test_water=w
        self.test_bottle=b
    def getwater(self):
        print("Get Hot {0} in {1}".format(self.test_water,self.test_bottle))
class Sub(Base):
    def getwater(self):
        super(Sub,self).getwater()
        print("Get cold {0} in {1}".format(self.test_water,self.test_bottle))
a=Sub("water","Officebottle")
a.getwater()
'''

#
'''
n=int(input("Enter the number: "))
sn=7
c=0
if(n==7):
    print("Successfullly Guessed")
else:
    print("Try Again")
    c+=1
    while(c==3):
        print("Game Over")
'''

#
'''
sn=7
c=3
for i in range(c):
    n=int(input("Enter the number: "))
    
    if n==sn:
        print("Successfully Guessed")
        break
    
    else:
        print("Try Again")
print("Game Over")    
'''

#
'''
started=False
while True:
    cmd=input()
    if cmd=="start":
        if started:
            print("Car already started")
        else:
            print("Car Started...Ready to Go!")
            started=True
    elif cmd=="stop":
        if not started:
            print("car already Stopped..")
            
        else:
            print("car Stop..")
            started=False
    elif cmd=="quit":
        break
    elif cmd=="help":
        print(start - to start
                    stop - to stop
                    quit - exit)
    else:
        print("I dont understand that...")
''' 
