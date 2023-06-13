class A:
    n=30
class B(A):
    def calc(self):
        c=self.n+70
        print(c)
obj=B()
obj.calc()
print("**************************************")
print("multi inheritence")
class mom:
    def mdisplay(self):
        print("mom class")
class dad:
    def ddisplay(self):
        print("dad class")
class child(mom,dad):
    def cdisplay(self):
        print("child class")
c1=child()
c1.cdisplay()
c1.mdisplay()
c1.ddisplay()
print("***************************************")
print("multilevel inheritence")
print("***************************************")
print("multi hierarchical inheritence")

