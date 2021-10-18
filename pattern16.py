n=int(input("enter the no of row:\n"))
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(format(num,"<2"),end=" ")
        num +=1
    print()