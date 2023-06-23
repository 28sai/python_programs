saiteja='1'
sanjay='4'
rohith='3'
print(saiteja+sanjay+rohith,"sansairoh")
print(0/1)

def divide(x,y):
    return x/y
try:
    x=divide(1/0)
except ZeroDivisionError:
    print("zero division error")
