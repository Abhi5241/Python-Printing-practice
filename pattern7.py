string=input("enter the string")
length=len(string)
for i in range(length):
    for j in range(i+1):
        print(string[j],end="")
    print()
