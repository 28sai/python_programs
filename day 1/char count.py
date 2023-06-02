n=input()
i=1
c=1
while(i<len(n)):
    if n[i]==n[i-1]:
        c+=1
    else:
        print(n[i-1],end=",")
        print(c,end=",")
        c=1
    i+=1
print(n[i-1],end=",")
print(c)