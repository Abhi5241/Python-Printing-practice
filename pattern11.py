a=int(input("enter the number of rows:\n"))
i=0
while(a>i):
    star=i+1
    while star>0:
        print("*",end="")
        star=star - 1
    i=i+1
    print()