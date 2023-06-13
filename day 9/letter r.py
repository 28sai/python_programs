n=5
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(n-1):
        if(i==j or j==0):
            print("*",end=" ")
        else:
            print("_",end=" ")
        
