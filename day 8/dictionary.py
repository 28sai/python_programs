x={"sai":"pocox3pro","sanjay":"samsum","rohith":"redmi"}
print(x["sai"])
print(x.items())
print(x.keys())
print(x.values())
print()
x={"sai":"blue&green","sanjay":"purple","rohith":"blue","babu":"red","keerthan":"black"}
print(x)
print(x.items())
print(x.keys())
print(x.values())
print(x.update({"teja":"iphone"}))
print(x.pop("babu"))
print(x.popitem())
print(x.setdefault("babu","red"))
print(x)

d={n:n*n for n in range(1,5)}
print(d)

old={"rice":60,"dhal":120,"oil":150}
new={product:price*5 for product,price in old.items()}
print(new)

real={"sai":1,"sanjay":2,"rohith":3}
now={name:age for name,age in real.items() if age<3}
print(now)


d1={"sai":"hruthikroshan","sanjay":"ramcharan","rohith":"sampoorneshbabu"}
print(d1)
res={name:hero for name,hero in d1.items() if hero is "sampoorneshbabu"}
print(res)

print("*************iterable and .from keys***********")






