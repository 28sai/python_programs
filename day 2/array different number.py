#give an array of size n everu num is repeated twice except one
#num print that number?
l=[]
n=int(input())
c=0
for i in range(0,n):
    l.append(int(input()))
for x in l:
    c^=x
print(c)

l=[1,1,2,2,3,3,4,4,5,6,5,6,7]
c=0
for i in l:
    c=c^i
print(c)


	