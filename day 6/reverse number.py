#wap to print the count down timer from n to 0 using a while loop only

    
#wap to take he 3 digit input let n=123 and print the number in a reverse order
n=123
n=str(n)
for i in n:
    x=n[::-1]
print(x)

n=123
s=0
while(n!=0):
    r=n%10
    s=s*10+r
    n=n//10
print(s)

    