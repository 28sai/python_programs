n=int(input())
x=n**2
s1=str(n)
s2=str(x)
if s2[-len(s1):]==s1:
    print("yeees")
else:
    print("no")