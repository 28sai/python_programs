#wap to caliculate sum of list  of vlaues using reduce() fn
from functools import reduce
l1=[10,20,30]
print(reduce(lambda i,y:(i+y),l1))

import reduce from functools 
def add(x,y):
    return x+y
nums=[10,20,30]
print(reduce(add,nums))