import random as r
num=r.randint(1,10)
n=int(input("guess the num:"))
while(num!=n):
    n=int(input("guess the num again:"))
    if(n==num):
        print("won")
    elif(n>num):
        print("high")
    elif(n<num):
        print("low")
    
