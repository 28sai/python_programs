n=int(input())
c=0
for i in range(4):
    c=c<<1
    c=c|(n&1)
    n=n>>1
print(c)