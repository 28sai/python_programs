s1="mississippi"
s2="i"
if s2.isupper() :
    s1=s1.replace(s2,chr(ord(s2)+32))
else:
    s1=s1.replace(s2,chr(ord(s2)-32))
print(s1)