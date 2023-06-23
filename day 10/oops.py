class comp:             #class definition
    def config(self):   #config is a fucntion
        print("hello")
sam=comp()              #object 1
sam.config()

dell=comp()             #object 2
dell.config()
print("**************************************************")

class student():
    stname="sai"
    stroll=2035
    stbranch="CSE"

    def toprint(self):
        stname="saiteja"
        print("local variable is :",stname)
        print("class variable/instance variable is :",self.stname)
        print("class variable/instance variable is :",self.stroll)
        print("class variable/instance variable is :",self.stbranch)
    def fun2(self):
        print("second function")
s1=student()
s2=student()
print(s1.stroll)
print(s1.stbranch)
print("s2 ",s2.stname)
s1.toprint()
s2.toprint()
s2.fun2()
print("**************************************************")
class car:
    def __init__(self,modelname,year):
        self.modelname=modelname
        self.year=year
    def display(self):
        print(self.modelname,self.year)
c1=car("bmw",2023)
c2=car("benz",2022)
c1.display()
c2.display()
print("**************************************************")

