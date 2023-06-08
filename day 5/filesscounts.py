w=0
s=0
c=0
l=0
with open("sai.txt","r") as f:
    for line in f:
        l=l+1
        word='y'
        for letter in line:
            if letter!=" " and word=="y":
                w=w+1
                word='n'
            elif letter==" ":
                s+=1
                word='y'
            for i in letter:
                if(i !=" " and i !="\n"):
                    c+=1
print(w)
print(s)
print(c)
print(l)

                    
                        