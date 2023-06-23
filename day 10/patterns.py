n=5
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()

n=5
for i in range(n):
    for j in range(n):
        if(j==0 or j==n-1):
            print("*",end=" ")
        if(i==j or i+j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()