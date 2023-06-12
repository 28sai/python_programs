""" get lst of numbers as input return the product less than 750 else return sum
printy multiplication table for ythe giben number
gind oyt and prit given num is prie or nor
get one char as inut and diss[paly reainbow colrs if the character is in vibgyor
if not  display entr rainbow char
ger a num as input chrck if it is the hifheest or lowesr of 3 digit number
"""


def f1():
    l=[]
    x=1
    s=0
    n=int(input("size:"))
    for i in range(n):
        n=int(input("elements:"))
        l.append(n)
    print(l)
    for i in l:
        x=x*i
        s=s+i
    if(x<=750):
        print(x)
    else:
        print(s)
        
f1()
print("*************************")
print()
def mul():
    n=int(input("enter num:"))
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
mul()
print("*************************")
print()
def f2():
    y="vibgyor"
    x=input()
    if x in y:
        print("vibgyor")
    else:
        print("enter vibgyor color")
f2()

def f3():
    n=int(input())
    if(n==999):
        print("it is highest")
    elif n==100:
        print("it is lowest")
    elif(n>=101 or n<=998):
        print("it is in midrange of 100 AND 999")
f3()
print("*************************")
print()
def f4():
    n=int(input("enter a number"))
    p=0
    for i in range(1,n+1):
        if n%i==0:
            p=p+1
    if p==2:
        return 1
    else:
        return 0
c=f4()
if c==1:
    print("it is prime")
else:
    print("it is not")
