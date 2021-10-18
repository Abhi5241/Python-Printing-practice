n=3

m=n//2
for i in range(n):
    for j in range(n):
        if i+j==m or j-i==m or i-j==m or i+j==n+m-1:
            print("*",end=" ")
        else:
            print(end="  ")

    print()