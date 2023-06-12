#give an array of size n everu num is repeated twice except one
#num print that number?
l=[]
n=int(input())
c=0
for i in range(0,n):
    l.append(int(input()))
print(l)
for j in range(len(l)):
    for k in range(len(l)):
        if(l[i]==l[j]):  
            c+=1
if c!=1:
    print(l[i])

