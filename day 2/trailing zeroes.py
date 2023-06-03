#trailing zeroes
n=int(input())
c=0
for i in range(n):
    if(n>>i)&1:
        break
    else:
        c+=1
print(c)
print()
n=int(input())
c=0
while(not(n&1)):
    c+=1
    n>>=1
print(c)
