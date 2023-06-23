def sum(n):
   if n<=1:
       return n
   else:
       return n+sum(n-1)
n=int(input())
if n<0:
   print("enter pos num")
else:
   print(sum(n))


def fact(n):
   if n==0:
       return 1
   return n*fact(n-1)
r=fact(6)
print(r)
