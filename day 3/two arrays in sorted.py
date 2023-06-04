a=[-4,-2,1,3,7,9,10]
b=[-1,5,11]
c=a+b
print(sorted(c))
print("************************")
a=[-4,-2,1,3,7,9,10]
b=[-1,5,11]
a.extend(b)
x=0
for i in range(len(a)):
    flag=0
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            x=a[j]
            a[j]=a[j+1]
            a[j+1]=x
            flag=1
    if flag==0:
        break
print(a)
        
