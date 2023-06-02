x=int(input())
s=0
y=[]
for i in range(0,x+1):
    a=float(i)/(i+1)
    y.append(a)
    s+=a
print(s)
print(y)
print(y[5])


