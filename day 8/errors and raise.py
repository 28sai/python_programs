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

a=5
b=0
try:
    print(a/b)
except Exception as e:
    print("a num cant be divide by zero",e)
finally:
    print("closed")
print("*********************")
print()
def div(x,y):
    return x/y
def calc(x,y):
    y=y*div(x,y)
try:
    calc("hello",5)
    z=divide(5,0)
    print(z)
except TypeError:
    print("it is a type error")
except NameError:
    print("it is a name error")
except ZeroDivisionError:
    print("it is zero division error")
except ValueError:
    print("it is value error")
finally:
    print("no error")
print("program is executed")
print("*********************")
print()
x=101
if x%2!=0:
    raise Exception("x should be even num")
else:
    print("x is even number")
