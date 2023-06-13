x=["sai","sanjay","rohith","keerthan"]
y=[]
for i in x:
    if(i[0]=='s'):
        y.append(i)
print(y)

z=[2**x for x in range(1,10) if x%2==0]
print(z)

l1=[i for i in range(100,300,30)]
print(l1)

l2=[i for i in range(1,6) if i<5 ]
print(l2)


l3=[x for x in range(150,180)]
print(l3)
l4=[i for i in l3 if i%2==0]
print(l4)

l5=[i for i in l3 if i%2!=0]
print(l5)

l6=[i for i in range(1,11)]
print(l6)
l7=["even" if i%2==0 else "odd" for i in range(1,11)]
print(l7)

