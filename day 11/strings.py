x='sai\'s chocolate'
print(x)
print()
s="Sai"
y=" teja"
print(s+y)
print((s+y).title())
print(f"hello {x}")
print(x.upper())
print(x.lower())
print(x.isupper())
print(x.islower())
print(x.replace("chocolate","pen"))
print(x.split())
print(x.center(32,"@"))
print(x.capitalize())
x="  saiteja"
print(x)
print(x.strip())
print(x.count('a'))
print(len(x))
print("********")

x="sas"
if x[::-1]==x[0:]:
    print("it is pallindrome")
else:
    print("it is not")
print("***************")
for i in x:
    print(i)
print("***************")

y="hello saiteja"
z=y.count('a')
print(z)
print(y.replace("a",""))
print("*************")
x="saiteja got 99th rank in the class"
print(x[0:4])
print("****************")

print(x.replace(x[0:4],x[4:]))

print("****************")
for i in x:
    if i.isnumeric():
        print(i,end="")
print()
x="saisaiteja"
print(set(x))

