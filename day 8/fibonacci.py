def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=int(input("enter number:"))
if n<=0:
    print("pos num")
else:
    for i in range(n):
        print(fib(i))



print("*********************************")
def addition(n):
    return n+n
def multiplication(n):
    return n*n
#we double all numbers using map()
numbers=(1,2,3,4)
result=map(addition,numbers)
res1=map(multiplication,numbers)
print(list(result))
print(list(res1))
print("**********************************")
a=list(map(in(input().split(''))))
for i in a:
    print(i,end='')
print("**********************************")
#one parent and one child class
class parent:

