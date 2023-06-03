def pow(n):
    while(n!=1):
        if(n%2!=0):
            return False
        n=n//2
    return True
n=int(input())
if pow(n):
    print("yes")
else:
    print("no")

n=int(input())
if n&(n-1)==0:
    print("yes")
else:
    print("no")
    
