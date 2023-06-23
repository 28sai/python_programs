"""num=int(input("enter a number::"))
s=0
r=0
x=num
while(num>0):
    r=num%10
    s=s*10+r
    num=num//10
if(x==s):
    print(f"{x} is a pallindrome")
else:
    print(f"{x} is not a pallindrome")
print("\n")
n=int(input("enter a number:"))
fact=1
for i in range(2,n+1):
    fact*=i
print(f"{fact} is the factorial of {n}")
print("\n")
n1=int(input("enter a number"))
if n1%7 == 0 or n1%7 == 7:
    print(f"{n1} is buzz number")
else:
    print(f"{n1} is not a buzz number")
print("\n")
n2=input("enter a cahracter")
if n2 in "aeiouAEIOU":
    print(f"{n2} is character")
else:
    print(f"{n2} is not a character")

print("\n")
print("fhsdkjafjk \njdsfjaskdj fsdajfksj \n isdklfjiodsjkfjioadslksfadshjk \n herifhsdnjkfhskjcn \n hsdfjknakjhfusdkjfh uhfsdj\n shdjkhfkjhasddkfh skjfkj")
print("\n")
n3=int(input("enter a number"))
n4=float(input("enter a number"))
n5=float(input("enter a number"))
print(f"{n3} ,{n4} ,{n5} are given numbers")
print("\n")
n6=float(input("enter a number"))
n7=float(input("enter a number"))
n8=float(input("enter a number"))
n9=float(input("enter a number"))
n10=float(input("enter a number"))
sum=int(n6+n7+n8+n9+n10)
print(sum)
print(abs(4.6))


n1=int(input("1st num:"))
n2=int(input("2nd num:"))
print("sum:",n1+n2)
print("sub:",n1-n2)
print("mul:",n1*n2)
print("div(without decimal):",n1//n2)
print("div:",n1/n2)
print("rem:",n1%n2)

n=5
for i in range(n):
    print(i*"*")
n=5
for i in range(0, n):
    for j in range(0,n-i,- 1):
        print(end=" ")
    for j in range(0,i+1):
        print("*", end=" ")
    print()
print(10>30)
print(10==20)
print(5&1)
print(6|1)
print( 6>4 and 5<6)
print(8<=8 or 7>9)
print(6 is not 7)
print(6 != 7)
x="sai teja"
print("sai" in x)
print("ai" in x)"""

"""age= int(input("enter ur age"))
if age>=18:
    print("u are eligible to vote")
else:
    print("not eligible")

take two inputs one is city name and temp acco to thr temp display weather report as
hot cold mpoderate constraints: above 40 hot
and 5 to 15 cold
and 0 to 5 colder
moderate 16 to 90


city=input("enter city name:")
temp=int(input("enter temparature:"))
if temp>=40:
    print("it is hot")
elif temp>=5 and temp<=15:
    print("it is cold")
elif temp>=0 and temp<=5:
    print("colder")
elif temp<0:
    print("coldest")
elif temp>=16 and temp<=39:
    print("moderate")"""
    




print("\n")

n = 5
for i in range(n,-1,-1):
    for j in range(n,0,-1):
        print(end=" ")
    n=n+1
    for j in range(0,i+1):
        print("* ",end="")
    print("\r")

kumar=75
sam=kumar/2
kumar=sam/2
print(sam/2+sam)

x=36.32
y=x*3
z=y+56.19
fr=z-10
print(fr)

n3=6
n4=-6.1
print(n3*n4)

n1=36.0
n2=6.0
print(n1/n2)






