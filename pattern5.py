n=int(input("enter the number of row:\n"))
for i in range(n):
    for j in range(n):
        if i==0 or j==n-1 or i==j:
            print("*",end=" ")
        else:
            print(end="  ")
    print()