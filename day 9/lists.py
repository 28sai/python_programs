"""l=[]
l.append("saiteja")
l.append("sanjay")
l.append("rohith")
print(l)
print(type(l))
print(l[0:])
print(l[1:])
print(l[-1])
print(l.remove("rohith"))
print(l)
print(l.extend([5,6]))
print(l)
y=[1,2,3,7,5,3,8,6,9]
print(y.extend([l]))
print(y)
print(y.insert(3,"rohith"))
print(y)
print(y.remove("rohith"))
print(y)
print(y.pop())
print(y)
print(y.index(3))
print(y)
print(l)
print(y.copy())
print(y.sort())
y.reverse()
print(y)
l1=y.copy()
print(l1)
y.sort()
print(y)
print(y.count(3))
print(len(y))
print("*************************")
x=[1,2,3,4,5,2.7,4.6,5.6,"sai","teja"]
print(x[0:])
for i in x:
    print(i)

for j in range(9):
    print(x[j])
print("*************************")
e=[]
o=[]
x=[1,2,3,4,5,6,7,8,9,10]
for i in x:
    if(i%2==0):
        e.append(i)
    else:
        o.append(i)
print(e)
print(o)
print("**************************")
l=[]
s=0
size=int(input("enter size:"))
for i in range(size):
    ele=int(input("enter elements"))
    l.append(ele)
print(l)
for i in l:
    s+=i
print(s)
if s%2==0 and s%5==0:
    print("it is divi")
else:
    print("it isi not")
"""
x=["v","e","r","y","g","o","o","d","d","a","y"]
print(x[4:8])


