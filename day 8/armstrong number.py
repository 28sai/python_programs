n=int(input())
s=0
x=n
while(n>0):
    r=n%10
    s=s+(r*r*r*r*r)
    n=n//10
if(x==s):
    print("arm")
else:
    print("not arm")
