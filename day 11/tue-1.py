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
