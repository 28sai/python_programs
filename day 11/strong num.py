n=int(input())
s=0
x=n
while(n):
    i=1
    fact=1
    r=n%10
    while(i<=r):
        fact*=i
        i+=1
    s+=fact
    n=n//10
if(x==s):
    print("strng ")
else:
    print("not strng")
