l=[1,1,1,2,2,2,3,3,3,4,4,7,4,5,5,6,6,5,6]
for i in l:
    c=0
    for j in l:
        if i==j:
            c+=1
    if c==1:
        print(i)
        break
print("*****************")
l=[1,1,2,2,3,3,4,7,4,5,6,5,6]
c=0
for i in l:
    c= c ^ i
print(c)
print("*****************")
l=[1,1,2,2,3,3,4,7,4,5,6,5,6]
for i in range(32):
    c=0
    ans=0
    for j in l:
        if len&(1<<j)==0:
            c+=1
    if c%3==0:
        ans=ans|(1<<i)
print(ans)
