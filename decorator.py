#
def fun1(fun2):
    def innerfun():
        print(fun2)
        print("i got decorator")
        fun2()
    return innerfun

@fun1
def ordinary():
    print("I am ordinary")

ordinary()



def fun1(fun2):
    
    print(fun2)
    print("i got decorator")
    fun2()
    return innerfun

@fun1
def ordinary():
    print("I am ordinary")




