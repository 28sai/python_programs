#lambda function general syntax
#lambda args : expression
def small(a,b):
    z=(a if a<b else b)
    print(z)
s=lambda x,y:x+y
d=lambda x,y:x-y
print(s(9,5))
print(d(8,5))
print(small(s(9,5),d(8,5)))

# program to use lambda function within a regular fn
def inc(y):
    return (lambda x:x+1)(y)
a=100
print(a)
b=inc(a)
print(b)


lambda s:s(range(1,11))
print(a())
    