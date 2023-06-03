#give a number n abnnd integer i find out if ith bit is set or not?
n=int(input())
i=2
if 1&(n>>i)==1:
    print("set bit")
else:
    print("not set")
print()
n=int(input())
i=2
if n&(1<<i)==0:
    print("not set bit")
else:
    print("set bit")
