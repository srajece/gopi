#factorial of given number
class Factorial:
    def fact(self,n):
        f=1
        if n==0:
            print("sorry")
        elif n<0:
            print("its negative number")            
        else:
            for i in range(1,n+1):
                    f=f*i
            print("Factorial of",n,"is",f)
n=int(input("Enter the Number: "))
a=Factorial()
a.fact(n)
