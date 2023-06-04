l=[0,1,0,1,1,0,1]
x=0
for i in range(len(l)):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            x=l[j]
            l[j]=l[j+1]
            l[j+1]=x
print(l)
print("***************")


l=[0,1,0,1,1,0,1]

