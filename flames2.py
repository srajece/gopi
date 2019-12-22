#

string1=input("Enter the String One: ").lower()
string2=input("Enter the String Two: ").lower()
string1=list(string1)
string2=list(string2)
for i in range(len(string1)):
    for i in string1:
        for j in string2:
            print(i,j)
            if i == j:
                string1.remove(i)
                string2.remove(j)
                print(string1,string2)
                break
string=(string1+string2)

