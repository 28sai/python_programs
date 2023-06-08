n=int(input())
s=0
while(n!=0):
    r=n%10
    s=s+r
    n=n//10
if n%s==0:
    print("harshed ")
else:
    print("not")