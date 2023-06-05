n=int(input())
s1=0
s2=0
if n%2==0:
    n=n//2
    print(6*(n-1))
else:
    n=n//2+1
    print(7*(n-1))


n=int(input())
x=0
y=0
for i in range(1,n+1):
    if n%2!=0:
        x=x+7
    else:
        y=y+6
if n%2!=0:
    print(x)
else:
    print(y)
    n=n//2
    print(3**(n-1))
else:
    n=n//2+1
    print(2**(n-1))
    