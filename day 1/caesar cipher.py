n=str(input("Enter number:"))
for i in n:
    print(chr(ord(i)+1),end=" ")
print("\n****************")
print(chr(90))
print("\n****************")
message="danger"
index=0
while index<len(message):
    letter=message[index]
    print(chr(ord(letter)+1),end=" ")
    index+=1
