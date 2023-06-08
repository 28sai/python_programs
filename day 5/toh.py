def toh(n,a,b,c):
    if n==1:
        print(a,b)
        return
    toh(n-1,a,c,b)
    print(n,a,b)
    toh(n-1,c,b,a)
n=4
toh(4,1,2,3)
