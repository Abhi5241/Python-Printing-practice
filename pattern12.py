num=int(input("enter the input"))
row=0
while row<num:
    space=num-row-1
    while space>0:
        print(end=" ")
        space=space-1

    star=row+1
    while star>0:
        print("*",end=" ")
        star=star-1
    print()
    row=row+1


