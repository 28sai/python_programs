x=str(input())
n=1
out=" "
for i in range(len(x)):
    ch=x[i]
    if ch==" ":
        out+=" "
    elif(ch.isupper()):
        out+=chr((ord(ch)+n-65)%26+65)
    else:
        out+=chr((ord(ch)+n-97)%26+97)
print(out)

x=str(input())
for i in x:
    x=ord(i)
    print(chr(x+1),end=" ")


