def deco(func):
    def f1():
        print("hello!")
        func()
        print("bye!")
    return f1

def name():
    print("My name is saiteja.")

x=deco(name)
x()

